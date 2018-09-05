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
        if len(self.file_path.rsplit("."))<=1:
            raise SuffixError("xls")
        if self.file_path.rsplit(".")[-1] not in self.XLS_SUFFIX:
            raise SuffixError("xls")

    def write(self, field_name_list, data_list):
        assert len(field_name_list)>0 and len(data_list) >0 

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

