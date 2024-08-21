import pandas as pd

# 엑셀 파일 경로
input_file = 'C:/Users/COMPUTER/Desktop/final_file/drug_products_final.csv'
output_file = 'C:/Users/COMPUTER/Desktop/drug_product_test/drug_product_final.csv'

# CSV 파일 읽기
df = pd.read_csv(input_file, header=None)  # header=None을 사용하여 헤더를 읽지 않음

print("CSV 파일이 성공적으로 읽혔습니다.")
print(f"파일 경로: {input_file}")
print("원본 데이터프레임의 일부:")
print(df.head())  # 데이터프레임의 상위 5개 행을 출력

def add_quotes(value):
    if pd.isna(value):
        return '\"\"'
    value_str = str(value)
    if value_str.startswith('\"') and value_str.endswith('\"'):
        return value_str
    return f'\"{value_str}\"'

# 모든 칼럼의 데이터 값을 확인하여 적절히 수정
df = df.applymap(add_quotes)

print("\n모든 데이터가 적절히 '\"칼럼값\"' 형태로 변경되었습니다.")
print("변경된 데이터프레임의 일부:")
print(df.head())  # 변경된 데이터프레임의 상위 5개 행을 출력

# 수정된 데이터프레임을 새로운 CSV 파일로 저장 (헤더 없음)
df.to_csv(output_file, index=False, header=False, encoding='utf-8-sig')

print(f"\n변경된 데이터를 '{output_file}'로 저장했습니다.")
print(f"저장된 파일의 경로: {output_file}")