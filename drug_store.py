import requests
import pandas as pd
from xml.etree import ElementTree as ET

data_info = []

# API URL and parameters
url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown'
params = {
    'serviceKey': 'Iqq2ySFhpFFSDMfkJZzKVqhQXAvdk3RsxkOqz/PRadOd+vEIrBOyfrHTNoUH3C7q6EO2wxm4YA/FWyRMzdZhqg==',
    'pageNo': '1',
    'numOfRows': '24497'
}

response = requests.get(url, params=params)
content = response.content.decode('utf-8')

# XML content 파싱
root = ET.fromstring(content) 

def extract_values(root):
    items = root.findall('.//item') 
    
    for item in items:
        data = {
            'dutyAddr': item.find('dutyAddr').text if item.find('dutyAddr') is not None else "",
            'dutyName': item.find('dutyName').text if item.find('dutyName') is not None else "",
            'dutyTel1': item.find('dutyTel1').text if item.find('dutyTel1') is not None else "",
            'dutyTime1c': item.find('dutyTime1c').text if item.find('dutyTime1c') is not None else "",
            'dutyTime1s': item.find('dutyTime1s').text if item.find('dutyTime1s') is not None else "",
            'dutyTime2c': item.find('dutyTime2c').text if item.find('dutyTime2c') is not None else "",
            'dutyTime2s': item.find('dutyTime2s').text if item.find('dutyTime2s') is not None else "",
            'dutyTime3c': item.find('dutyTime3c').text if item.find('dutyTime3c') is not None else "",
            'dutyTime3s': item.find('dutyTime3s').text if item.find('dutyTime3s') is not None else "",
            'dutyTime4c': item.find('dutyTime4c').text if item.find('dutyTime4c') is not None else "",
            'dutyTime4s': item.find('dutyTime4s').text if item.find('dutyTime4s') is not None else "",
            'dutyTime5c': item.find('dutyTime5c').text if item.find('dutyTime5c') is not None else "",
            'dutyTime5s': item.find('dutyTime5s').text if item.find('dutyTime5s') is not None else "",
            'dutyTime6c': item.find('dutyTime6c').text if item.find('dutyTime6c') is not None else "",
            'dutyTime6s': item.find('dutyTime6s').text if item.find('dutyTime6s') is not None else "",
            'dutyTime7c': item.find('dutyTime7c').text if item.find('dutyTime7c') is not None else "",
            'dutyTime7s': item.find('dutyTime7s').text if item.find('dutyTime7s') is not None else "",
            'dutyTime8c': item.find('dutyTime8c').text if item.find('dutyTime8c') is not None else "",
            'dutyTime8s': item.find('dutyTime8s').text if item.find('dutyTime8s') is not None else "",
            'hpid': item.find('hpid').text if item.find('hpid') is not None else "",
            'wgs84Lat': item.find('wgs84Lat').text if item.find('wgs84Lat') is not None else "",
            'wgs84Lon': item.find('wgs84Lon').text if item.find('wgs84Lon') is not None else ""
        }
        data_info.append(data)

extract_values(root)

df = pd.DataFrame(data_info)
output_file = 'D:/drug_stores.xlsx' 
df.to_excel(output_file, index=False)

print(f'Data has been saved to {output_file}')
