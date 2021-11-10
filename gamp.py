import requests as requests
import uuid


tracking_id = 'UA-212474285-1'
client_id = str(uuid.uuid4())

response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json')
currency_rate = int(response.json()[0]['rate'] * 1000)


data = {
    'v': 1,
    'tid': tracking_id,
    'cid': client_id,
    't': 'event',
    'ec': 'Currency rate',  # category
    'ea': 'Update',  # action
    'el': 'USD/UAH',  # label
    'ev': currency_rate,  # value
    'ua': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

headers = {
    'user-agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36}'
}

response = requests.post('https://www.google-analytics.com/collect', data=data, headers=headers)
print(response)
