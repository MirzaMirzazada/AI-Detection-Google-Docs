from googleapiclient.discovery import build
from datetime import datetime


def get_revisions(credentials, document_id):

    service = build(
        "drive",
        "v3",
        credentials=credentials
    )

    revisions = []

    page_token = None

    while True:

        response = service.revisions().list(
            fileId=document_id,
            pageSize=1000,
            pageToken=page_token,
            fields=(
                "nextPageToken,"
                "revisions("
                "id,"
                "modifiedTime,"
                "lastModifyingUser"
                ")"
            )
        ).execute()

        revisions.extend(
            response.get("revisions", [])
        )

        page_token = response.get(
            "nextPageToken"
        )

        if not page_token:
            break

    return revisions


def detect_editing_bursts(revisions):

    if len(revisions) < 2:
        return 0

    timestamps = []

    for revision in revisions:

        modified_time = revision.get(
            "modifiedTime"
        )

        if modified_time:

            timestamp = datetime.fromisoformat(
                modified_time.replace(
                    "Z",
                    "+00:00"
                )
            )

            timestamps.append(timestamp)

    timestamps.sort()

    bursts = 0

    for i in range(1, len(timestamps)):

        gap = (
            timestamps[i]
            - timestamps[i - 1]
        ).total_seconds() / 60

        # If two revisions happen
        # within 2 minutes, count it
        # as an editing burst.
        if gap <= 2:
            bursts += 1

    return bursts


def analyze_revisions(revisions):

    if not revisions:

        return {
            "revision_count": 0,
            "unique_users": 0,
            "editing_duration_hours": 0,
            "average_minutes_between_revisions": 0,
            "editing_bursts": 0
        }

    timestamps = []

    users = set()

    for revision in revisions:

        modified_time = revision.get(
            "modifiedTime"
        )

        if modified_time:

            timestamp = datetime.fromisoformat(
                modified_time.replace(
                    "Z",
                    "+00:00"
                )
            )

            timestamps.append(timestamp)

        user = revision.get(
            "lastModifyingUser"
        )

        if user:

            email = user.get(
                "emailAddress"
            )

            if email:
                users.add(email)

    timestamps.sort()

    if len(timestamps) > 1:

        total_seconds = (
            timestamps[-1]
            - timestamps[0]
        ).total_seconds()

        duration_hours = (
            total_seconds / 3600
        )

        intervals = []

        for i in range(
            1,
            len(timestamps)
        ):

            seconds = (
                timestamps[i]
                - timestamps[i - 1]
            ).total_seconds()

            intervals.append(
                seconds / 60
            )

        average_interval = (
            sum(intervals)
            / len(intervals)
        )

    else:

        duration_hours = 0
        average_interval = 0

    # Calculate editing bursts
    burst_count = detect_editing_bursts(
        revisions
    )

    return {

        "revision_count": len(
            revisions
        ),

        "unique_users": len(
            users
        ),

        "editing_duration_hours": round(
            duration_hours,
            2
        ),

        "average_minutes_between_revisions": round(
            average_interval,
            2
        ),

        "editing_bursts": burst_count
    }