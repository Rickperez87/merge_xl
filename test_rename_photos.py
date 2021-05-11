import unittest
import rename_photos

class test_rename_photos(unittest.TestCase):
    def test_init_files(self):
        test_param='*^#_   a_b   *#^$c.jpeg'
        self.assertEqual(rename_photos.remove_spaces_special_chars(test_param)
,'abc')
    pass

if __name__ == '__main__':
    unittest.main()