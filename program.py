import requests, bs4


def print_header():
    print("-"*25)
    print("Weather App".center(25))
    print("-"*25)


def get_html(zip_code):
    url = f'http://www.wunderground.com/weather-forecast/{zip_code}'
    response = requests.get(url)
    return response.text


def get_weather(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text().strip()
    condition = soup.find(class_='condition-icon').get_text().strip()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text().strip()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text().strip()

    print(loc + '\n' + condition +'\n' + temp + scale)


def main():
    print_header()
    zip_code = input('What zipcode do you want the weather for? (98034) > ')
    html = get_html(zip_code)
    get_weather(html)
    # TODO: parse html
    # TODO: display for the forecast



if __name__ == '__main__':
    main()