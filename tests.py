import unittest
from utils import *


class TestUtils(unittest.TestCase):
    def test_parse_bug(self):
        self.assertDictEqual(
            parse_bug(
                "BUG\nType - Bug\nTeam - Chess\nLocation - <https://www.zuri.chat/channels/message-board/null>\nFix - This is my fix\nDescription - This is the description of the bug I found"
            ),
            {
                "type ": "Bug",
                "team ": "Chess",
                "location ": "<https://www.zuri.chat/channels/message-board/null>",
                "fix ": "This is my fix",
                "description ": "This is the description of the bug I found",
            },
        )


if __name__ == "__main__":
    unittest.main()
