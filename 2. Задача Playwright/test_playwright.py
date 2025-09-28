import pytest
from playwright.sync_api import sync_playwright

URL = "https://playwright.dev/"
EXPECTED_TITLE = "Playwright: Fast and reliable end-to-end testing for modern web apps"

# Тестовая функция, параметризованная браузерами
@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
def test_page_title(browser_name):
    with sync_playwright() as p:
        # Запуск выбранного браузера
        browser = getattr(p, browser_name).launch()
        page = browser.new_page()
        page.goto(URL)
        # Проверка заголовка
        title = page.title()
        assert title == EXPECTED_TITLE
        browser.close()