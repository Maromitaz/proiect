from flask import Flask, render_template
from pyppeteer import launch
from pyppeteer.browser import Browser
import threading, random, polling, requests, asyncio, os
import settings

app = Flask(__name__, template_folder="web/templates")

@app.route("/")
def index():
    return render_template("index.html", is_web = False)

port = random.randint(6000, 7000)

def run_flask():
    app.run(
        debug = settings.IS_DEBUG,
        port = port
        )

localhost = f"http://localhost:{port}"

async def open_browser():
    browser = await launch(
        executablePath=detect_chrome(), 
        headless=False, 
        args=[f"--app={localhost}"]
    )

    # while True:
    #     pages = await browser.pages()
    #     if not pages:
    #         break
    #     await asyncio.sleep(0.5)
    await asyncio.sleep(2)

    # loop = asyncio.get_event_loop()

    polling.poll(
        lambda: (not asyncio.get_event_loop().run_until_complete(browser.pages())),
        step=0.5,
        poll_forever=True,
    )
    print("IT WORKS")
    await browser.close()

def detect_chrome():
    paths = [
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        f"{os.getenv("LOCALAPPDATA")}\\Google\\Chrome\\Application\\chrome.exe"
    ]
    for path in paths:
        if(os.path.isfile(path)):
            return path
    return ""

if(__name__ == "__main__"):
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()

#     polling.poll(
#         lambda: requests.get(localhost).status_code == 200,
#         step=0.5,
#         ignore_exceptions=(requests.exceptions.ConnectionError),
#         poll_forever=True,
#     )
    
    browser = asyncio.run(open_browser())
    