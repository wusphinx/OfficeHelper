import unittest
from helper import XlsHelper
from helper import SuffixError

class TestXlsHelper(unittest.TestCase):
    def test_init(self):
        pass

    def test_check_file_suffix(self):
        with self.assertRaises(SuffixError) as cm:
            XlsHelper("ok").check_file_suffix()
    def test_write(self):
        field_name_list, data_list = ['f1', "f2"], [[1,'row1'], ['row2']]
        XlsHelper("./test1.xls").write(field_name_list, data_list)

if __name__ == '__main__':
    unittest.main()