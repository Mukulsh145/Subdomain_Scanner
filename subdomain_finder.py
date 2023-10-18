import requests

def request(url):
        try:
             return requests.get("https://" + url)
        except requests.exceptions.ConnectionError:
             pass


url = input("enter  :- ")

subdomain = requests.get("https://" + url)

with open("Enter your subdomain.txt file path here" , "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        test_url = word + "." + url
        response = request(test_url)
        if response:
             print("found url :-" + test_url)

try:
     pass 
except KeyboardInterrupt as e:
     print(f"Oops! you Interrupted")
     pass

