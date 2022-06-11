from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    page.fill("input[name='q']", 'mercado livre')
    #page.wait_for_timeout(3000)
    page.click("input[name='btnK']")
    page.wait_for_timeout(3000)
    page.click("h3")
    page.wait_for_timeout(3000)
    page.fill("input[name='as_word']", 'vara de pesca')
    page.wait_for_timeout(3000)
    page.click("button.nav-search-btn")
    page.wait_for_timeout(10000)
    browser.close()