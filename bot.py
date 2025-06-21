import random
import asyncio
from datetime import datetime
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Configuration
API_ID = 22615428
API_HASH = "a7d711f54b17309b721d7cc51349e619"
STRING_SESSION = "1BZWaqwUAUFCkNErjb6vplKAD1phhGrWIlTRZgswABhYpPGd8z2aI6YzssYE7_M4BSVtxwBmQgkIuWAliCa26zcpXP1gQbo94Kh0sRR6ItC44pP7yktl06cxkNZBNHwErrzvOMad6C0bO7heDMDf7OHYkjvlUQ88u5ptSSbfsHzRrhmQK_h_xPSF_V9lc2xfwMWyGfxwoN5lowZO5lFOGexyuCILvKtMdmUrhWk8hCHPZoIFH4YHTcD4BTFIdsCnqxPoirXSiKHu7K2SyzjwoSeijEuos-IsXheUppJKCw1glTnV-qklOqxMVLz0G549fYxW4wolNQjioR_99h2HiuDIXjuB265Y="

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
START_TIME = datetime.now()

# Databases
GAALI_DB = [
    "Madarchod! 😡", "Bhen ke laude! 🤬", "Chutiya ho kya? 😒",
    "Gandu saala! 🍑", "Teri maa ki chut! 👿", "Bhosdiwale! 💢",
    "Landure! 🍆", "Chakke! 🏳️‍🌈", "Tere baap ne condom nahi pehna! 🚫🍌",
    "Naali ka keeda! 🐛", "Teri shakal dekh ke condom companies ka business badh gaya! 💸",
    "Tere jaise chutiyon ke liye hi to condom bana hai! 🎈",
    "Teri naani ko nanga nachaya! 👵💃", "Tere ghar mein suar palte hain kya? 🐷",
    "Teri aukaat gutter ke paani jaisi hai! 🚽", "Chal nikal laude! 👋",
    "Teri maa ki chut mein rocket launch kardunga! 🚀",
    "Tere jaise chutiye ko to main apni gaand se bhi nahi lagata! 🍑✋",
    "Teri shakal dekh ke to bhagwan bhi ro diye! 😭🙏",
    "Tere jaise chutiye ko to main apni jooti se bhi nahi maarta! 👟",
    "Teri maa ki chut mein Diwali manata hoon! 🎆",
    "Tere baap ne teri maa ko choda, aur tu paida ho gaya! 👶",
    "Teri shakal dekh ke to mirror bhi toot jaye! 🪨",
    "Tere jaise chutiye ko to main apni ungli se bhi nahi chhuta! 👆",
    "Teri maa ki chut mein Holi khelta hoon! 🎨",
    "Tere baap ne teri maa ko choda, aur tu paida ho gaya! 👶",
    "Teri shakal dekh ke to bhagwan bhi apna chehra chhupane lage! 🙈",
    "Tere jaise chutiye ko to main apni gaand se bhi nahi lagata! 🍑✋"
]

SHAYARI_DB = [
    "💔 Dard ka sahara hai tu... Zindagi barbaad kar di!",
    "❤️ Mohabbat mein toh hum mare bhi... Tum jeete raho!",
    "😢 Aankhon mein ashq, dil mein dard... Zindagi hai ya koi saza?",
    "🌹 Tumhare bina jeena mumkin nahi... Par tumhare saath jeena bhi mushkil hai!",
    "🔥 Dil todne wale... Khuda se daro!",
    "😔 Har dard bhula diya tune... Par jo dard diya hai wo nahi jata!",
    "💌 Mohabbat mein dhokha khaya hai... Ab to aadat si hai mujhko!",
    "😭 Tere ishq ne mar diya... Par teri yaad mein jeena pada!",
    "🌙 Raat bhar teri yaad satati hai... Subah tak neend nahi aati!",
    "💔 Tumhare bina jeena mumkin nahi... Par tumhare saath jeena bhi mushkil hai!",
    "😢 Tere bina zindagi adhuri hai... Par tere saath bhi to kuch khasa nahi!",
    "❤️ Mohabbat ka dard hai ye... Na khud jeene deta hai, na marne deta hai!",
    "😔 Tere ishq ne diwana bana diya... Ab har shaam rota hoon!",
    "💌 Tumhare liye to main mar bhi sakta hoon... Par tumhare bina jeena nahi!",
    "😭 Tere bina zindagi mein koi maza nahi... Par tere saath bhi to kuch khasa nahi!",
    "🌹 Mohabbat ka dard hai ye... Na khud jeene deta hai, na marne deta hai!",
    "🔥 Tere ishq ne diwana bana diya... Ab har shaam rota hoon!",
    "😢 Tumhare liye to main mar bhi sakta hoon... Par tumhare bina jeena nahi!",
    "💔 Tere bina zindagi adhuri hai... Par tere saath bhi to kuch khasa nahi!",
    "❤️ Mohabbat ka dard hai ye... Na khud jeene deta hai, na marne deta hai!",
    "😔 Tere ishq ne diwana bana diya... Ab har shaam rota hoon!",
    "💌 Tumhare liye to main mar bhi sakta hoon... Par tumhare bina jeena nahi!",
    "😭 Tere bina zindagi mein koi maza nahi... Par tere saath bhi to kuch khasa nahi!",
    "🌹 Mohabbat ka dard hai ye... Na khud jeene deta hai, na marne deta hai!",
    "🔥 Tere ishq ne diwana bana diya... Ab har shaam rota hoon!",
    "😢 Tumhare liye to main mar bhi sakta hoon... Par tumhare bina jeena nahi!",
    "💔 Tere bina zindagi adhuri hai... Par tere saath bhi to kuch khasa nahi!",
    "❤️ Mohabbat ka dard hai ye... Na khud jeene deta hai, na marne deta hai!",
    "😔 Tere ishq ne diwana bana diya... Ab har shaam rota hoon!",
    "💌 Tumhare liye to main mar bhi sakta hoon... Par tumhare bina jeena nahi!"
]

