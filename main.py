import os, sys
import re
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import utils

load_dotenv()

app = App(token=os.getenv("SLACK_BOT_TOKEN"))


@app.message(r"^BUG")
def record_bug(message, say):
    user_id = message["user"]
    bug = utils.parse_bug(message["text"])
    bug_exists = utils.is_similar_bug_semantic(bug)
    if bug_exists != "":
        say(f"Hi <@{user_id}>.\nThe bug already exists with tracking {bug_exists}.")
        return
    tracking_id = utils.save_bug(bug)
    say(
        f"Hi <@{user_id}>.\nYour bug has been recorded. Tracking is {tracking_id}",
        thread_ts=message["ts"],
    )


@app.event("app_mention")
def mention_handler(body, say):
    say("Hello World!")


@app.message("hello")
def ask_who(message, say):
    print("got a message")
    say("FIRE HELLO WORLD")


if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
