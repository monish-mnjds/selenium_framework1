import xlrd
from Library.Config import Config
from pprint import pprint

class read_excel_file:
    def read_excel(self):
        
        wb = xlrd.open_workbook(Config.workbook)
        ws = wb.sheet_by_name(Config.sheetName)
        rows = ws.get_rows()
        next(rows)
        d = {row[0].value: (row[1].value, row[2].value) for row in rows}
        pprint(d)

rx = read_excel_file()

rx.read_excel()