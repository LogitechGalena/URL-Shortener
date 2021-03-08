# URL-Shortener
A short script to shorten URLs using requests alone.

## How to Install:

Open up the command prompt and navigate to the folder in which URLShortener.py is located.
Run the following in the command prompt:

```
pip install -r requirements.txt
```

This reads `requirements.txt` and installs all the libraries listed so you don't have to do it all manually.
After this type in:

```
python URLShortener.py
```
You're all set! Go crazy.

## Usage:

Unfortunately, you can't usually use any link and use the script. It has to be fully formatted as such:

```
http://www.example.com/
```
Something important: Most links, when copied, don't include the `www`. However, this is important as the API used only takes full, complete URLs. If you get an error, this is most likely the case.

![CLI Image](https://github.com/LogitechGalena/URL-Shortener/blob/main/CLI.png)
