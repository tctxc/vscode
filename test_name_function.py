import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #集成自unittest.TestCase类
    '''测试name_function.py'''

    def test_first_last_name(self): #测试方法必须有test_开头
        '''能够正确处理向Janis Joplin这样的姓名吗'''
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #assertEqual()断言方法，核实运行的结果和期待的结果是否一致


    def test_first_last_middle(self):
        '''能够正确处理Wolfgang Amadeus Mozart这样的姓名吗？'''
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
