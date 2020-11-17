import time

def shortenURL()
    url = input(URL to shorten )

    payload = {
        url url
    }
    
    print(url)
    r = requests.post('httpscleanuri.comapiv1shorten', data=payload)
    if error in r.json() 
        print(Invalid URl. Make sure that URL includes 'https')
        print(Error )
        print(r.json())
    else
        print(r.json())

while True
    shortenURL()