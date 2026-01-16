import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import time
import random

# Target URL (Mobile version for better access)
BASE_URL = "https://m.bizbuysell.com/massachusetts-established-businesses-for-sale/"

async def run():
    async with async_playwright() as p:
        # Launch browser - Mobile emulation
        # using chrome/chromium often works well, sometimes webkit is less detected.
        # We will try chromium with a device scale header or just standard mobile emulation.
        iphone_13 = p.devices['iPhone 13']
        # Update user agent in the dictionary directly to avoid argument conflict
        iphone_13['user_agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
        
        # Run in headful mode to avoid bot detection
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(**iphone_13)
        
        page = await context.new_page()
        
        # Navigate to initial URL
        current_url = BASE_URL
        page_num = 1
        all_businesses = []

        while True:
            print(f"Navigating to list page: {current_url}")
            await page.goto(current_url, timeout=60000)
            
            # Handle potential "Bulletin" popup or "Get advice" modal
            try:
                # Wait a bit for popup
                await asyncio.sleep(2)
                popup_close = await page.query_selector("text='No, thanks'")
                if popup_close:
                     print("Dismissing popup...")
                     await popup_close.click()
            except Exception as e:
                pass

            print(f"Scraping list page {page_num}...")
            
            # Wait for list to load
            try:
                await page.wait_for_selector('a.diamond, a.showcase, a.basic', state='attached', timeout=30000)
            except Exception as e:
                print("List items not found (Access Denied?).")
                await page.screenshot(path=f"debug_error_page_{page_num}.png")
                break
            
            # Extract next page URL *before* navigating away
            next_btn = await page.query_selector('a.pagerNext')
            next_page_url = None
            if next_btn:
                href = await next_btn.get_attribute('href')
                if href:
                     if href.startswith('/'):
                        next_page_url = f"https://m.bizbuysell.com{href}"
                     else:
                        next_page_url = href
            
            # Get all listing links
            listings_handle = await page.query_selector_all('a.diamond, a.showcase, a.basic')
            listing_urls = []
            for item in listings_handle:
                href = await item.get_attribute('href')
                if href:
                    if href.startswith('/'):
                        href = f"https://m.bizbuysell.com{href}"
                    listing_urls.append(href)
            
            print(f"Found {len(listing_urls)} businesses on page {page_num}")
            
            # Visit each business detail page sequentially in the SAME tab
            for url in listing_urls:
                print(f"  Scraping details for: {url}")
                try:
                    await page.goto(url, timeout=60000)
                    
                    # Random sleep to mimic human reading
                    await asyncio.sleep(random.uniform(2.0, 5.0))
                    
                    # Extract Data
                    data = {}
                    data['Link'] = url
                    
                    # Title
                    try:
                        data['Title'] = await page.inner_text('h1', timeout=5000)
                    except:
                        data['Title'] = 'N/A'
                    
                    # Check for access denied on detail page
                    if "Access Denied" in data['Title']:
                        print("    ACCESS DENIED on detail page.")
                        continue

                    # Financials
                    financials_labels = ["Asking Price", "Cash Flow", "Gross Revenue", "EBITDA"]
                    for label in financials_labels:
                        try:
                            val = await page.evaluate(f'''(label) => {{
                                const b = Array.from(document.querySelectorAll('.lgFinancials b')).find(el => el.textContent.includes(label));
                                return b ? b.parentElement.textContent.replace(label, '').replace(':', '').trim() : 'N/A';
                            }}''', label)
                            data[label] = val
                        except:
                            data[label] = 'N/A'
                            
                    # Details
                    details_labels = ["Location", "Established", "FF&E", "Inventory", "Real Estate", "Employees"]
                    for label in details_labels:
                         try:
                            val = await page.evaluate(f'''(label) => {{
                                const dt = Array.from(document.querySelectorAll('dl.listingProfile_details dt')).find(el => el.textContent.includes(label));
                                const dd = dt ? dt.nextElementSibling : null;
                                return dd ? dd.textContent.trim() : 'N/A';
                            }}''', label)
                            data[label] = val
                         except:
                             data[label] = 'N/A'
                    
                    # Description
                    try:
                        data['Description'] = await page.inner_text('.businessDescription', timeout=5000)
                    except:
                        data['Description'] = 'N/A'
                        
                    all_businesses.append(data)
                    
                except Exception as e:
                    print(f"Error scraping {url}: {e}")
            
            # Prepare for next page
            if next_page_url:
                print("Moving to next list page...")
                current_url = next_page_url
                page_num += 1
                await asyncio.sleep(random.uniform(2.0, 4.0))
            else:
                print("No more pages found.")
                break
                
        await browser.close()
        
        # Save Data
        df = pd.DataFrame(all_businesses)
        df.to_csv('bizbuysell_data.csv', index=False)
        print(f"Done! Scraped {len(all_businesses)} businesses. Saved to bizbuysell_data.csv")

if __name__ == '__main__':
    asyncio.run(run())
