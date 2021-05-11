import time

from xc_automation_test.src import base


class ServerDetails(base.NovaBase):

    def test_server_details(self):
        # 进入服务器详情页面
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[1]/p').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[2]/'
                                          'div[1]/div[2]/div[2]/span').click()
        time.sleep(2)
        # 1.跳转告警
        time.sleep(3)
        server_name = self.driver.find_element_by_xpath('//*[@id="test_chart_content"]/'
                                                        'div[1]/div/div[1]/div[1]/p').text
        self.driver.find_element_by_xpath('//*[@id="test_chart_content"]/div[1]/div/'
                                          'div[1]/div[2]/ul[1]/li[1]').click()
        time.sleep(2)
        title1 = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                                   'div[1]/div/span[2]/span[1]').text
        con1 = self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/div[3]/'
                                                 'div/div[1]/span/span/span').text
        con2 = self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/'
                                                 'div[5]/div/div[1]/span/span/span').text
        if title1 == '事件和告警' and con1 == '告警' and con2 == server_name:
            print('\nCases01:\n步骤:点击告警按钮。\n预期结果:跳转告警页面并代入相应的筛选条件。'
                  '\n实际结果:跳转告警页面并代入相应的筛选条件。\nPass')
        else:
            print('\nCases01:\n步骤:点击告警按钮。\n预期结果:跳转告警页面并代入相应的筛选条件。'
                  '\n实际结果:跳转失败。\nFail')
        # 2.跳转事件
        self.driver.back()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_chart_content"]/div[1]/'
                                          'div/div[1]/div[2]/ul[1]/li[2]').click()
        time.sleep(2)
        con3 = self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/div[3]/'
                                                 'div/div[1]/span/span/span').text
        con4 = self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/div[5]/'
                                                 'div/div[1]/span/span/span').text
        if title1 == '事件和告警' and con3 == '事件' and con4 == server_name:
            print('\nCases02:\n步骤:点击事件按钮。\n预期结果:跳转事件页面并代入相应的筛选条件。'
                  '\n实际结果:跳转事件页面并代入相应的筛选条件。\nPass')
        else:
            print('\nCases02:\n步骤:点击事件按钮。\n预期结果:跳转事件页面并代入相应的筛选条件。'
                  '\n实际结果:跳转失败。\nFail')
        # 3.跳转任务
        self.driver.back()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_chart_content"]/div[1]/'
                                          'div/div[1]/div[2]/ul[1]/li[3]').click()
        time.sleep(2)
        title2 = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                                   'div[1]/div/span[2]/span[1]').text
        if title2 == '任务':
            print('\nCases03:\n步骤:点击任务按钮。\n预期结果:跳转任务页面并代入相应的筛选条件。'
                  '\n实际结果:跳转任务页面并代入相应的筛选条件。\nPass')
        else:
            print('\nCases03:\n步骤:点击任务按钮。\n预期结果:跳转任务页面并代入相应的筛选条件。'
                  '\n实际结果:跳转失败。\nFail')
        # 4.系统配置与反面
        self.driver.back()
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="test_chart_content"]'
                                          '/div[1]/div/div[2]/div[2]/div[2]/button[2]').click()  # 切换背面
        server_name2 = self.driver.find_element_by_xpath('//*[@id="test_baseinfo_01"]'
                                                         '/div[3]/ul/li[1]/span[2]').text  # 系统配置节点名称
        if server_name == server_name2:
            print('\nCases04:\n步骤:验证节点名称回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases04:\n步骤:验证节点名称回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 5.服务器操作,服务已在维护状态
        # self.driver.back()
        # time.sleep(1)
        # self.driver.refresh()
        # time.sleep(2)
        # self.driver.find_element_by_id('list').click()#切换列表视图
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="test_list_content"]/div/'
        #                                   'div/div[3]/table/tbody/tr[1]/td[9]/div/ul/li[3]').click()#点击关闭电源按钮
        # time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div['
        #                                   '2]/div[2]/form/div[2]/div/div[1]/input').send_keys('cs123456')
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[1]'
        #                                   '/div[3]/button[2]').click()
        # time.sleep(1.5)
        # self.driver.find_element_by_xpath('/html/body/div[3]/'
        #                                   'div[1]/div[3]/button[2]').click()#确认关闭
        # time.sleep(1)
        # self.driver.refresh()
        # time.sleep(2)
        # self.driver.find_element_by_id('list').click()  # 切换列表视图
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="test_list_content"]/div/'
        #                                   'div/div[3]/table/tbody/tr[1]/td[9]/div/ul/li[4]').click()#点击软关机
        # time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/'
        #                                   'div[2]/div[2]/form/div[2]/div/div/input').send_keys('cs123456')
        # self.driver.find_element_by_xpath('/html/body/'
        #                                   'div[2]/div[1]/div[3]/button[2]').click()
        # time.sleep(1.5)
        # self.driver.find_element_by_xpath('/html/body/div[3]/'
        #                                   'div[1]/div[3]/button[2]').click()#确认关闭
        # time.sleep(1)
        # self.driver.refresh()
        # time.sleep(2)
        # self.driver.find_element_by_id('list').click()  # 切换列表视图
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="test_list_content"]/div/div/'
        #                                   'div[3]/table/tbody/tr[1]/td[9]/div/ul/li[5]').click()#点击关机重启
        # time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/'
        #                                   'div[2]/div[2]/form/div[2]/div/div/input').send_keys('cs123456')
        # self.driver.find_element_by_xpath('/html/body/div[2]/'
        #                                   'div[1]/div[3]/button[2]').click()
        # time.sleep(1.5)
        # self.driver.find_element_by_xpath('/html/body/div[3]/'
        #                                   'div[1]/div[3]/button[2]').click()#确认关闭
