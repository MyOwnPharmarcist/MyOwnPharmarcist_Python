import pandas as pd
import csv

# 입력 및 출력 파일 경로 설정
input_excel = 'C:/Users/COMPUTER/Desktop/drug_product_test/drug_products_excel_final.xlsx'
output_csv = 'C:/Users/COMPUTER/Desktop/drug_product_test/drug_products_final_csv_output.csv'

# 엑셀 파일 읽기
df = pd.read_excel(input_excel, engine='openpyxl')

# 데이터 전처리 함수
def process_cell(cell):
    if isinstance(cell, str):
        # 불필요한 \ 제거
        cell = cell.replace('\\', '')
        # 콤마나 줄바꿈이 있는 경우는 따옴표가 자동으로 붙으므로, 직접 처리할 필요 없음
        if ',' in cell or '\n' in cell:
            return cell
        else:
            # 콤마와 줄바꿈이 없는 경우 따옴표 추가
            return f'{cell}'
    return cell

# 각 셀의 값 처리
df_processed = df.applymap(process_cell)

# CSV 파일로 저장 (헤더 없이, quoting을 사용하여 자동으로 따옴표 처리)
df_processed.to_csv(output_csv, index=False, header=False, quoting=csv.QUOTE_MINIMAL, encoding='utf-8')

print(f'Processing complete. Check the output file: {output_csv}')