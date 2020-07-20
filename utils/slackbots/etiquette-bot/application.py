'''
Slack Channel Suggestions Bot

DM the author of a message that has been tagged with the :thread: emoji (likely by a Slack Mod).

Updated: July, 2020
Published: TBD

Features to add:
    - Configure App Home with information-security related items
    - Track message ids that have been moderated with a :thread: reaction
        - Check with Security Oversight on this
    - Eventually link to internal Slack documentation

'''

import os
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter
from slack import WebClient
load_dotenv()
from home import get_app_home_block

# SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
slack_client = WebClient(SLACK_BOT_TOKEN)

# Slack Event Adapter for receiving actions via the Events API
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events")

# this is currently Zach, but can be altered for any future admin or admin group
slack_admin = 'U014A5XS4JK'

# Reaction added events
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    if emoji == 'thread':  # Only processes the bot response if the emoji is :thread:
        channel = event["item"]["channel"]
        message_author = event["item_user"]
        message_id = event["item"]["ts"].replace(
            '.', '')  # remove . for URL compatibility
        moderator = event["user"]  # user who added the :thread: reaction
        text = (f'Hello there! <@{moderator}> marked your recent message posted in <#{channel}> for cleanup. '
                f'Please try to send only one message at a time or thread your messages to the initial message. '
                f'Doing so will help keep our channels clean and digestible for all. Thanks! Please send a direct message to <@{slack_admin}> '
                f'if you have any questions.\n\n'
                f'https://policeaccessibility.slack.com/archives/{channel}/p{message_id}')
        slack_client.chat_postMessage(channel=message_author, text=text)
        # for testing purposes. Sends duplicate message to Zach
        slack_client.chat_postMessage(channel=slack_admin, text=f'original author was <@{message_author}>' + text)
    print(event)  # for testing purposes

# App Home Opened events
@slack_events_adapter.on("app_home_opened")
def app_home_opened(event_data):
    event = event_data["event"]
    if ('tab' in event) and (event['tab'] == 'home'):
        user = event['user']
        blocks = get_app_home_block(user=user, slack_admin=slack_admin)
        views = {"type": "home", "blocks": blocks}
        slack_client.views_publish(user_id=user, view=views)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000, debug=True)
