import re
import time

from xc_automation_test.src import base


class StorageOverview(base.NovaBase):

    def test_storage_overview(self):
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[1]/p').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[2]/div[3]/div[2]/div[1]/span').click()
        time.sleep(3)
        # 存储池
        save1 = int(self.driver.find_element_by_xpath('//*[@id="test_health02"]/'
                                                      'div[2]/div/div[2]/div/div[1]/div/p').text)
        save2 = int(self.driver.find_element_by_xpath('//*[@id="test_health02"]/'
                                                      'div[2]/div/div[2]/div/div[2]/div/p').text)
        self.driver.find_element_by_xpath('//*[@id="test_health02"]/div[2]/div/div[2]/div/div[2]').click()
        time.sleep(3)
        save = self.driver.find_elements_by_xpath('//*[@id="test_pool_01"]/div[3]/table/tbody/tr')
        if int(save1 + save2) == int(len(save)):
            print('\nCases01:\n步骤:验证存储池数量回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases01:\n步骤:验证存储池数量回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        self.driver.back()
        time.sleep(3)
        # 数据状态
        data1 = self.driver.find_element_by_id('test_data_status').text
        data2 = self.driver.find_element_by_id('test_rate_02').text
        if data1 == '数据可用' and data2 == '100 %':
            print('\nCases02:\n步骤:验证数据状态回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases02:\n步骤:验证数据状态回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 告警
        sumP = 0
        for i in range(1, 4):
            P = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                                  'div[3]/div/div[2]/div[2]/div[1]/ul/li[' + str(i) + ']/span').text
            P = int(re.sub("\D", "", P))
            sumP = sumP + P  # 优先级列表之和
        sumS = 0
        for n in range(1, 4):
            S = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                                  'div[3]/div/div[2]/div[2]/div[2]/ul/li[' + str(n) + ']/span').text
            S = int(re.sub("\D", "", S))
            sumS = sumS + S  # 状态列表之和
        if sumP == sumS:
            print('\nCases03:\n步骤:验证告警数量回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases03:\n步骤:验证告警数量回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # top3过去24小时
        title1 = self.driver.find_element_by_xpath('//*[@id="test_top2"]/div[1]/div').text
        title2 = self.driver.find_element_by_xpath('//*[@id="test_top2"]/div[2]/div').text
        self.driver.find_element_by_xpath('//*[@id="test_top2"]/div[2]/div').click()
        time.sleep(4)
        title = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[1]/div/span/span[1]').text
        con1 = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                                 'div[2]/div/div[2]/div[6]/div/div[1]/span/span[1]/span').text
        con2 = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                                 'div[2]/div/div[2]/div[6]/div/div[1]/span/span[2]/span').text
        if title == '性能分析' and title1[0:3] == con1[0:3] and title2[0:3] == con2[0:3]:
            print('\nCases04:\n步骤:验证TOP3跳转条件回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases04:\n步骤:验证TOP3跳转条件回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        self.driver.back()
        time.sleep(3)
        # 容量状态
        allram1 = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                    'div[2]/div[3]/div[1]/div[3]/div[1]/div/div[3]/p').text
        useram1 = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                    'div[2]/div[3]/div[1]/div[3]/div[2]/div/div[3]/p').text
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[2]/div/p').click()
        time.sleep(3)
        allram2 = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                    'div[2]/div[3]/div[3]/div[3]/div/div[3]/p').text
        useram2 = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                    'div[2]/div[3]/div[3]/div[4]/div/div[3]/p').text
        if allram1 == allram2 and useram1 == useram2:
            print('\nCases05:\n步骤:验证容量状态回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases05:\n步骤:验证容量状态回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
