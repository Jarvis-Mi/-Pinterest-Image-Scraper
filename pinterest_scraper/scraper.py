# pinterest_scraper/scraper.py
from playwright.sync_api import sync_playwright
import time
import random

def auto_pinterest_image_download(url, num_images=10, scroll_attempts_limit=250):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # You can give headless as an input argument here
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url, timeout=0)
            page.wait_for_selector("img", timeout=60000)
        except Exception as e:
            print(f"Error Loading Page: {e}")
            browser.close()
            return []

        img_urls = set()
        scroll_attempts = 0

        while len(img_urls) < num_images and scroll_attempts < scroll_attempts_limit:
            page.wait_for_selector("img", timeout=60000)
            img_elements = page.query_selector_all("img")
            for img in img_elements:
                src = img.get_attribute("src")
                if src and src.startswith("http"):
                    img_urls.add(src)
                if len(img_urls) >= num_images:
                    break
            
            # Scroll the page
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            print(f"Scrolling: {scroll_attempts}", end="\r")
            t = random.randint(4, 8)
            time.sleep(t)
            scroll_attempts += 1

        browser.close()
        return list(img_urls)[:num_images]
