import xlrd


class ReadExcel:

    @staticmethod
    def get_data():

        mydata = []
        workbook = xlrd.open_workbook("C://Users//subbu//Desktop//data.xlsx")
        sheet = workbook.sheet_by_index(0)
        for row_index in range(0,sheet.nrows):
            mydata.append(sheet.row_values(row_index, 0, sheet.ncols))
            # myrows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
            print("My Data::",mydata)
        return mydata



