import requests
url="http://192.168.1.3:5000/predict"
data={
  "review": "This movie was awesome"
}
response=requests.post(url,json=data)
# print(response.status_code)
print(response.text)