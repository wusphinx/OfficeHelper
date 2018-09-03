import unittest
from helper import XlsHelper
from helper import SuffixError

class TestXlsHelper(unittest.TestCase):
    def test_init(self):
        pass

    def test_check_file_suffix(self):
        with self.assertRaises(SuffixError) as cm:
            XlsHelper("ok").check_file_suffix()

if __name__ == '__main__':
    unittest.main()