import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'START_DATE*','END_DATE*','CATEGORY*','STOP*','MILES*','PURPOSE*'})

print(r.json())
