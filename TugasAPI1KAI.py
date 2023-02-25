import requests
url = 'https://api-partner.krl.co.id/krlweb/v1/schedule' 
query = {"stationid":'KPB',"timefrom":'05:00',"timeto":'08:00'}
response = requests.get(url,query)

data=response.json()['data']
for i in data:
    if i['dest'] == 'BEKASI':
        print(i['time_est'],"-",i['dest_time'],"-",i['route_name'])