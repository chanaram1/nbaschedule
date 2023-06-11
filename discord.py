from discord_webhook import DiscordWebhook
from nba import schedule

# Call the schedule function from nba.py
games = schedule()

# Create a string with the schedule information
schedule_text = ""
for game in games:
    schedule_text += game + "\n"

# Create the Discord webhook with the schedule content
webhook = DiscordWebhook(url='webhook', content=schedule_text)

# Execute the webhook to send the message to Discord
response = webhook.execute()
