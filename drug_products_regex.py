import pandas as pd
import re

def clean_text(text):
    # HTML 태그 제거
    text = re.sub(r'<[^>]*>', '', text)
    # HTML 엔티티 제거
    text = re.sub(r'&[^;]+;', '', text)
    return text

# 엑셀 파일 경로
input_file = 'C:/Users/COMPUTER/Desktop/final_file/drug_products_excel.xlsx'
output_file = 'C:/Users/COMPUTER/Desktop/final_file/drug_product_final.csv'

# 엑셀 파일 읽기
df = pd.read_excel(input_file)

print("엑셀 파일이 성공적으로 읽혔습니다.")
print(f"파일 경로: {input_file}")
print("원본 데이터프레임의 일부:")
print(df.head())  # 데이터프레임의 상위 5개 행을 출력

# 각 칼럼에서 텍스트 정제
for col in df.columns:
    if df[col].dtype == 'object':  # 문자열 데이터만 처리
        print(f"\n정제 중: {col} 칼럼")
        df[col] = df[col].apply(lambda x: clean_text(x) if isinstance(x, str) else x)
        print("정제된 데이터 샘플:")
        print(df[col].head())  # 정제된 칼럼의 상위 5개 행을 출력

# 수정된 데이터프레임을 새로운 CSV 파일로 저장 (헤더 없음)
df.to_csv(output_file, index=False, header=False, encoding='utf-8-sig')

print(f"\n정제된 데이터를 '{output_file}'로 저장했습니다.")
print(f"저장된 파일의 경로: {output_file}")
