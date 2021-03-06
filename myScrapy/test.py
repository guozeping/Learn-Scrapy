import requests
from requests.exceptions import RequestException
headers = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/board/4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


# 爬取网页源代码
def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print(RequestException)
        return None


def main():
    url = "https://maoyan.com"
    html = get_one_page(url, headers)
    print(html)
    print(html.capitalize())
    print(html.center())


if __name__ == '__main__':
    main()
