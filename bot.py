
import os
import json
import urllib.request

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        result = json.loads(response.read())

    if not result.get("ok"):
        raise RuntimeError("Telegram message failed")

    print("Telegram notification sent successfully!")

if __name__ == "__main__":
    send_message(
        "🏎️ HOT WHEELS STOCK ALERT BOT\n\n"
        "Your Telegram connection is working!\n"
        "Chennai PIN: 600030\n\n"
        "Next: Connecting shopping platforms."
    )
