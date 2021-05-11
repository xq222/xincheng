import time

from xc_automation_test.src import base
#from selenium.common import exceptions as selenium_e
from selenium.common.exceptions import NoSuchElementException



class Alarm(base.NovaBase):

    def test_alarm(self):
        '''跳转告警页面'''
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/'
                                          'ul/li[5]/div[1]/p').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/'
                                          'li[5]/div[2]/div/div[2]/div[2]/span').click()
        time.sleep(2)
        # 1.级别筛选条件
        num = 0
        for i in range(2, 5):
            num += 1
            self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/div[4]/div/div[2]/span/span/i').click()
            time.sleep(2)
            P = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/'
                                                  'div[1]/ul/li[' + str(i) + ' ]/span')
            P_txt = P.text
            P.click()  # 选择级别
            time.sleep(1)
            self.driver.find_element_by_id('test_eventFilter').click()  # 搜索
            time.sleep(3)
            try:
                assert self.driver.find_element_by_xpath(
                    '//*[@id="test_eventTab"]/div[3]/table/tbody/tr[1]/td[8]/div').is_displayed()
                if self.driver.find_element_by_xpath(
                        '//*[@id="test_eventTab"]/div[3]/table/tbody/tr[1]/td[8]/div').text == P_txt:
                    print('\nCases0' + str(num) + ':\n步骤:告警级别选择:' + P_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索成功。\nPass')
                else:
                    print('\nCases0' + str(num) + ':\n步骤:告警级别选择:' + P_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索失败。\nFail')
            except NoSuchElementException:
                print('\nCases0' + str(num) + ':\n步骤:告警级别选择:' + P_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:暂无数据。\nPass')

            self.driver.find_element_by_xpath(
                '//*[@id="test_eventOpen"]/div[4]/div/div[1]/span/span/i').click()  # 清除筛选条件
            time.sleep(2)
        # 2.状态筛选条件
        self.driver.refresh()  # 清空筛选条件
        time.sleep(2)
        num2 = num
        for o in range(2, 5):
            num2 += 1
            self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/div[8]/div/div[2]/span/span/i').click()
            time.sleep(1)
            state = self.driver.find_element_by_xpath('/html/body/div[2]/'
                                                      'div[1]/div[1]/ul/li[' + str(o) + ']/span')
            state_txt = state.text
            state.click()  # 选择状态
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                              'div[1]/div/span[2]/span[1]').click()  # 点击空白处，收起下拉框
            time.sleep(1)
            self.driver.find_element_by_id('test_eventFilter').click()
            time.sleep(3)
            try:
                assert self.driver.find_element_by_xpath(
                    '//*[@id="test_eventTab"]/div[3]/table/tbody/tr[1]/td[9]/div/div').is_displayed()
                if self.driver.find_element_by_xpath(
                        '//*[@id="test_eventTab"]/div[3]/table/tbody/tr[1]/td[9]/div/div').text == state_txt:
                    print('\nCases0' + str(num2) + ':\n步骤:告警状态选择:' + state_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索成功。\nPass')
                else:
                    print('\nCases0' + str(num2) + ':\n步骤:告警状态选择:' + state_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索失败。\nFail')
            except NoSuchElementException:
                print('\nCases0' + str(num2) + ':\n步骤:告警状态选择:' + state_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:暂无数据。\nPass')

            self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/div[8]/div/div[1]/span/span/i').click()
            time.sleep(2)

        # 3.虚拟机筛选条件
        self.driver.refresh()  # 清空筛选条件
        time.sleep(2)
        num3 = num2
        for p in range(2, 4):
            num3 += 1
            self.driver.find_element_by_xpath('//*[@id="test_eventOpen"]/div[6]/div/div[2]/span/span/i').click()
            time.sleep(2.5)
            vm = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/'
                                                   'div[1]/ul/li[' + str(p) + ']/span')
            vm_txt = vm.text
            vm.click()  # 选择状态
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                              'div[1]/div/span[2]/span[1]').click()  # 点击空白处，收起下拉框
            time.sleep(1)
            self.driver.find_element_by_id('test_eventFilter').click()
            time.sleep(3)
            try:
                assert self.driver.find_element_by_xpath(
                    '//*[@id="test_eventTab"]/div[3]/table/tbody/tr[1]/td[9]/div/div').is_displayed()  # 暂用状态字段来判断
                print('\nCases0' + str(num3) + ':\n步骤:虚拟机选择:' + vm_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索成功。\nPass')

            except NoSuchElementException:
                print('\nCases0' + str(num3) + ':\n步骤:虚拟机选择:' + vm_txt + ',点击搜索。\n预期结果:搜索成功。\n实际结果:暂无数据。\nPass')

            self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                              'div[2]/div/div[2]/div[6]/div/div[1]/span/span/i').click()
            time.sleep(2)