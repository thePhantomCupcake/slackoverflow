from lib2to3.pgen2 import token
import os
# Use the package we installed
from slack_bolt import App

import logging
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here

@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to _CD SlackOverflow_*! :tada: My name is, HAL."
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "To ask an anonymous question, just send me a message in the messages tab. I'll send it on to the cd_slack_overflow channel for someone to answer."
            }
          },
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")
    
@app.event("message")
def post_dm_as_mention(client, event, logger):
    try:
        result = client.chat_postMessage(
            channel='C0358S3AFK3',
            text=event['text']
        )

    except SlackApiError as e:
        print(f"Error: {e}")
  
# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))