# Commands
@client.on(events.NewMessage(pattern='.ping'))
async def ping(event):
    uptime = datetime.now() - START_TIME
    await event.reply(
        "🤖 **Kira Bot Status**\n"
        f"🟢 **Online:** True\n"
        f"📶 **Ping:** {random.randint(1, 5)} ms\n"
        f"⏱ **Uptime:** {str(uptime).split('.')[0]}\n"
        f"💾 **RAM Use:** {random.randint(30, 60)}%\n"
        "⚡ **Powered By: [Kira Network](https://t.me/KiraNetwork)**"
    )

@client.on(events.NewMessage(pattern='.help'))
async def help(event):
    await event.reply(
        file="https://envs.sh/Quv.jpg",
        message="**📜 Kira Bot Commands:**\n\n"
               "🔹 `.spam 5 Hello` - Flood messages\n"
               "🔹 `.raid 3 @username` - 50+ Gaaliyan 🌶️\n"
               "🔹 `.shayari 2 @username` - 30+ Shayari 💔\n"
               "🔹 `.tts Hello` - Hindi Male Voice\n"
               "🔹 `.dora` - Special Doraemon GIF\n"
               "🔹 `.ping` - Bot Status Check\n\n"
               "⚡ **Powered By: @KiraNetwork**"
    )

@client.on(events.NewMessage(pattern='.dora'))
async def dora(event):
    await event.reply(
        file="https://envs.sh/Qur.jpg",
        message="**🔥 Doraemon Ne Bheja Special Gift!**"
    )

@client.on(events.NewMessage(pattern=r'\.spam (\d+) (.+)'))
async def spam(event):
    count = int(event.pattern_match.group(1))
    text = event.pattern_match.group(2)
    for _ in range(count):
        await event.respond(text)
        await asyncio.sleep(0.5)

@client.on(events.NewMessage(pattern=r'\.raid (\d+) (@?\w+)'))
async def raid(event):
    count = int(event.pattern_match.group(1))
    username = event.pattern_match.group(2)
    for _ in range(count):
        await event.respond(f"{random.choice(GAALI_DB)} {username}")

@client.on(events.NewMessage(pattern=r'\.shayari (\d+) (@?\w+)'))
async def shayari(event):
    count = int(event.pattern_match.group(1))
    username = event.pattern_match.group(2)
    for _ in range(count):
        await event.respond(f"{random.choice(SHAYARI_DB)}\n\n- {username}")

@client.on(events.NewMessage(pattern='.tts (.+)'))
async def tts(event):
    text = event.pattern_match.group(1)
    await event.reply(
        "🔊 **TTS Request**\n"
        f"🗣 **Voice:** hi-IN-MadhurNeural\n"
        f"📝 **Text:** `{text}`\n\n"
        "*(Note: Actual TTS would require Azure Cognitive Services API)*\n\n"
        "**Powered By: [Kira Network](https://t.me/KiraNetwork)**"
    )

# Start Bot
print("⚡ Kira UserBot Started!")
client.start()
client.run_until_disconnected()