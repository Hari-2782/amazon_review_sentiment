from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_reviews_from_ca(pages=5):
    reviews = []

    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        for page in range(1, pages + 1):
            url = f"https://www.consumeraffairs.com/online/amazon.html?page={page}#scroll_to_reviews=true"
            driver.get(url)
            time.sleep(3)  # Let JS load

            soup = BeautifulSoup(driver.page_source, "html.parser")
            review_blocks = soup.find_all("div", class_="rvw__sc-1p7pmlv-0")

            for block in review_blocks:
                p = block.find("p")
                if p:
                    review_text = p.get_text(strip=True)
                    reviews.append(review_text)

            print(f"Page {page} scraped, total reviews so far: {len(reviews)}")
            time.sleep(1)

    finally:
        driver.quit()

    df = pd.DataFrame(reviews, columns=["review"])
    df.to_csv("ca_reviews.csv", index=False)
    print(f"Scraped {len(df)} reviews from ConsumerAffairs.")
    return df

if __name__ == "__main__":
    get_reviews_from_ca(pages=5)
