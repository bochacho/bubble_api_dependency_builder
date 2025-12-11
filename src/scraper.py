import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="src/auth.json")
    page = context.new_page()
    page.goto("https://bubble.io/page?id=autonow-95520&tab=Plugins&name=PG+INVENTORY&version=02y16&type=custom")
    page.get_by_text("Cancel", exact=True).click()

    page.locator('[data-id="apiconnector2"]').click();

    # page.locator("div").filter(has_text=re.compile(r"^API Connector$")).first.click()
    div = page.locator('[class="custom-plugin-panel apiconnector2"]');
    # div.locator('.apps-wrapper')  

    
    panelSelector = 'div.custom-plugin-panel.apiconnector2 div.call-panel.bubble-ui.green-box';
    panels = page.locator(panelSelector)
    all_panels = panels.all();

    for item in all_panels:
        item.get_by_text('expand').first.click()
        item.get_by_text('expand all calls').click()
        
        init_locators = item.get_by_text('Manually enter API response')
        init_buttons = init_locators.all()

        for btn in init_buttons:
            btn.click()
            # Wait for the animation to complete
            popup = page.locator('div.modal-popup.apiconnector-json-popup')
            popup.locator('div.btn-save').click()
            # popup.wait_for(state="visible")

            # # Wait for the animation class to be removed
            # page.locator('div.modal-popup.apiconnector-json-popup.velocity-animating').wait_for(state="hidden", timeout=2000)

            # page.locator('div.btn-save').click(force=True)
            break
        break


    time.sleep(10)

    # while (await page.locator(panelSelector).count() > 0) {
    # const firstPanel = page.locator(panelSelector).first();
    # await firstPanel.click();
    # // Wait for DOM to update if needed
    # await page.waitForTimeout(500);
    # }
    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)

