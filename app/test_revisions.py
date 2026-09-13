from google_auth import get_credentials
from google_docs import extract_document_id
from revision_analyzer import (
    get_revisions,
    analyze_revisions
)


url = input("Paste Google Docs URL: ")

credentials = get_credentials()

document_id = extract_document_id(url)

revisions = get_revisions(
    credentials,
    document_id
)

print("\nREVISION HISTORY")
print("=" * 50)

for revision in revisions:

    print(
        revision.get("id"),
        revision.get("modifiedTime")
    )

print("\nANALYSIS")
print("=" * 50)

stats = analyze_revisions(
    revisions
)

for key, value in stats.items():

    print(
        f"{key}: {value}"
    )