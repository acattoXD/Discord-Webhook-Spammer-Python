import requests
import threading
import multiprocessing
import json
import random
import string
import os

config: dict = json.load(open("config.json"))


def start():
    while True:
        try:
            s = requests.Session()
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "sec-ch-ua": '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "sec-gpc": "1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            }
            proxy: bool = config.get("proxy")
            proxytype: str = config.get("proxytype")
            proxyurl: str = config.get("proxyurl")
            if proxy == "true" or proxy == "True":
                proxy = True
            else:
                proxy = False
            
            if proxyurl == "" and proxy:
                print("You're running proxyless, please turn 'Proxy' off in config.json and rerun.")

            if proxy and proxyurl != "":
                s.proxies = {"all": f"{proxytype}://{proxyurl}"}
            else:
                print("You're running proxyless, if you wish to use a proxy turn 'proxy' on and enter a proxy url and a method. Continuing proxyless.")
                s.proxies = None

            url = ""

            message: str = config.get("message")
            embed: bool = config.get("embed")
            username: str = config.get("username")
            description: str = config.get("description")
            title: str = config.get("title")
            color: str = config.get("color")
            footer: str = config.get("footer")
            ping: bool = config.get("ping")
            weird: bool = config.get("weird")

            if embed == "true" or embed == "True":
                embed = True
            else:
                embed = False

            if weird == "true" or weird == "True":
                weird = True
            else:
                weird = False

            if ping == "true" or ping == "True":
                ping = True
            else:
                ping = False

            if not embed:
                data = {"content": message, "username": username}

            if embed:
                data = {"username": username}
                data["embeds"] = [
                    {
                        "description": description,
                        "title": title,
                        "color": color,
                        "footer": {"text": footer},
                    }
                ]

            if ping:
                data = {"content": "@everyone" + f"\n{message}", "username": username}

            if embed and ping:
                data = {"content": "@everyone", "username": username}
                data["embeds"] = [
                    {
                        "description": description,
                        "title": title,
                        "color": color,
                        "footer": {"text": footer},
                    }
                ]

            weirdmaker = "".join(
                random.choice(string.ascii_letters + string.digits + string.punctuation)
                for _ in range(50)
            )

            if weird and embed and ping:
                data = {"content": "@everyone", "username": username}
                data["embeds"] = [
                    {
                        "description": description + f"\n{weirdmaker}",
                        "title": title,
                        "color": color,
                        "footer": {"text": footer},
                    }
                ]

            if weird == True:
                data = {"content": message + f"\n{weirdmaker}", "username": username}

            if weird and embed:
                data = {"username": username}
                data["embeds"] = [
                    {
                        "description": description + f"\n{weirdmaker}",
                        "title": title,
                        "color": color,
                        "footer": {"text": footer},
                    }
                ]

            result = s.post(url, json=data)
            embedtrue = embed
            if result.ok:
                print(f"Successfully sent a message, Embed message: {embedtrue}")
            else:
                if result.status_code == 429:
                    print(
                        f"Failed to send a message, the webhook is ratelimited. Code: {result.status_code}"
                    )
                else:
                    print(f"Unknown error. Code: {result.status_code}")
        except Exception:
            pass


threadamount: int = config.get("threads")
processamount: int = config.get("processes")


def threadingstart():
    for _ in range(int(threadamount)):
        threading.Thread(target=start).start()


if __name__ == "__main__":
    for _ in range(int(processamount)):
        multiprocessing.Process(target=threadingstart).start()
