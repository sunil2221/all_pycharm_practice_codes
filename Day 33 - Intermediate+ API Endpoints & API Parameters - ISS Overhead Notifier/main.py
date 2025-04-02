import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# # if response.status_code == 404:
# #     raise Exception("you screwed up")
# # elif response.status_code == 300:
# #     raise Exception("go away")
#
# response.raise_for_status()
# data = response.json()['iss_position']['latitude']
# data1 = response.json()['iss_position']['longitude']
# print(data)
# print(data1)

parameters = {
    "lat":
    "lng":
}

response = requests.get(url='https://api.sunrise-sunset.org/json')
response.raise_for_status()
print(response)