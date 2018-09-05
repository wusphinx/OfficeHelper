import xlrd
import xlwt

class SuffixError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class XlsHelper(object):
    XLS_SUFFIX = ['xls', 'xlsx']

    def __init__(self, file_path):
        self.file_path = file_path
        self.check_file_suffix()

    def check_file_suffix(self):
        if len(self.file_path.rsplit("."))<=1:
            raise SuffixError("xls")
        if self.file_path.rsplit(".")[-1] not in self.XLS_SUFFIX:
            raise SuffixError("xls")

    def write(self, field_name_list, data_list):
        assert len(field_name_list)>0 and len(data_list) == len(field_name_list) 
        
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('sheet 1')
        for index, item in enumerate(field_name_list):
            sheet.write(0, index, item)
        
        row_num = 1
        for row_data in data_list:
            assert len(row_data) <= len(field_name_list)
            for col_num, item in enumerate(row_data):
                sheet.write(row_num, col_num, item)
            row_num += 1
        wbk.save(self.file_path)

