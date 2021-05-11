import re
import time

from xc_automation_test.src import base


class VirtualMachineOverview(base.NovaBase):

    def test_virtual_machine_overview(self):
        # 进入虚拟机总览页面
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[1]/p').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]'
                                          '/div[2]/div[2]/div[2]/div[1]/span').click()
        time.sleep(2)
        # 1.健康状态
        vmware_in = int(self.driver.find_element_by_xpath('//*[@id="test_oOCap"]/'
                                                          'div[2]/div[1]/div[2]/div/div[1]/div/p').text)  # 在线
        vmware_out = int(self.driver.find_element_by_xpath(
            '//*[@id="test_oOCap"]/div[2]/div[1]/div[2]/div/div[2]/div/p').text)  # 离线
        power1 = int(self.driver.find_element_by_xpath('//*[@id="test_oOCap"]/div[2]'
                                                       '/div[2]/div[2]/div/div[1]/div/p').text)
        power2 = int(self.driver.find_element_by_xpath('//*[@id="test_oOCap"]/'
                                                       'div[2]/div[2]/div[2]/div/div[2]/div/p').text)
        if vmware_in + vmware_out >= power1 + power2:
            print('\nCases01:\n步骤:验证虚拟机电源状态数据回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases01:\n步骤:验证虚拟机电源状态数据回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        self.driver.find_element_by_xpath('//*[@id="test_oOCap"]/div[2]/'
                                          'div[1]/div[2]/div/div[2]').click()
        time.sleep(1)
        vm_ware = self.driver.find_element_by_xpath('//*[@id="test_vPag"]/div[1]').text
        vm_ware = re.sub("\\D", "", vm_ware)
        vm_ware = int(vm_ware[2:])
        if vmware_in + vmware_out == vm_ware:
            print('\nCases02:\n步骤:验证虚拟机数量回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases02:\n步骤:验证虚拟机数量回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 2.容量状态
        u_cpu = 0
        for c in range(1, vm_ware + 1):
            if c > 10:
                break
            else:
                cpu_x = int(self.driver.find_element_by_xpath(
                    '//*[@id="test_vTab"]/div[3]/table/tbody/tr[' + str(c) + ']/td[3]/div/div/span').text)
                u_cpu = u_cpu + cpu_x  # 已用CPU之和
        u_ram = 0
        for r in range(1, vm_ware + 1):
            if r > 10:
                break
            else:
                ram_x = self.driver.find_element_by_xpath(
                    '//*[@id="test_vTab"]/div[3]/table/tbody/tr[' + str(r) + ']/td[4]/div/div/span').text
                ram_x = int(re.sub("\\D", "", ram_x))
                u_ram = u_ram + ram_x  # 已用内存之和
        self.driver.back()
        time.sleep(2)
        cpu = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/'
                                                'div[2]/div[3]/div[1]/div/div[3]/p').text
        cpu = int(re.sub("\\D", "", cpu))  # 容量状态cpu
        ram = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                                'div[2]/div[2]/div[3]/div[2]/div/div[3]/p').text
        ram = int(re.sub("\\D", "", ram))  # 容量状态内存

        if u_cpu == cpu and u_ram == ram:
            print('\nCases03:\n步骤:验证容量状态回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases03:\n步骤:验证容量状态回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 告警
        sum_p = 0
        for i in range(1, 4):
            p = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[3]/div[1]/div/'
                                                  'div[2]/div[2]/div[1]/ul/li[' + str(i) + ']/span').text
            p = int(re.sub("\\D", "", p))
            sum_p = sum_p + p  # 优先级列表之和
        sum_s = 0
        for n in range(1, 4):
            s = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[3]/div[1]/div/'
                                                  'div[2]/div[2]/div[2]/ul/li[' + str(n) + ']/span').text
            s = int(re.sub("\\D", "", s))
            sum_s = sum_s + s  # 状态列表之和
        if sum_p == sum_s:
            print('\nCases04:\n步骤:验证告警信息回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases04:\n步骤:验证告警信息回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
