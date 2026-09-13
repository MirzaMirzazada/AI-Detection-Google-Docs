import re

from googleapiclient.discovery import build


def extract_document_id(url):
    match = re.search(
        r"/document/d/([a-zA-Z0-9-_]+)",
        url
    )

    if not match:
        raise ValueError("Invalid Google Docs URL")

    return match.group(1)


def get_document_text(credentials, document_id):

    service = build(
        "docs",
        "v1",
        credentials=credentials
    )

    document = service.documents().get(
        documentId=document_id
    ).execute()

    text = []

    body = document.get("body", {})

    for element in body.get("content", []):

        paragraph = element.get("paragraph")

        if not paragraph:
            continue

        for item in paragraph.get("elements", []):

            text_run = item.get("textRun")

            if text_run:
                text.append(
                    text_run.get("content", "")
                )

    return "".join(text)