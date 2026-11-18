from datetime import datetime, timezone

def solve(value):
    return datetime.fromtimestamp(value, timezone.utc).isoformat()
