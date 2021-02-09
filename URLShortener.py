import requests
from colorama import init 
from termcolor import colored 

init()

def shortenURL():
    url = input("URL to shorten: ")
    
    r = requests.post('https://cleanuri.com/api/v1/shorten', data={"url":url})
    if "error" in r.json(): 
        print("Invalid URL. Make sure that URL includes 'https://'")
        print("Error: ")
        print(r.json())
    else:
        print(colored("Result URL:", 'green'))
        print(colored(r.json()["result_url"], 'yellow'))

while True:
    shortenURL()
