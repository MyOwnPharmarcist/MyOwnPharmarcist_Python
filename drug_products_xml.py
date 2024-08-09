import requests
import pandas as pd
import xml.etree.ElementTree as ET

data_info = []

# API URL and parameters
url = 'http://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService05/getDrugPrdtPrmsnDtlInq04'
params = {
    'serviceKey': 'Iqq2ySFhpFFSDMfkJZzKVqhQXAvdk3RsxkOqz/PRadOd+vEIrBOyfrHTNoUH3C7q6EO2wxm4YA/FWyRMzdZhqg==',
    'pageNo': '1',  # Starting page number
    'numOfRows': '100',  # Max number of rows per page
    'type': 'xml'
}

# Function to extract values from XML
def extract_values(root):
    items = root.findall('.//item')  # Adjust the XPath based on the XML structure
    for item in items:
        ee_doc_data_str = ""
        ud_doc_data_str = ""

        ee_doc_data = item.find('EE_DOC_DATA')
        if ee_doc_data is not None:
            for para in ee_doc_data.findall(".//PARAGRAPH"):
                ee_doc_data_str += (para.text or "") + "\n"
            ee_doc_data_str = ee_doc_data_str.strip()

        ud_doc_data = item.find('UD_DOC_DATA')
        if ud_doc_data is not None:
            for para in ud_doc_data.findall(".//PARAGRAPH"):
                ud_doc_data_str += (para.text or "") + "\n"
            ud_doc_data_str = ud_doc_data_str.strip()

        data = {
            'ITEM_NAME': item.findtext('ITEM_NAME', default="").strip(),
            'ENTP_NAME': item.findtext('ENTP_NAME', default="").strip(),
            'ETC_OTC_CODE': item.findtext('ETC_OTC_CODE', default="").strip(),
            'CHART': item.findtext('CHART', default="").strip(),
            'STORAGE_METHOD': item.findtext('STORAGE_METHOD', default="").strip(),
            'VALID_TERM': item.findtext('VALID_TERM', default="").strip(),
            'INDUTY_TYPE': item.findtext('INDUTY_TYPE', default="").strip(),
            'EE_DOC_DATA': ee_doc_data_str,
            'UD_DOC_DATA': ud_doc_data_str
        }
        data_info.append(data)

# Fetch data from multiple pages
page_no = 1
total_rows = 0
max_rows = 46743  # Total number of rows to fetch

while total_rows < max_rows:
    params['pageNo'] = str(page_no)
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        content = response.content.decode('utf-8')

        # Parse XML content
        root = ET.fromstring(content)

        # Extract data from XML
        extract_values(root)

        # Update total rows count
        num_rows = len(root.findall('.//item'))
        total_rows += num_rows
        
        # Check if the number of items is less than the maximum allowed rows per page
        if num_rows < 100:
            break  # No more data to fetch

        page_no += 1  # Go to the next page

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        break

# Create DataFrame and save to Excel
df = pd.DataFrame(data_info)
output_file = 'D:/drug_products.xlsx'
df.to_excel(output_file, index=False)

print(f'Data has been saved to {output_file}')
