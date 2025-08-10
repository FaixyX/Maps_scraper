import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

#  Ask for user input 
niche = input("Enter the niche or search term (e.g., 'restaurants in California'): ").strip()
max_scrolls = input("Enter number of scrolls for more results (default 5): ").strip()
max_scrolls = int(max_scrolls) if max_scrolls.isdigit() else 5

#Chrome Options 
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)

all_businesses = []  # List to hold all business data

try:
    driver.get("https://www.google.com/maps")

    # Wait for search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchboxinput"))
    )

    # Search for niche
    search_box.clear()
    search_box.send_keys(niche)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for results to appear

    # Locate the results scroll container
    scrollable_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label*="Results for"]'))
    )

    # Scroll inside the results panel
    for _ in range(max_scrolls):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        time.sleep(2)

    # Get all business result containers
    businesses = driver.find_elements(By.CSS_SELECTOR, "div.Nv2PK")
    print(f"\nFound {len(businesses)} businesses for '{niche}':\n")

    for index, biz in enumerate(businesses, start=1):
        try:
            # Click each business to open detail view
            driver.execute_script("arguments[0].scrollIntoView(true);", biz)
            time.sleep(1)
            biz.click()
            time.sleep(3)  # wait for detail panel

            # Extract data
            try:
                name = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1.DUwDvf"))
                ).text
            except NoSuchElementException:
                name = "N/A"

            try:
                rating = driver.find_element(By.CSS_SELECTOR, "div.F7nice > span:nth-child(1) > span:nth-child(1)").text
            except NoSuchElementException:
                rating = "N/A"

            try:
                total_reviews = driver.find_element(By.CSS_SELECTOR, "span:nth-child(2) > span > span").text.replace("(", "").replace(")", "")
            except NoSuchElementException:
                total_reviews = "N/A"

            try:
                category = driver.find_element(By.CSS_SELECTOR, "button.DkEaL").text
            except NoSuchElementException:
                category = "N/A"

            try:
                address = driver.find_element(By.CSS_SELECTOR, "button[data-item-id='address']").text
            except NoSuchElementException:
                address = "N/A"

            try:
                website = driver.find_element(By.CSS_SELECTOR, "a[data-item-id='authority']").get_attribute("href")
            except NoSuchElementException:
                website = "N/A"

            try:
                phone = driver.find_element(By.CSS_SELECTOR, "button[data-item-id^='phone']").text
            except NoSuchElementException:
                phone = "N/A"

            # Click the "About" tab in the business panel
            try:
                about_tab = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@aria-label, 'About ')]"))
                )
                about_tab.click()
                time.sleep(3)  # wait for about content to load
            except Exception as e:
                print("Could not click About tab:", e)

            # Extract About details
            about_details = {}
            try:
                about_section = driver.find_element(By.CSS_SELECTOR, "div[aria-label^='About']")
                sections = about_section.find_elements(By.CSS_SELECTOR, "div.iP2t7d.fontBodyMedium")

                for section in sections:
                    heading = section.find_element(By.TAG_NAME, "h2").text
                    items = section.find_elements(By.CSS_SELECTOR, "ul.ZQ6we li span[aria-label]")
                    about_details[heading] = [item.get_attribute("aria-label") for item in items]

            except NoSuchElementException:
                about_details = {}

            # Store all data in dictionary
            business_data = {
                "name": name,
                "rating": rating,
                "total_reviews": total_reviews,
                "category": category,
                "address": address,
                "website": website,
                "phone": phone,
                "about": about_details
            }

            all_businesses.append(business_data)

# print
            print(f"{index}. {name}")

        except Exception as e:
            print(f"Error extracting business {index}: {e}")

except (TimeoutException, WebDriverException) as e:
    print("Error:", e)

finally:
    driver.quit()

# save to JSON file
with open("businesses_data.json", "w", encoding="utf-8") as f:
    json.dump(all_businesses, f, ensure_ascii=False, indent=4)

print(f"Scraped data saved to 'businesses_data.json'")