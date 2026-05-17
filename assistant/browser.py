from playwright.sync_api import sync_playwright
import urllib.parse

play = sync_playwright().start()

browser = play.chromium.launch(
    headless=False
)

page = browser.new_page()

# =========================
# GOOGLE SEARCH
# =========================

def google_search(query):

    search_url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(query)
    )

    page.goto(search_url)

# =========================
# OPEN FIRST GOOGLE LINK
# =========================

def open_first_link():

    try:

        page.locator("h3").first.click()

        return True

    except:

        return False

# =========================
# YOUTUBE SEARCH
# =========================

def youtube_search(query):

    search_url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(query)
    )

    page.goto(search_url)

# =========================
# OPEN FIRST VIDEO
# =========================

def open_first_video():

    try:

        page.locator("#video-title").first.click()

        return True

    except:

        return False

# =========================
# VIDEO CONTROLS
# =========================

def pause_video():

    page.keyboard.press("Space")

def fullscreen_video():

    page.keyboard.press("f")

def next_video():

    page.keyboard.press("Shift+N")

# =========================
# SCROLL
# =========================

def scroll_down():

    page.mouse.wheel(0, 1000)

def scroll_up():

    page.mouse.wheel(0, -1000)