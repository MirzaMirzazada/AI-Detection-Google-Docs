from transformers import pipeline


MODEL_NAME = "Hello-SimpleAI/chatgpt-detector-roberta"


print("Loading Hugging Face model...")

detector = pipeline(
    "text-classification",
    model=MODEL_NAME
)

print("Model loaded.")


def detect_ai(text):

    result = detector(
        text,
        truncation=True
    )

    prediction = result[0]

    return {
        "label": prediction["label"],
        "score": float(
            prediction["score"]
        )
    }


def analyze_chunks(chunks):

    results = []

    for index, chunk in enumerate(chunks):

        print(
            f"Analyzing chunk "
            f"{index + 1}/{len(chunks)}..."
        )

        result = detect_ai(chunk)

        results.append({
            "chunk": index + 1,
            "label": result["label"],
            "score": result["score"],
            "word_count": len(
                chunk.split()
            )
        })

    return results