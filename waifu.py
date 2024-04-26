from pyrogram import Client, filters
from pyrogram.types import Message

# Replace 'API_ID' and 'API_HASH' with your actual API credentials
API_ID = "xxxxxx" 
API_HASH = 'xxxxxxx'
SESSION_STRING = "xxxxxxxx" # Your String Session Here 
CLIENT_NAME = "xxxx"  # Any Random Name

# Create a Pyrogram client with the provided session string
app = Client(session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH, name=CLIENT_NAME)

@app.on_message(filters.photo & filters.user(['Grab_Your_Waifu_Bot', 'Grab_Your_Husbando_Bot']))
def handle_waifu_bot_photo(client: Client, message: Message):
    # Reply to the photo with /waifu@collect_waifu_cheats_bot
    command = '/waifu@collect_waifu_cheats_bot'
    message.reply_text(command)

@app.on_message(filters.text & filters.reply & filters.user('Collect_Waifu_Cheats_Bot'))
def handle_waifu_reply(client: Client, message: Message):
    # Extract the character name from the reply
    character_name = message.text.splitlines()[0].replace("Character name:", "").strip()

    # Send /grab command with the extracted character name
    grab_command = f'/grab {character_name}'
    client.send_message(chat_id=message.chat.id, text=grab_command)

    print(f"Sent {grab_command} in response to /waifu reply")

# Run the application
app.run()
