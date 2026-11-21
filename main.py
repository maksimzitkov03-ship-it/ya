import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange")
list_1 = []

response_text = response.text
response_parse = response_text.split("<currency>")

for element in response_parse:
    if "USD" in element or "EUR" in element:
        for element2 in element.split("<rate>"):
            if "</rate>" in element2:
                rate = element2.split("</rate>")[0].strip()
                if "<cc>USD</cc>" in element:
                    list_1.append(f"USD: {rate}")
                if "<cc>EUR</cc>" in element:
                    list_1.append(f"EUR: {rate}")

print("курсы с сайта НБУ:")
print(list_1)
