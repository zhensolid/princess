from openpyxl import load_workbook

def get_excel_date():
    workbook = load_workbook("一季度.xlsx")
    worksheet = workbook["一季度汇总表"]

    data = []
    for row in worksheet.iter_rows(min_row=1):
        dict_data = {}
        dict_data["name"] = row[0].value
        dict_data["value"] = row[2].value
        data.append(dict_data)
    workbook.close()

    return data
# note 输出数据
# print(get_excel_date())

