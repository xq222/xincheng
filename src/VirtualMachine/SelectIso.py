import time
import random

from xc_automation_test.src import base


class SelectIso(base.NovaBase):

    def test_Virtual_machine_select_iso(self):
        '''---选择镜像创建虚拟机---'''
        iso1 = ['测试ISO.iso', 'Ubuntu', 'Ubuntu 18.04 server(64位)']
        iso2 = ["测试ISO2.iso", "Windows", "Windows 10(64位)"]
        isoname = (iso1[0], iso2[0])
        self.driver.find_element_by_xpath('//*[@id="test_health1"]/div[3]/div[2]/div[2]').click()
        time.sleep(3)#跳转虚拟机页面
        self.driver.find_element_by_id('test_vCreate').click()
        time.sleep(2)
        # 选择创建新虚拟机
        self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[1]/div[1]/img').click()
        time.sleep(2)
        # 1.验证镜像回显
        viso1 = self.driver.find_element_by_xpath('//*[@id="test_cSelIso"]/option[1]')
        viso2 = self.driver.find_element_by_xpath('//*[@id="test_cSelIso"]/option[2]')
        visoname = (viso1.text, viso2.text)
        if isoname == visoname:
            print('\nCases01\n步骤:验证镜像回显是否正确。\n预期结果:镜像回显正确。\n实际结果:镜像回显正确。\nPass')
        else:
            print('\nCases01\n步骤:验证镜像回显是否正确。\n预期结果:镜像回显正确。\n实际结果:镜像已变更，请人工核查。\nFail')
            print(visoname)
        # 2.验证镜像版本
        viso1.click()
        next = self.driver.find_element_by_xpath('//*[@id="test_cINext"]')
        next.click()
        time.sleep(1)
        next.click()
        time.sleep(1)
        num = random.randint(0, 999)
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[1]/div/div[1]/input').send_keys('Test' + str(num))
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[14]/div/div[2]/div[2]/i').click()
        time.sleep(1)
        next.click()
        time.sleep(2)
        viso1name = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[10]/p[2]').text
        viso1Vx1 = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[8]/p[2]').text
        viso1Vx2 = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[9]/p[2]').text
        viso1check = [viso1name, viso1Vx1, viso1Vx2]

        if iso1 == viso1check:
            print('\nCases02\n步骤:验证镜像版本回显是否正确。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases02\n步骤:验证镜像版本回显是否正确。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 获取虚拟机信息
        vm_name = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[1]/p[2]').text
        running_host = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[2]/p[2]').text
        v_cpu = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[3]/p[2]').text
        memory = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[4]/p[2]').text
        sound_card = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[5]/p[2]').text
        disk = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[6]/p[2]').text
        network_interface = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[7]/p[2]').text
        system_version = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[8]/p[2]').text
        system_family = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[9]/p[2]').text
        iso_name = self.driver.find_element_by_xpath('//*[@id="test_cIShow"]/li[10]/p[2]').text

        next.click()  # 点击创建
        time.sleep(10)
        if self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/span').text == "Test" + str(num):

            print('\nCases03:\n步骤:选择ISO新建虚拟机，虚拟机配置如下:'
                  '\n<虚拟机名称>' + vm_name +
                  '\n<运行主机>' + running_host +
                  '\n<vCPU>' + v_cpu +
                  '\n<内存>' + memory +
                  '\n<声卡>' + sound_card +
                  '\n<磁盘>' + disk +
                  '\n<网络接口>' + network_interface +
                  '\n<系统版本>' + system_version +
                  '\n<系统系列>' + system_family +
                  '\n<镜像名称>' + iso_name +
                  '\n预期结果:虚拟机创建成功。\n实际结果:虚拟机创建成功。\nPass')

        else:
            print('\nCases03:\n步骤:选择ISO新建虚拟机，虚拟机配置如下:'
                  '\n<虚拟机名称>' + vm_name +
                  '\n<运行主机>' + running_host +
                  '\n<vCPU>' + v_cpu +
                  '\n<内存>' + memory +
                  '\n<声卡>' + sound_card +
                  '\n<磁盘>' + disk +
                  '\n<网络接口>' + network_interface +
                  '\n<系统版本>' + system_version +
                  '\n<系统系列>' + system_family +
                  '\n<镜像名称>' + iso_name +
                  '\n预期结果:虚拟机创建成功。\n实际结果:虚拟机创建失败。\nFail')
