import requests
data = open('request.json', 'rb').read()
key = open('apiKey.txt', 'rb').read()
response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=%s'%(key), data=data, headers={'Content-Type': 'application/json'})
print response.text
