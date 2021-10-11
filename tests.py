import unittest
import spacy, pymongo, os
from dotenv import load_dotenv
from utils import *

load_dotenv()
nlp = spacy.load("en_core_web_sm")
db = pymongo.MongoClient(os.getenv("DB_URL"))[os.getenv("DB_NAME")]


class TestUtils(unittest.TestCase):
    def test_parse_bug(self):
        self.assertDictEqual(
            parse_bug(
                "BUG\nType - Bug\nTeam - Chess\nLocation - <https://www.zuri.chat/channels/message-board/null>\nFix - This is my fix\nDescription - This is the description of the bug I found"
            ),
            {
                "type": "Bug",
                "team": "Chess",
                "location": "<https://www.zuri.chat/channels/message-board/null>",
                "fix": "This is my fix",
                "description": "This is the description of the bug I found",
            },
        )

    def test_is_similar_semantic(self):
        self.assertEqual(
            is_similar_semantic(
                "the boy is wearing a red shirt",
                "the boy is wearing a red shirt",
            ),
            1,
        )

    def test_is_similar_bug_semantic(self):
        new_bug = {
            "type": "Bug",
            "team": "Chess",
            "location": "<https://www.zuri.chat/channels/message-board/null>",
            "fix": "This is my fix",
            "description": "This is the description of the bug I found",
            "tracking_id": "qjvlw",
        }
        self.assertEqual(is_similar_bug_semantic(new_bug), "qjvlw")


if __name__ == "__main__":
    unittest.main()
