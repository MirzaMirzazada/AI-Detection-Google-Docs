def calculate_ai_score(
    ai_results,
    revision_stats
):

    if not ai_results:
        return 0

    ai_scores = []

    for result in ai_results:

        label = result["label"].lower()
        score = result["score"]

        # Convert model output into
        # an actual AI-likelihood signal.
        if "human" in label:
            ai_probability = 1 - score

        elif "chatgpt" in label or "ai" in label:
            ai_probability = score

        else:
            ai_probability = 0.5

        ai_scores.append(
            ai_probability
        )

    # Average AI likelihood across chunks
    ai_average = (
        sum(ai_scores)
        / len(ai_scores)
    )

    # --------------------------------
    # Revision behavior
    # --------------------------------

    revision_count = revision_stats[
        "revision_count"
    ]

    duration = revision_stats[
        "editing_duration_hours"
    ]

    burst_count = revision_stats[
        "editing_bursts"
    ]

    revision_signal = 0

    # Very few revisions can be a weak
    # signal of large text insertion.
    if revision_count <= 5:
        revision_signal += 0.15

    # Very short editing period.
    if duration > 0 and duration < 0.5:
        revision_signal += 0.15

    # Editing bursts are only a weak signal.
    if burst_count > 10:
        revision_signal += 0.05

    # --------------------------------
    # Combine signals
    # --------------------------------

    combined = (
        ai_average * 0.80
        +
        revision_signal * 0.20
    )

    return min(
        round(combined, 3),
        1.0
    )


def classify(score):

    if score >= 0.75:
        return "HIGH AI-LIKELIHOOD"

    elif score >= 0.50:
        return "MODERATE AI-LIKELIHOOD"

    else:
        return "LOW AI-LIKELIHOOD"