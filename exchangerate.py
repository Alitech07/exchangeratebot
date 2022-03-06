import requests

from pprint import pprint as print

API_KEY = '2c2241afb9926ee04ed839b4'

currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

r = requests.get(url)
rj = r.json()
info={
  'time':rj['time_last_update_utc'],
  'conversion':rj['conversion_rate']
}

def convertation(usd):
  x = float(rj['conversion_rate'])*usd
  print(x)
  count = 0
  mas = ''
  while True:

    y = x%1000
    x = x//1000
    if count>=1:
      if len(str(int(y)))<=3:
        mas = str(int(y)).rjust(4-len(str(int(y))), "0")+' '+ mas
      else:
        mas = str(int(y))+' '+ mas
    else:
      if len(str(int(y)))<=3:
        mas += str(y).rjust((3-len(str(int(y))))+len(str(y)), "0")
      else:
        mas += str(y)

    if x//1000 == 0:
      break
  
    count+=1

  mas = str(int(x))+' '+ mas
  mas = mas.split(".")
  mas = mas[0]+'.'+mas[1][0:4]
  return mas

