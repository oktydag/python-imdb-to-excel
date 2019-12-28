from openpyxl import *

workbook_name = "imdb_your_chooses.xlsx"

class WorksheetHandler:

    def create_worksheet(self,header1,header2,header3):
        workbook = Workbook()
        sheet = workbook.active
        sheet.append((header1, header2, header3))
        workbook.save(workbook_name)
        workbook.close()
        return workbook

    def append_in_worksheet(self, workbook, title,rating,image):
        sheet = workbook.active
        sheet.append((title, rating, image))
        workbook.save(workbook_name)
        workbook.close()