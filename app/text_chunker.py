def chunk_text(text, words_per_chunk=180):

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        words_per_chunk
    ):

        chunk = " ".join(
            words[i:i + words_per_chunk]
        )

        if len(chunk.split()) >= 50:
            chunks.append(chunk)

    return chunks