"""Analysis report generation."""
from datetime import datetime


def generate_report(
    document_url,
    revision_stats,
    ai_results,
    final_score,
    classification
):

    lines = []

    lines.append(
        "AI-ASSISTED AUTHORSHIP ANALYSIS"
    )

    lines.append("=" * 60)

    lines.append(
        f"Generated: {datetime.now()}"
    )

    lines.append(
        f"Document: {document_url}"
    )

    lines.append("")

    lines.append(
        "OVERALL ASSESSMENT"
    )

    lines.append("-" * 60)

    lines.append(
        f"AI-likelihood score: "
        f"{final_score:.1%}"
    )

    lines.append(
        f"Classification: "
        f"{classification}"
    )

    lines.append("")

    lines.append(
        "REVISION ANALYSIS"
    )

    lines.append("-" * 60)

    for key, value in revision_stats.items():

        lines.append(
            f"{key}: {value}"
        )

    lines.append("")

    lines.append(
        "TEXT ANALYSIS"
    )

    lines.append("-" * 60)

    for result in ai_results:

        lines.append(
            f"Chunk {result['chunk']}: "
            f"{result['label']} "
            f"({result['score']:.1%})"
        )

    lines.append("")

    lines.append(
        "IMPORTANT NOTE"
    )

    lines.append("-" * 60)

    lines.append(
        "This report is an analytical indicator, "
        "not definitive proof of AI authorship."
    )

    return "\n".join(lines)