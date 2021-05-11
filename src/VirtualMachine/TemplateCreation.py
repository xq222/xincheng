import time
import random

from xc_automation_test.src import base


class TemplateCreation(base.NovaBase):

    def test_Virtual_machine_template_creation(self):
        '''从模板中创建虚拟机'''
        self.driver.find_element_by_xpath('//*[@id="test_health1"]/div[3]/div[2]/div[2]').click()
        time.sleep(2)#跳转虚拟机页面
        self.driver.find_element_by_id('test_vCreate').click()
        time.sleep(2)
        # 选择模板部署
        self.driver.find_element_by_id('test_cTem').click()
        time.sleep(1)
        vname = self.driver.find_element_by_xpath('//*[@id="test_cTName"]/div/div/div[1]/input')
        next = self.driver.find_element_by_id("test_cTNext")
        # 1.验证虚拟机名称字段
        vname.send_keys("")  # 2.1虚拟机名称输入为空，点击下一步
        next.click()
        time.sleep(1)
        tips1 = self.driver.find_element_by_xpath('//*[@id="test_cTName"]/div/div/div[2]')
        if tips1.text == '请输入虚拟机名称':
            print('\nCases01:\n步骤:虚拟机名称输入为空，点击保存。\n预期结果:请输入虚拟机名称\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases01:\n步骤:虚拟机名称输入为空，点击保存。\n预期结果:请输入虚拟机名称\n实际结果:' + tips1.text + '\nFail')
        vname.send_keys("23@#as")  # 2.2虚拟机名称包含特殊字符，点击下一步
        time.sleep(1)
        next.click()
        time.sleep(1)
        if tips1.text == '仅限字母、数字、中文及特殊字符"_"、"-"':
            print('\nCases02:\n步骤:虚拟机名称包含特殊字符(23@#as)，点击保存。'
                  '\n预期结果:仅限字母、数字、中文及特殊字符"_"、"-"\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases02:\n步骤:虚拟机名称包含特殊字符(23@#as)，点击保存。'
                  '\n预期结果:仅限字母、数字、中文及特殊字符"_"、"-"\n实际结果:' + tips1.text + '\nFail')
        vname.clear()
        vname.send_keys("sx")  # 2.3虚拟机名称小于3位时，点击下一步
        next.click()
        time.sleep(1)
        if tips1.text == '虚拟机名称长度为3-16个字符':
            print('\nCases03:\n步骤:虚拟机名称小于3位(sx)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases03:\n步骤:虚拟机名称小于3位(sx)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + tips1.text + '\nFail')
        vname.clear()
        vname.send_keys('qwertyuioplkjhgf3')  # 2.4虚拟机名称大于16位时，点击下一步
        next.click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="test_cTName"]/div/div/div[2]').text == '虚拟机名称长度为3-16个字符':
            print('\nCases04:\n步骤:虚拟机名称大于16位(qwertyuioplkjhgf3)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + self.driver.find_element_by_xpath(
                '//*[@id="test_cTName"]/div/div/div[2]').text + '\nPass')
        else:
            print('\nCases04:\n步骤:虚拟机名称大于16位(qwertyuioplkjhgf3)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + self.driver.find_element_by_xpath(
                '//*[@id="test_cTName"]/div/div/div[2]').text + '\nFail')
        vname.clear()
        a = random.randint(0, 999)
        vname.send_keys("Test" + str(a))  # 2.5虚拟机名称输入有效值
        time.sleep(2)
        # 2.验证运行主机字段
        Yserver = ["xc-cdh-node-1", "xc-cdh-node-2", "xc-cdh-node-3"]
        self.driver.find_element_by_xpath('//*[@id="test_cTMain"]/div/div/div/div/input').click()
        time.sleep(2)
        server1 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').text
        time.sleep(1)
        server2 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').text
        time.sleep(1)
        server3 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').text
        Nserver = [server1, server2, server3]
        if Yserver == Nserver:
            print('\nCases05:\n步骤:验证运行主机名称回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases05:\n步骤:验证运行主机名称回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()  # 选择运行主机
        time.sleep(1)
        next.click()  # 使用默认模板直接下一步
        time.sleep(2)

        # 获取虚拟机信息
        vm_name = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[1]/p[2]').text
        running_host = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[2]/p[2]').text
        v_cpu = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[3]/p[2]').text
        memory = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[4]/p[2]').text
        sound_card = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[5]/p[2]').text
        disk = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[6]/p[2]').text
        network_interface = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[7]/p[2]').text
        system_version = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[8]/p[2]').text
        system_family = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[9]/p[2]').text
        iso_name = self.driver.find_element_by_xpath('//*[@id="test_cTShow"]/li[10]/p[2]').text

        next.click()  # 点击创建
        time.sleep(10)
        if self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/span').text == "Test" + str(a):

            print('\nCases06:\n步骤:从模板部署虚拟机，虚拟机配置如下:'
                  '\n<虚拟机名称>' + vm_name +
                  '\n<运行主机>' + running_host +
                  '\n<vCPU>' + v_cpu +
                  '\n<内存>' + memory + 'MB'
                  '\n<声卡>' + sound_card +
                  '\n<磁盘>' + disk +
                  '\n<网络接口>' + network_interface +
                  '\n<系统版本>' + system_version +
                  '\n<系统系列>' + system_family +
                  '\n<镜像名称>' + iso_name +
                  '\n预期结果:虚拟机创建成功。\n实际结果:虚拟机创建成功。\nPass')
        else:
            print('\nCases06:\n步骤:从模板部署虚拟机，虚拟机配置如下:'
                  '\n<虚拟机名称>' + vm_name +
                  '\n<运行主机>' + running_host +
                  '\n<vCPU>' + v_cpu +
                  '\n<内存>' + memory + 'MB'
                  '\n<声卡>' + sound_card +
                  '\n<磁盘>' + disk +
                  '\n<网络接口>' + network_interface +
                  '\n<系统版本>' + system_version +
                  '\n<系统系列>' + system_family +
                  '\n<镜像名称>' + iso_name +
                  '\n预期结果:虚拟机创建成功。\n实际结果:虚拟机创建失败。\nFail')

