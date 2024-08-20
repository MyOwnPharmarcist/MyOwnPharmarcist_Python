import requests
import pandas as pd

# 네이버 클라우드 플랫폼에서 발급받은 API 키
CLIENT_ID = 'we7grllraz'
CLIENT_SECRET = 'RMHIpKQAa853iPxMBd3atQ4odgQWuxooTWAoNpIE'

# 주소를 위도와 경도로 변환하는 함수
def geocode_address(address):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    headers = {
        'X-NCP-APIGW-API-KEY-ID': CLIENT_ID,
        'X-NCP-APIGW-API-KEY': CLIENT_SECRET
    }
    params = {
        'query': address
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'addresses' in data and data['addresses']:
        lat = data['addresses'][0]['y']
        lon = data['addresses'][0]['x']
        return lat, lon
    else:
        return '변환 실패', '변환 실패'

# 입력 및 출력 파일 경로 설정
# input_csv = 'C:/Users/COMPUTER/Desktop/x_y_test_100.csv'
output_csv = 'C:/Users/COMPUTER/Desktop/emergency_drug_test/coordinates_converted.csv'

# CSV 파일 읽기 (적절한 인코딩 사용)
df = pd.read_csv(input_csv, encoding='ISO-8859-1', header=None)

# 주소가 1번째 칼럼에 있다고 가정
def add_coordinates(row):
    address = '전북특별자치도 전주시 덕진구 기린대로 696' # 주소가 1번째 칼럼에 있다고 가정
    latitude, longitude = geocode_address(address)
    return pd.Series([latitude, longitude])

# 좌표 변환 (3번째와 4번째 칼럼에 추가)
df[['Latitude', 'Longitude']] = df.apply(add_coordinates, axis=1)

# 기존 칼럼 + 변환된 위도와 경도 칼럼 결합
df_converted = df

# 변환된 데이터 저장 (헤더 없음, UTF-8 인코딩)
df_converted.to_csv(output_csv, index=False, header=False, encoding='utf-8-sig')

print(f'CSV 파일이 성공적으로 생성되었습니다: {output_csv}')
