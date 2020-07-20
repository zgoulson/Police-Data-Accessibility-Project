# class AppHome:
#     """Constructs the Slack Bot Home Tab"""

def get_app_home_block(user, slack_admin):

    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Hi <@{user}> :wave:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Great to see you here! I am PDAP Slack Bot Mark I. I am still in the early stages of development. So far this is what I can do:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "• Help the Slack Moderators contact users violating our message :thread: policy \n "
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "If you have a suggestion or would like to help develop my functionalities please click one of the buttons below!"
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Join Slack Bot Development!",
                        "emoji": True
                    },
                    "value": "join_bot_dev_channel"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Contact a Slack Admin!",
                        "emoji": True
                    },
                    "value": "message_slack_admin"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"Author: <@{slack_admin}>",
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "plain_text",
                    "text": "Published: July 2020",
                            "emoji": False
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "Check out the source code in the <https://github.com/Police-Data-Accessibility-Project/Police-Data-Accessibility-Project|PDAP GitHub Repo>!"
                }
            ]
        }
    ]
    return blocks
