import requests

def shortenURL():
    url = input("URL to shorten: ")

    payload = {
        "url": url
    }
    
    r = requests.post('https://cleanuri.com/api/v1/shorten', data=payload)
    if "error" in r.json(): 
        print("Invalid URl. Make sure that URL includes 'https://'")
        print("Error: ")
        print(r.json())
    else:
        print("Result URL:")
        print(r.json()["result_url"])

while True:
    shortenURL()