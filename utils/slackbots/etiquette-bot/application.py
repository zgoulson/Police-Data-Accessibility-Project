from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def verify():
    data = request.json
    if data['event']['type'] == 'app_mention':
        user_text = data['event']['text']
        user = data['event']['user']
        webhook_url = '***********Your webhook url******************'
        slack_data = { "text": 'How can I help you ?' }
        response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
        )
    return('', 204)

if __name__ == '__main__':
app.run(debug=True,port=3000)
