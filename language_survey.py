from survey import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = '你最近在学习什么技能？'
my_survey = AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("输入'q'可以退出程序：")
while True:
    response = input('请输入你的答案：')
    if response == 'q':
        break
    my_survey.store_response(response)


#显示全部调查结果
print('\n感谢参与调查问卷！')
my_survey.show_results()