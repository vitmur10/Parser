import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0"
    }
    r = requests.get(url=url, headers=headers, )

    with open("index.html", "w") as f:
        f.write(r.text)

    soup = BeautifulSoup(r.text, "lxml")
    shortstory_line = soup.find_all("div", "full")
    for film_url in shortstory_line:
        film_url = film_url.find('a').get("href")
        print(film_url)


def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        driver = webdriver.Chrome(
            executable_path=r"E:\Парсер\chromedriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)

        with open('index_selenium.html', 'w') as f:
            f.write(driver.page_source)
    except Exception as ex:
        print(ex)


def main():
    get_data_with_selenium(f"https://filmix.ac")


if __name__ == '__main__':
    main()
