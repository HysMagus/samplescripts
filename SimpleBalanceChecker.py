#Check ERC-20 Balances Simply via Python
import requests
apiurl = 'http://api.ethplorer.io/getAddressInfo/'

print("What Address Would You Like to Check?")

address = input()

url = apiurl + address + "?apiKey=freekey"
print(url)

response = requests.get(url)
data = response.json()

print(data)