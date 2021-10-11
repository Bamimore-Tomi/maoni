from typing import Tuple
import re, random, string

# BUG
# Type - Bug
# Team - Chess
# Location - https://www.zuri.chat/channels/message-board/null
# Fix - This is my fix
def parse_bug(text: str) -> dict:
    lines = [i.strip().split("-") for i in text.strip().split("\n")]
    lines_parsed = dict()
    for i, j in enumerate(lines):
        if len(j) < 2:
            continue
        elif len(j) > 2:
            lines_parsed[j[0].lower()] = "-".join(j[1:]).strip()
        else:
            lines_parsed[j[0].lower()] = j[1].strip()
    return lines_parsed


def random_string(lenght: int) -> str:
    return "".join([random.choice(string.ascii_lowercase) for i in range(lenght)])


def save_bug(db, bug: dict) -> str:
    tracking_id = random_string(5)
    bug["tracking_id"] = tracking_id
    db.bugs.insert_one(bug)
    return tracking_id
