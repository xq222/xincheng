import re
import time

from xc_automation_test.src import base


class ServerOverview(base.NovaBase):

    def test_server_overview(self):
        # 进入服务器总览页面
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[1]/p').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]'
                                          '/div[2]/div[1]/div[2]/div[1]/span').click()
        time.sleep(2)

        # 1.健康状态
        server_in = int(self.driver.find_element_by_xpath(
            '//*[@id="test_health2"]/div[2]/div[1]/div[2]/div/div[1]/div/p').text)  # 在线
        server_out = int(self.driver.find_element_by_xpath('//*[@id="test_health2"]/div[2]/'
                                                           'div[1]/div[2]/div/div[2]/div/p').text)  # 离线
        self.driver.find_element_by_xpath('//*[@id="test_health2"]/div[2]/div[1]/div[2]/div/div[1]').click()  # 去服务器详情页
        time.sleep(2)
        server_all = int(len(self.driver.find_elements_by_xpath('//*[@id="test_list_content"]'
                                                                '/div/div/div[3]/table/tbody/tr')))
        if server_in + server_out == server_all:
            print('\nCases01:\n步骤:验证服务器数量回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases01:\n步骤:验证服务器数量回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        self.driver.back()
        time.sleep(2)
        disk_in = int(self.driver.find_element_by_xpath('//*[@id="test_health2"]/'
                                                        'div[2]/div[2]/div[2]/div/div[1]/div/p').text)  # 在线
        disk_out = int(self.driver.find_element_by_xpath('//*[@id="test_health2"]/'
                                                         'div[2]/div[2]/div[2]/div/div[2]/div/p').text)  # 离线
        if disk_in == 15 and disk_out == 0:  # 虚拟机没有磁盘信息
            print('\nCases02:\n步骤:验证硬盘数量回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases02:\n步骤:验证硬盘数量回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 2.容量状态
        cpu = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                                'div[2]/div[3]/div[1]/div/div[3]/p').text
        ram = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                                'div[2]/div[3]/div[2]/div/div[3]/p').text
        self.driver.back()  # 返回仪表盘
        time.sleep(2.5)
        v_cpu = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                                  'div[3]/div[3]/div[1]/div/div[3]/p').text
        v_ram = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                                  'div[3]/div[3]/div[2]/div/div[3]/p').text
        if cpu == v_cpu and ram == v_ram:
            print('\nCases03:\n步骤:验证容量状态数据回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases03:\n步骤:验证容量状态数据回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        self.driver.forward()
        time.sleep(1.5)

        # 3.告警
        sum_p = 0
        for i in range(1, 4):
            p = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/div[3]/'
                                                  'div/div[2]/div[2]/div[1]/ul/li[' + str(i) + ']/span').text
            p = int(re.sub("\\D", "", p))  # 优先级列表之和
            sum_p = sum_p + p
        sum_s = 0
        for n in range(1, 4):
            s = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/div[3]/'
                                                  'div/div[2]/div[2]/div[2]/ul/li[' + str(n) + ']/span').text
            s = int(re.sub("\\D", "", s))  # 状态列表之和
            sum_s = sum_s + s
        if sum_p == sum_s:
            print('\nCases04:\n步骤:验证告警数量回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases04:\n步骤:验证告警数量回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nFail')

        # 4.CPU、内存利用率
        time.sleep(1)
        cpu_use = self.driver.find_element_by_xpath('//*[@id="test_top1"]/div[1]/div[2]/ul').text
        ram_use = self.driver.find_element_by_xpath('//*[@id="test_top1"]/div[2]/div[2]/ul').text
        self.driver.back()
        time.sleep(2.5)
        v_cpu_use = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                      'div[2]/div[5]/div/div[2]/div[1]/div[2]/ul').text
        v_ram_use = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                      'div[2]/div[5]/div/div[2]/div[2]/div[2]/ul').text
        if cpu_use == v_cpu_use and ram_use == v_ram_use:
            print('\nCases05:\n步骤:验证CPU、内存利用率回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases05:\n步骤:验证CPU、内存利用率回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
