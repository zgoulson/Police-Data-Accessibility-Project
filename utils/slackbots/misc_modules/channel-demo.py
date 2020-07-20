import os
from slack import WebClient
from slack.errors import SlackApiError
from dotenv import load_dotenv
load_dotenv()
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
client = WebClient(token=SLACK_BOT_TOKEN)

def list_channels():
    response = client.conversations_list()
    conversations = response["channels"]
    return conversations

def channel_info(channel_id):
    response = client.conversations_info(
    channel=channel_id,
    include_num_members=1
    )
    if response:
        return response['channel']
    return None


if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
            detailed_info = channel_info(c['id'])
            if detailed_info:
                print(detailed_info['purpose']['value'])
    else:
        print("Unable to authenticate.")
