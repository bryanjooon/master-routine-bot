import os
import datetime
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

MINI_APP_URL = "https://bryanjooon.github.io/master-routine-bot/"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "🚀 Open Routine & PR Tracker", "web_app": {"url": MINI_APP_URL}}]
            ]
        }
    }
    res = requests.post(url, json=payload)
    print("Telegram Response:", res.json())

def check_schedule():
    # GMT+5 Timezone adjustment for Tashkent
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
    day_name = now.strftime("%A")
    
    if day_name == "Monday":
        msg = (
            "📅 *MONDAY — ACTIVE RECOVERY DAY*\n\n"
            "06:00 AM: Drive Home ➔ Sleep by 08:00 AM\n"
            "02:30 PM: Wake up ➔ Voice Reset ➔ Power Juice\n"
            "02:40 PM: Pray Dhuhr ➔ 10 Chin Tucks\n"
            "02:50 PM: 1.5 Hours Qur'an Study\n"
            "04:15 PM: Whitening Strips (30m) ➔ Minoxidil\n"
            "05:00 PM: Swim Session (Light Backstroke + Mobility)"
        )
    elif day_name == "Tuesday":
        msg = (
            "🏋️ *TUESDAY — GYM DAY 1: POWER & BOXING*\n\n"
            "06:30 AM – 07:30 AM:\n"
            "• Legs: Heavy Trap Bar Deadlift (3x5) + Box Jumps\n"
            "• Chest: Incline DB Press (3x8) + Flyes\n"
            "• Back: Chest-Supported DB Row (3x8) + Lat Pulldown\n"
            "• Shoulders: DB OHP (3x8) + Lateral Raises\n"
            "• Arms: DB Curls + Tricep Extensions\n"
            "07:30 AM: 3 Rounds Boxing Sparring\n"
            "08:15 AM: Post-Workout Meal (300g Tvorog + Banana + Smetana)\n\n"
            "05:15 PM PRE-SHIFT MEAL: 4 Eggs + Bread + PB Banana ➔ Nest One"
        )
    elif day_name == "Wednesday":
        msg = (
            "📅 *WEDNESDAY — ACTIVE RECOVERY DAY*\n\n"
            "02:30 PM: Wake up ➔ Voice Reset ➔ Power Juice ➔ Dhuhr\n"
            "02:50 PM: 1.5 Hours Qur'an Study\n"
            "04:15 PM: Whitening Strips ➔ Minoxidil\n"
            "05:15 PM PRE-SHIFT MEAL: 4 Fried Eggs + Bread + 2 Bananas w/ PB\n"
            "06:00 PM – 06:00 AM: Work Shift at Nest One"
        )
    elif day_name == "Thursday":
        msg = (
            "🏋️ *THURSDAY — GYM DAY 2: ATHLETIC & WRESTLING*\n\n"
            "06:30 AM – 07:30 AM:\n"
            "• Legs: Barbell Jump Squats (4x5) + Single-Leg RDL\n"
            "• Chest: Weighted Dips (3x8) + Push-Offs\n"
            "• Back: Weighted Pull-Ups (3x6-8) + DB Single Arm Row\n"
            "• Shoulders: Push Press (3x8) + Rear Delt Flyes\n"
            "• Arms: Hammer Curls + Tricep Pushdowns\n"
            "07:30 AM: 3 Rounds Wrestling Entries\n"
            "08:15 AM: Post-Workout Meal (300g Tvorog + Banana + Honey)\n\n"
            "05:15 PM PRE-SHIFT MEAL: 4 Eggs + Bread + PB Banana"
        )
    elif day_name == "Friday":
        msg = (
            "🕌 *FRIDAY — JUMU'AH DAY*\n\n"
            "06:00 AM: Drive Home (Surah Al-Kahf) ➔ Sleep\n"
            "12:00 PM: Wake ➔ Ghusl ➔ Miswak/Attar ➔ Jumu'ah\n"
            "05:00 PM: Power Juice ➔ Asr ➔ Dua Window\n"
            "05:15 PM: Whitening Strips + Minoxidil\n"
            "05:30 PM PRE-SHIFT MEAL: 4 Eggs + Bread + PB ➔ Nest One"
        )
    elif day_name == "Saturday":
        msg = (
            "🏋️ *SATURDAY — GYM DAY 3: HYPERTROPHY & KICKBOXING*\n\n"
            "06:30 AM – 07:30 AM:\n"
            "• Legs: DB Walking Lunges (3x10) + Calf Raises\n"
            "• Chest: Flat DB Press (3x8) + Cable Crossovers\n"
            "• Back: Seated Cable Row (3x10) + Lat Pulldowns\n"
            "• Shoulders: Cable Lateral Raises + Face Pulls\n"
            "• Arms: Preacher Curls + Overhead DB Extension\n"
            "07:30 AM: 3 Rounds Kickboxing Flow\n"
            "08:15 AM: Post-Workout Meal (300g Tvorog + Banana + Smetana)\n\n"
            "09:30 PM WORK MEAL: 2 Cans Tuna + 4 Hard-Boiled Eggs + Bread"
        )
    else: # Sunday
        msg = (
            "⚽ *SUNDAY — FOOTBALL DAY*\n\n"
            "06:00 AM: Drive to Football Match with Friends\n"
            "08:00 AM: Drive Home ➔ Sleep\n"
            "02:30 PM: Wake up ➔ Voice Reset ➔ Power Juice ➔ Dhuhr\n"
            "02:50 PM: 1.5 Hours Qur'an Study\n"
            "05:15 PM PRE-SHIFT MEAL: 4 Eggs + Bread + PB Banana\n"
            "09:30 PM WORK MEAL: 250g Tvorog + Walnuts + 2 Bananas + Milk"
        )

    send_telegram(msg)

if __name__ == "__main__":
    check_schedule()
