import time
import requests
from plyer import notification

WEATHER_API_KEY = "62e3205580e14e2b1d120b8a2ac70e45"   # we will set this later
CITY = "Ahmednagar"

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
    data = requests.get(url, verify=False).json()
    
    if data["cod"] != 200:
        return "Weather info unavailable."
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].title()
    return f"{temp}°C — {desc}"


def show_notification(title, msg):
    notification.notify(
        title=title,
        message=msg,
        timeout=8,
        app_icon=None
    )

def daily_quote():
    url = "https://api.quotable.io/random"
    data = requests.get(url, verify=False).json()
    return data["content"]


def main():
    while True:
        weather = get_weather()
        quote = daily_quote()

        show_notification("☁️ Weather Update", weather)
        time.sleep(5)

        show_notification("💡 Daily Motivation", quote)
        time.sleep(5)

        show_notification("🔔 Reminder", "Stay focused and keep building projects!")
        time.sleep(3600)  # update every hour

if __name__ == "__main__":
    show_notification("AI Notifier", "Service has started running in background.")
    main()
