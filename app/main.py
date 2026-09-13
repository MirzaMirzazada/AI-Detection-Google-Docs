"""Application entry point."""
from google_auth import get_credentials

from google_docs import (
    extract_document_id,
    get_document_text
)

from revision_analyzer import (
    get_revisions,
    analyze_revisions
)

from text_chunker import chunk_text

from ai_detector import analyze_chunks

from scoring import (
    calculate_ai_score,
    classify
)

from report import generate_report


def run_analysis(document_url):

    print("\nConnecting to Google...")

    credentials = get_credentials()

    document_id = extract_document_id(
        document_url
    )

    print("Reading Google Doc...")

    text = get_document_text(
        credentials,
        document_id
    )

    print(
        f"Document contains "
        f"{len(text.split())} words."
    )

    print("\nReading revision history...")

    revisions = get_revisions(
        credentials,
        document_id
    )

    revision_stats = analyze_revisions(
        revisions
    )

    print(
        f"Found "
        f"{revision_stats['revision_count']} revisions."
    )

    print("\nSplitting document...")

    chunks = chunk_text(text)

    print(
        f"Created {len(chunks)} chunks."
    )

    print("\nRunning Hugging Face detector...")

    ai_results = analyze_chunks(
        chunks
    )

    print("\nCalculating score...")

    final_score = calculate_ai_score(
        ai_results,
        revision_stats
    )

    classification = classify(
        final_score
    )

    report = generate_report(
        document_url,
        revision_stats,
        ai_results,
        final_score,
        classification
    )

    print("\n")
    print(report)

    with open(
        "reports/report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print(
        "\nReport saved to reports/report.txt"
    )


if __name__ == "__main__":

    url = input(
        "Paste Google Docs URL: "
    )

    run_analysis(url)