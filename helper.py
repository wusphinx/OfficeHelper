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

    def check_file_suffix(self):
        if len(self.file_path.rsplit("."))<=1:
            raise SuffixError("xls")
        if self.file_path.rsplit(".")[-1] not in XLS_SUFFIX:
            raise SuffixError("xls")

