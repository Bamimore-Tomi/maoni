import re, random, string, sys, spacy, pymongo, os
from dotenv import load_dotenv

load_dotenv()
db = pymongo.MongoClient(os.getenv("DB_URL"))[os.getenv("DB_NAME")]


try:
    nlp = spacy.load("en_core_web_sm")
except:
    print("Install spacy model with - python -m spacy download en_core_web_sm")
    sys.exit(1)

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
            lines_parsed[j[0].lower().strip()] = "-".join(j[1:]).strip()
        else:
            lines_parsed[j[0].lower().strip()] = j[1].strip()
    return lines_parsed


def random_string(length: int) -> str:
    return "".join([random.choice(string.ascii_lowercase) for i in range(length)])


def save_bug(bug: dict) -> str:
    tracking_id = random_string(5)
    bug["tracking_id"] = tracking_id
    db.bugs.insert_one(bug)
    return tracking_id


def is_similar_semantic(first: str, second: str) -> int:
    doc1 = nlp(first)
    doc2 = nlp(second)
    return doc1.similarity(doc2)


def is_similar_bug_semantic(new_bug: dict) -> str:
    all_bugs = db.bugs.find()
    for i in all_bugs:
        if is_similar_semantic(new_bug["description"], i["description"]) > 0.7:
            return i["tracking_id"]
    return ""
