import os
from telethon import TelegramClient, events

api_id = int(os.getenv('24222039'))
api_hash = os.getenv('6dd2dc70434b2f577f76a2e993135662')
group_id = os.getenv('-1001702618096')  # Now using environment variable

client = TelegramClient('my_session', api_id, api_hash)

@client.on(events.NewMessage(chats=group_id, incoming=True))
async def my_event_handler(event):
    reply_message = "Hey 👋🏻 😍 ... (Hey 👋🏻📫 𝗬𝗼𝘂𝗿 𝗙𝗶𝗹𝗲 𝗶𝘀 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗛𝗲𝗮𝗿
👉  @Fundamongobot)"
    await event.reply(reply_message)

client.start()
print("Auto-reply bot is running...")
client.run_until_disconnected()
