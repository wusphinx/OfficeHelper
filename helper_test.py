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
        data_list = []
        for i in range(65536*2):
            data_list.append([1,'row%d'%(i+1)])
        field_name_list = ['f1', "人生苦短，我用python"]
        XlsHelper("./test1.xls").write(field_name_list, data_list)

if __name__ == '__main__':
    unittest.main()