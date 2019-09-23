import requests

session = requests.Session()
response = session.get('https://stackoverflow.com/questions/45086383/python-requests-403-forbidden-despite-setting-user-agent-headers', headers={'User-Agent': 'Mozilla/5.0'})

print(response.status_code)  
print(response.text)  
print(response.links)

