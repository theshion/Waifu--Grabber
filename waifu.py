from pyrogram import Client, filters
from pyrogram.types import Message

# Replace 'API_ID' and 'API_HASH' with your actual API credentials
API_ID = "25071254" 
API_HASH = '5cb7bac198160c6dcf76f11da7b26a45'
SESSION_STRING = "BQF-jpYAAV5gjpV7tKgskfviPIgijHtol_5LbBuK7IWVRNkSILDTPR-I_zJsmATIP94duKNrT08AGkNFkT2ADnX16td9ND0ELKOZu7TUZzjV6VXYDJYIJHU9soS4_Ep_zmLthuBs_yTQH2rfe6F71O09VQ33QG45bCaGLqjVyplnmRr-2kY6dTMeGv1ejw_uiahPFh1beyK1BLFpQh7joxyEow8sXU3iivUEtX6ApCYHTyHu1-71AUV1aYNOELr0-hnMfRpDN4W0xNGCcXiL_cKojnW_j50sKz4B8eaw_yTdQp6-L_IqqiGHOlXZKkvOzHAhYwMTjDyv8FQIii2XDuR4L5DymwAAAAGPazsjAA" # Your String Session Here 
CLIENT_NAME = "shion"  # Any Random Name

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
