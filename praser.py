import requests
def text():
    joker = requests.get('https://icanhazdadjoke.com/slack').json()
    jk = joker["attachments"][0]
    return jk["text"]
if __name__ == "__main__":
    print(text())
