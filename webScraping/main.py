import requests
import selectorlib
import time

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)["tours"]
    return value


def sed_email():
    print("Send email")


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")
        

def read():
    with open("data.txt", "r") as file:
       return file.read()
    

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read()
        if extracted != "No upcoming tours":
            if extracted not in content:
                sed_email()
                store(extracted)
        time.sleep(2)