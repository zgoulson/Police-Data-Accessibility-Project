import os
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter
from slack import WebClient
load_dotenv()

# Create a SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
slack_client = WebClient(SLACK_BOT_TOKEN)

# Our app's Slack Event Adapter for receiving actions via the Events API
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events")

# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    if emoji == 'thread':
        channel = event["item"]["channel"]
        message_author = event["item_user"]
        text = ":%s:" % emoji
        slack_client.chat_postMessage(channel=message_author, text=text)
    print(event)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)
