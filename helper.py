import xlrd
import xlwt

class SuffixError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class XlsHelper(object):
    XLS_SUFFIX = ['xls', 'xlsx']
    MAX_ROW = 65536

    def __init__(self, file_path):
        self.file_path = file_path
        self.check_file_suffix()

    def check_file_suffix(self):
        if len(self.file_path.rsplit(".")) <= 1:
            raise SuffixError("xls")
        if self.file_path.rsplit(".")[-1] not in self.XLS_SUFFIX:
            raise SuffixError("xls")

    def write(self, field_name_list, data_list):
        assert len(field_name_list)>0 and len(data_list) > 0 

        wbk = xlwt.Workbook()
        step = self.MAX_ROW-1
        for i in range(0,len(data_list), step):
            sheet_name = 'sheet %d'%(i/step + 1)
            sheet = wbk.add_sheet(sheet_name)

            for index, item in enumerate(field_name_list):
                sheet.write(0, index, item)
            
            for index, row_data in enumerate(data_list[i:i+step]):
                assert len(row_data) <= len(field_name_list)
                for col_num, item in enumerate(row_data):
                    sheet.write(index+1, col_num, item)
        wbk.save(self.file_path)
    
    def read(self, sheet_index, row_start, row_end, col_start, col_end):
        """
        start from 0
        """
        assert row_start >=0 and row_start <= row_end
        assert col_start >=0 and col_start <= col_end

        xls = xlrd.open_workbook(self.file_path)
        ss = xls.sheets()
        assert len(ss) - 1 >= sheet_index
        sheet = ss[sheet_index]

        assert col_end <= sheet.ncols - 1 
        assert row_end <= sheet.nrows - 1

        data = list()
        for row_num in range(row_start, row_end):
            row_data = list()
            for col_num in range(col_start, col_end):
                row_data.append(sheet.row_values(row_num)[col_num])
            data.append(row_data)
        
        return data
