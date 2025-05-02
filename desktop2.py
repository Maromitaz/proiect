from flask import Flask, render_template
from pyppeteer import launch
from pyppeteer.browser import Browser
import threading, random, polling, requests, asyncio
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

async def get_browser_pages(browser: Browser):
    pages = await browser.pages()
    return not pages
async def open_browser():
    browser = await launch(headless=False, args=[f"--app={localhost}"])

    polling.poll(
        lambda: get_browser_pages(browser) == True,
        step=1,
        poll_forever=True,
    )

    browser.close()

# if(__name__ == "__main__"):
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()

#     polling.poll(
#         lambda: requests.get(localhost).status_code == 200,
#         step=0.5,
#         ignore_exceptions=(requests.exceptions.ConnectionError),
#         poll_forever=True,
#     )
    
    # asyncio.run(open_browser())
