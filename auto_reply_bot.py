from telethon import TelegramClient, events

# Set your credentials here
api_id =24222039   # Replace with your actual API ID
api_hash = '6dd2dc70434b2f577f76a2e993135662'  # Replace with your actual API Hash
group_id = '-1001702618096'  # Replace with your actual group ID or username

client = TelegramClient('my_session', api_id, api_hash)

@client.on(events.NewMessage(chats=group_id, incoming=True))
async def my_event_handler(event):
    # Customize your reply message here
    reply_message = "Hey 👋🏻 😍



📫 𝗬𝗼𝘂𝗿 𝗙𝗶𝗹𝗲 𝗶𝘀 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗛𝗲𝗮𝗿

••••••••••••••••••••••••••••••••••••••••
👉  @Fundamongobot
👉  @Fundamongobot
👉  @Fundamongobot
👉 @Fundamongobot
👉  @Fundamongobot
👉 @Fundamongobot
👉  @Fundamongobot
👉  @Fundamongobot
••••••••••••••••••••••••••••••••••••••••

𝗣𝗮𝗴𝗲𝘀 📄  ◾   𝟭/𝟮  ◾  𝗡𝗲𝘅𝘁 ⏩"  # Change this to your desired reply message
    await event.reply(reply_message)

# Start the client
client.start()
print("Auto-reply bot is running...")
client.run_until_disconnected()
