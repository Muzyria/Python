from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        **p.devices['iPhone 11 Pro Max']  # Эмуляция устройства iPhone 11 Pro Max
    )
    page = context.new_page()
    page.goto('https://google.com')

    # Создание скриншота страницы
    page.screenshot(path='screenshot.png')

    browser.close()
