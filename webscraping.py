import requests
from bs4 import BeautifulSoup


def download_website(url, statusCode):
    response = requests.get(url)
    if response.status_code == statusCode:
        soup = BeautifulSoup(response.content, 'html.parser')
        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))
        # return str(soup)
    else:
        print(
            f"Failed to download website. Status code: {response.status_code}")


if __name__ == '__main__':
  download_website("https://",200)
