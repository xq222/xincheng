import time

from xc_automation_test.src import base
#from selenium.common import exceptions as selenium_e
from selenium.common.exceptions import NoSuchElementException


class Task(base.NovaBase):

    def test_task(self):
        '''跳转任务页面'''
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[5]/div[1]/p/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[5]/div[2]/div/div[2]/div[1]/span').click()
        time.sleep(3)
        search = self.driver.find_element_by_id('test_taskFilter')
        # 1.任务名称检索条件
        Tname = ['创建虚拟机', '创建虚拟机模板', '开启虚拟机', '删除虚拟机模板', '添加视图', '物理删除视图']
        taskname = self.driver.find_element_by_xpath('//*[@id="test_taskOpen"]/div[3]/div/div[1]/input')
        num = 0
        for i in Tname:
            num += 1
            taskname.send_keys(i)
            time.sleep(1)
            search.click()
            time.sleep(3.5)
            taskname.clear()
            try:
                assert self.driver.find_element_by_xpath(
                    '//*[@id="test_taskTab"]/div[3]/table/tbody/tr[1]/td[2]/div').is_displayed()
                if self.driver.find_element_by_xpath(
                        '//*[@id="test_taskTab"]/div[3]/table/tbody/tr[1]/td[2]/div').text == i:
                    print('\nCases0' + str(num) + ':\n步骤:任务名称输入:' + i + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索成功。\nPass')
                else:
                    print('\nCases0' + str(num) + ':\n步骤:任务名称输入:' + i + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索失败。\nFail')
            except NoSuchElementException:
                print('\nCases0' + str(num) + ':\n步骤:任务名称输入:' + i + ',点击搜索。\n预期结果:搜索成功。\n实际结果:暂无数据。\nPass')

        # 2.目标类型检索条件
        self.driver.refresh()  # 清空筛选条件
        time.sleep(2)
        num2 = num
        for o in range(2, 10):
            num2 += 1
            self.driver.find_element_by_xpath('//*[@id="test_taskOpen"]/div[4]/div/div[2]/span/span/i').click()
            time.sleep(2)
            Target_type = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/'
                                                     'div[1]/ul/li[' + str(o) + ']/span')
            T_text = Target_type.text
            time.sleep(1)
            Target_type.click()  # 选择类型
            time.sleep(2)
            self.driver.find_element_by_id('test_taskFilter').click()  # 查找
            time.sleep(3.5)
            try:
                assert self.driver.find_element_by_xpath(
                    '//*[@id="test_taskTab"]/div[3]/table/tbody/tr[1]/td[5]/div').is_displayed()
                if self.driver.find_element_by_xpath(
                        '//*[@id="test_taskTab"]/div[3]/table/tbody/tr[1]/td[5]/div').text == T_text:
                    print('\nCases0' + str(num2) + ':\n步骤:目标类型选择:' + T_text + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索成功。\nPass')
                else:
                    print('\nCases0' + str(num2) + ':\n步骤:目标类型选择:' + T_text + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索失败。\nFail')
            except NoSuchElementException:
                print('\nCases0' + str(num2) + ':\n步骤:目标类型选择:' + T_text + ',点击搜索。\n预期结果:搜索成功。\n实际结果:暂无数据。\nPass')

            self.driver.find_element_by_xpath('//*[@id="test_taskOpen"]/div[4]/div/div[1]/span/span/i').click()  # 清除上一个条件

        # 3.结果检索条件
        self.driver.refresh()  # 清空筛选条件
        time.sleep(2)
        num3  = num2
        for p in range(2, 6):
            self.driver.find_element_by_xpath('//*[@id="test_taskOpen"]/div[6]/div/div[2]/span').click()
            time.sleep(2)
            res = self.driver.find_element_by_xpath('/html/body/div[2]/'
                                                    'div[1]/div[1]/ul/li[' + str(p) + ']/span')
            time.sleep(2)
            res.click()  # 选择结果
            resname = res.text
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="r_content"]/div[2]/div[1]/div/span[2]/span[1]').click()  # 点击空白处，收起下拉框
            time.sleep(2)
            self.driver.find_element_by_id('test_taskFilter').click()
            time.sleep(3.5)
            try:
                assert self.driver.find_element_by_xpath(
                    '//*[@id="test_taskTab"]/div[3]/table/tbody/tr[1]/td[7]/div/div').is_displayed()
                if self.driver.find_element_by_xpath(
                        '//*[@id="test_taskTab"]/div[3]/table/tbody/tr[1]/td[7]/div/div').text == resname:
                    print('\nCases0' + str(num3) + ':\n步骤:结果选择:' + resname + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索成功。\nPass')
                else:
                    print('\nCases0' + str(num3) + ':\n步骤:结果选择:' + resname + ',点击搜索。\n预期结果:搜索成功。\n实际结果:搜索失败。\nFail')
            except NoSuchElementException:
                print('\nCases0' + str(num3) + ':\n步骤:结果选择:' + resname + ',点击搜索。\n预期结果:搜索成功。\n实际结果:暂无数据。\nPass')

            self.driver.find_element_by_xpath('//*[@id="test_taskReset"]').click()  # 重置筛选条件
            time.sleep(2)