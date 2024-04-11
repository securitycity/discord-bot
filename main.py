import discord
import aiohttp

PROXY = "http://81.91.139.76:8080"
message = "Hello Thanks for Your message"
# Create a Discord client
client = discord.Client(proxy=PROXY)

# Define your bot's token
TOKEN = ""

# Function to save user details to a text file
def save_user_details(sender_name, sender_id):
    with open("user_details.txt", "a") as file:
        file.write(f"Name: {sender_name}, ID: {sender_id}\n")

# Event: When the bot is ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# Event: When a message is received
@client.event
async def on_message(message):
    # Check if the message was sent in the desired server and channel
    if message.guild.name == "Your Server Name" and message.channel.name == "Your Channel Name":
        # Save sender's details
        sender_name = message.author.name
        sender_id = message.author.id
        
        # Save the user details to a text file
        save_user_details(sender_name, sender_id)
        
        # Send a message back to the sender
        await message.author.send(message)

# Run the bot with your token
client.run(TOKEN)