import unittest
from survey import AnonymousSurvey

class TestAnoymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类进行测试'''
    def test_store_single_response(self):
        '''测试单个答案会被妥善保存'''
        question = '你最近在学习什么技能？'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        '''测试三个答案会被妥善保存'''
        question = '你最近在学习什么技能？'
        my_survey = AnonymousSurvey(question)
        responses = ['English','Janpanese','German']


        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()