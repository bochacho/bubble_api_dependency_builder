import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os

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
    all_panels = panels.all()

    for item in all_panels:
        item.get_by_text('expand').first.click()
        item.get_by_text('expand all calls').click()
        
        # ===============================================================
        # Using Btns
        # init_locators = item.get_by_text('Manually enter API response')
        # init_buttons = init_locators.all()

        # for btn in init_buttons:
        #     btn.click()
        #     # Wait for the animation to complete
        #     popup = page.locator('div.modal-popup.apiconnector-json-popup')
        #     popup.locator('div.btn-save').click()

        #     break
        # ===============================================================

        subPanelSelector = 'div.sub-call-panel'
        subPanels = item.locator(subPanelSelector).all()
        
        for subPanel in subPanels:
            init_btn = subPanel.get_by_text('Manually enter API response')
            init_btn.click()
            popup = page.locator('div.modal-popup.apiconnector-json-popup')
            popup.locator('div.btn-save').click()
            
            snapshot = page.content()
            with open('src/content.html', 'w', encoding='utf-8') as file:
                file.write(snapshot)
                
            # popup = page.locator('div.modal-popup.apiconnector-json-popup')
            # fieldDivs = popup.locator('div.field-zone.sub').all()
            # for field in fieldDivs:
            #     fieldName = field.locator('div.field-name').text_context()
            #     print(fieldName)
            #     break

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

