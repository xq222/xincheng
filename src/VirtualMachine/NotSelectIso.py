import re
import time
import random

from xc_automation_test.src import base


class NotSelectIso(base.NovaBase):

    def test_Virtual_machine_not_select_iso(self):
        '''---不选择镜像创建虚拟机---'''
        self.driver.find_element_by_xpath('//*[@id="test_health1"]/div[3]/div[2]/div[2]').click()
        time.sleep(2)
        # 新建虚拟机
        self.driver.find_element_by_id('test_vCreate').click()
        time.sleep(3)
        # 选择新建
        self.driver.find_element_by_id('test_cIso').click()
        time.sleep(2)
        # 暂不选择镜像并下一步
        next = self.driver.find_element_by_id('test_cINext')
        next.click()
        time.sleep(1.5)
        # 1.验证操作系统与版本对应'''
        # 选择操作系统
        self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]/div'
                                          '[2]/div[2]/div[2]/form/div[1]/div/div/div/input').click()
        time.sleep(3)
        iso = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').text
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]/'
                                          'div[2]/div[2]/div[2]/form/div[2]/div/div/div/input').click()
        time.sleep(2)
        vx = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]').text
        if iso in vx:
            print('\nCases01:\n步骤:验证操作系统与版本是否对应。\n预期结果:系统与版本对应。\n实际结果:系统与版本对应。\nPass')
        else:
            print('\nCases01:\n步骤:验证操作系统与版本是否对应。\n预期结果:系统与版本对应。\n实际结果:系统与版本不对应。\nFail')
        next.click()
        time.sleep(1.5)
        # 2.验证虚拟机名称字段
        vname = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]'
                                                  '/div[1]/div[2]/div[3]/div[2]/form/div[1]/div/div[1]/input')
        vname.send_keys("")  # 2.1虚拟机名称输入为空，点击下一步
        next.click()
        time.sleep(1)
        tips1 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[1]/div/div[2]').text
        if tips1 == '请输入虚拟机名称':
            print('\nCases02:\n步骤:虚拟机名称输入为空，点击保存。\n预期结果:请输入虚拟机名称\n实际结果:' + tips1 + '\nPass')
        else:
            print('\nCases02:\n步骤:虚拟机名称输入为空，点击保存。\n预期结果:请输入虚拟机名称\n实际结果:' + tips1 + '\nFail')
        vname.send_keys("23@#as")  # 2.2虚拟机名称包含特殊字符，点击下一步
        next.click()
        time.sleep(1)
        tips2 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[1]/div/div[2]')
        if tips2.text == '仅限字母、数字、中文及特殊字符"_"、"-"':
            print('\nCases03:\n步骤:虚拟机名称包含特殊字符(23@#as)，点击保存。'
                  '\n预期结果:仅限字母、数字、中文及特殊字符"_"、"-"\n实际结果:' + tips2.text + '\nPass')
        else:
            print('\nCases03:\n步骤:虚拟机名称包含特殊字符(23@#as)，点击保存。'
                  '\n预期结果:仅限字母、数字、中文及特殊字符"_"、"-"\n实际结果:' + tips2.text + '\nFail')
        vname.clear()
        vname.send_keys("sx")  # 2.3虚拟机名称小于3位时，点击下一步
        next.click()
        time.sleep(1)
        if tips2.text == '虚拟机名称长度为3-16个字符':
            print('\nCases04:\n步骤:虚拟机名称小于3位(sx)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + tips2.text + '\nPass')
        else:
            print('\nCases04:\n步骤:虚拟机名称小于3位(sx)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + tips2.text + '\nFail')
        vname.clear()
        vname.send_keys("qwertyuioplkjhgfa")  # 2.4虚拟机名称大于16位时，点击下一步
        next.click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[1]/div/div[2]').text == '虚拟机名称长度为3-16个字符':
            print('\nCases05:\n步骤:虚拟机名称大于16位(qwertyuioplkjhgfa)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[1]/div/div[2]').text + '\nPass')
        else:
            print('\nCases05:\n步骤:虚拟机名称大于16位(qwertyuioplkjhgfa)，点击保存。'
                  '\n预期结果:虚拟机名称长度为3-16个字符\n实际结果:' + self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[1]/div/div[2]').text + '\nFail')
        vname.clear()
        num = random.randint(0, 999)
        vname.send_keys('Test' + str(num))  # 2.5虚拟机名称输入有效值
        time.sleep(1)

        # 3.验证主机是否正常
        # Yserver = ["cdh-test01","cdh-test02","cdh-test03"]
        # self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[2]/div/div/div/span/span/i').click()
        # time.sleep(2)
        # server1 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').text
        # server2 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').text
        # server3 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').text
        # Nserver = [server1,server2,server3]
        # if Yserver == Nserver:
        #     print("运行主机回显正确")
        # else:
        #     print("运行主机回显异常")
        #     print(Nserver)
        # time.sleep(3)
        # self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()#选择运行主机
        # time.sleep(1)

        # 4.vcpu字段验证
        vcpu = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]/'
                                                 'div[2]/div[3]/div[2]/form/div[3]/div/div[1]/div[1]/input')
        vcpu.click()
        vcpu.clear()
        vcpu.send_keys(" ")  # 4.1vcpu为空时，点击下一步
        time.sleep(1)
        next.click()
        time.sleep(1)
        tips3 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[3]/div/div[2]').text
        if tips3 == '格式不正确':
            print('\nCases06:\n步骤:vCPU输入为空格，点击保存。\n预期结果:格式不正确\n实际结果:' + tips3 + '\nPass')
        else:
            print('\nCases06:\n步骤:vCPU输入为空格，点击保存。\n预期结果:格式不正确\n实际结果:' + tips3 + '\nFail')
        vcpu.clear()
        vcpu.send_keys("was")  # 4.2vcpu为非法值，点击下一步
        next.click()
        time.sleep(1)
        tips3 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[3]/div/div[2]').text
        if tips3 == '格式不正确':
            print('\nCases07:\n步骤:vCPU输入非法值(was)，点击保存。\n预期结果:格式不正确\n实际结果:' + tips3 + '\nPass')
        else:
            print('\nCases07:\n步骤:vCPU输入非法值(was)，点击保存。\n预期结果:格式不正确\n实际结果:' + tips3 + '\nFail')
        cpu = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div'
                                                '[1]/div[2]/div[3]/div[2]/form/div[3]/div/div/div[2]/i').text
        cpu = int(re.sub("\D", "", cpu))
        time.sleep(1.5)
        vcpu.clear()
        vcpu.send_keys(cpu + 1)  # 4.3vcpu大于当前剩余数量时，点击下一步
        next.click()
        time.sleep(1)
        tips4 = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]'
                                                  '/div[2]/div[3]/div[2]/form/div[4]').text
        if tips4 == '可用vCPU个数不足':
            print('\nCases08:\n步骤:vCPU输入大于当前剩余数量时:' + (str(cpu + 1)) +'，点击保存。'
                  '\n预期结果:可用vCPU个数不足\n实际结果:' + tips4 + '\nPass')
        else:
            print('\nCases08:\n步骤:vCPU输入大于当前剩余数量时:' + (str(cpu + 1)) +'，点击保存。'
                  '\n预期结果:可用vCPU个数不足\n实际结果:' + tips4 + '\nFail')
        time.sleep(1)
        vcpu.clear()
        vcpu.send_keys('1')  # 输入个合法的值
        time.sleep(1)

        # 5.内存字段验证
        vram = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]/'
                                                 'div[2]/div[3]/div[2]/form/div[5]/div/div[1]/input')
        vcpu.click()
        vcpu.clear()
        vram.send_keys(" ")  # 5.1vram为空时，点击下一步
        time.sleep(1)
        next.click()
        time.sleep(1)
        tips5 = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]'
                                                  '/div[2]/div[3]/div[2]/form/div[5]/div/div[3]').text
        if tips5 == '格式不正确。':
            print('\nCases09:\n步骤:内存输入为空格，点击保存。'
                  '\n预期结果:格式不正确。\n实际结果:' + tips5 + '\nPass')
        else:
            print('\nCases09:\n步骤:内存输入为空格，点击保存。'
                  '\n预期结果:格式不正确。\n实际结果:' + tips5 + '\nFail')
        time.sleep(1)
        vram.clear()
        vram.send_keys("test")  # 5.2vram为非法值，点击下一步
        next.click()
        time.sleep(1)
        tips5 = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]'
                                                  '/div[2]/div[3]/div[2]/form/div[5]/div/div[3]').text
        if tips5 == '格式不正确。':
            print('\nCases10:\n步骤:内存输入非法值(test)，点击保存。'
                  '\n预期结果:格式不正确。\n实际结果:' + tips5 + '\nPass')
        else:
            print('\nCases10:\n步骤:内存输入非法值(test)，点击保存。'
                  '\n预期结果:格式不正确。\n实际结果:' + tips5 + '\nFail')
        ram = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]'
                                                '/div[2]/div[3]/div[2]/form/div[5]/div/i').text
        ram = int(re.sub("\\D", "", ram))
        time.sleep(1)
        vram.clear()
        vram.send_keys(int(ram / 100 + 1))  # 5.3vram大于当前剩余数量时，点击下一步
        next.click()
        time.sleep(1)
        tips6 = self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div'
                                                  '[1]/div[2]/div[3]/div[2]/form/div[6]').text
        if tips6 == '内存容量不足':
            print('\nCases11:\n步骤:内存输入大于当前剩余数量时:' + (str(int(ram / 100 + 1))) +'，点击保存。'
                  '\n预期结果:内存容量不足\n实际结果:' + tips6 + '\nPass')
        else:
            print('\nCases11:\n步骤:内存输入大于当前剩余数量时:' + (str(int(ram / 100 + 1))) +'，点击保存。'
                  '\n预期结果:内存容量不足\n实际结果:' + tips6 + '\nFail')
        time.sleep(1)
        vram.clear()
        vram.send_keys('1')  # 输入个合法的值
        time.sleep(1)

        # 6.添加磁盘字段验证
        # 6.1单位为GB时
        vdisk = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[1]/input')
        add1 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/i')
        vcpu.click()
        vcpu.clear()
        vdisk.send_keys(" ")  # 6.1.1磁盘为空时，点击添加
        time.sleep(1)
        add1.click()
        time.sleep(1)
        tips7 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[4]').text
        if tips7 == '请输入正确格式的磁盘容量':
            print('\nCases12:\n步骤:磁盘为空格时,点击添加。'
                  '\n预期结果:请输入正确格式的磁盘容量\n实际结果:' + tips7 + '\nPass')
        else:
            print('\nCases12:\n步骤:磁盘为空格时,点击添加。'
                  '\n预期结果:请输入正确格式的磁盘容量\n实际结果:' + tips7 + '\nFail')
        time.sleep(1)
        vdisk.clear()
        vdisk.send_keys("www")  # 6.1.2磁盘为非法值，点击添加
        add1.click()
        time.sleep(1)
        tips7 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[4]').text
        if tips7 == '请输入正确格式的磁盘容量':
            print('\nCases13:\n步骤:磁盘输入非法值时(www),点击添加。'
                  '\n预期结果:请输入正确格式的磁盘容量\n实际结果:' + tips7 + '\nPass')
        else:
            print('\nCases13:\n步骤:磁盘输入非法值时(www),点击添加。'
                  '\n预期结果:请输入正确格式的磁盘容量\n实际结果:' + tips7 + '\nFail')

        pool = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[9]/div/i')
        pool1 = pool.text
        pool1 = int(re.sub("\D", "", pool1))
        time.sleep(1)
        vdisk.clear()
        vdisk.send_keys(int(pool1 / 100 + 1))  # 6.1.3磁盘大于当前剩余数量时，点击下一步
        add1.click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '超过可用容量，请重新输入':
            print('\nCases14:\n步骤:磁盘输入大于当前剩余数量时:' + (str(int(pool1 / 100 + 1)))+'，点击保存。'
                  '\n预期结果:超过可用容量，请重新输入\n实际结果:' + self.driver.find_element_by_xpath('/html/body/div[2]').text + '\nPass')
        else:
            print('\nCases14:\n步骤:磁盘输入大于当前剩余数量时:' + (str(int(pool1 / 100 + 1)))+'，点击保存。'
                  '\n预期结果:超过可用容量，请重新输入\n实际结果:' + self.driver.find_element_by_xpath('/html/body/div[2]').text + '\nFail')
        time.sleep(1)
        # 6.2单位为MB时
        # self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[2]/div[1]/span/span/i').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()#切换单位为MB
        # time.sleep(1)
        # vcpu.click()
        # vcpu.clear()
        # vdisk.send_keys(" ")# 6.2.1磁盘为空时，点击添加
        # time.sleep(1)
        # add1.click()
        # time.sleep(1)
        # tips7 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[4]').text
        # print("MB磁盘为空时点击添加，系统提示:" + tips7)
        # time.sleep(1)
        # vdisk.clear()
        # vdisk.send_keys("www")  # 6.2.2磁盘为非法值，点击添加
        # add1.click()
        # time.sleep(1)
        # tips7 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[4]').text
        # print("MB磁盘输入非法值时点击添加，系统提示:" + tips7)
        # pool2 = pool.text
        # pool2 = int(re.sub("\D", "",pool2))
        # time.sleep(1)
        # vdisk.clear()
        # vdisk.send_keys(int(pool2/100 + 1))  # 6.2.3磁盘大于当前剩余数量时，点击下一步
        # add1.click()
        # time.sleep(1)
        # print("MB磁盘大于当前剩余数量时，系统提示:" + tips2.text)
        # time.sleep(1)
        # # 6.3单位为TB时
        # self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[2]/div[1]/span/span/i').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]').click()  # 切换单位为TB
        # time.sleep(1)
        # vcpu.click()
        # vcpu.clear()
        # vdisk.send_keys(" ")# 6.3.1磁盘为空时，点击添加
        # time.sleep(1)
        # add1.click()
        # time.sleep(1)
        # tips7 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[4]').text
        # print("TB磁盘为空时点击添加，系统提示:" + tips7)
        # time.sleep(1)
        # vdisk.clear()
        # vdisk.send_keys("www")  # 6.3.2磁盘为非法值，点击添加
        # add1.click()
        # time.sleep(1)
        # tips7 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[4]').text
        # print("TB磁盘输入非法值时点击添加，系统提示:" + tips7)
        # pool3 = pool.text
        # pool3 = int(re.sub("\D", "", pool3))
        # time.sleep(1)
        # vdisk.clear()
        # vdisk.send_keys(int(pool3/100 + 1))  # 6.3.3磁盘大于当前剩余数量时，点击下一步
        # add1.click()
        # time.sleep(1)
        # print("TB磁盘大于当前剩余数量时，系统提示:" + tips2.text)
        # 6.4磁盘添加/删除验证
        # self.driver.find_element_by_xpath('//*[@id="createVirtual"]/div[2]/div/div[2]/div[1]/div[2]/div'
        #                                   '[3]/div[2]/form/div[9]/div/div[2]/div/input').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]').click()  # 切换单位为GB
        time.sleep(2)
        vdisk.clear()
        vdisk.send_keys("1")
        add1.click()
        add1.click()
        add1.click()
        add1.click()
        add1.click()
        pool4 = pool.text
        pool4 = int(re.sub("\D", "", pool4))
        if pool1 / 100 - 5 == pool4 / 100:
            print('\nCases15:\n步骤:添加磁盘后验证剩余容量是否正确。\n预期结果:剩余容量正确。\n实际结果:剩余容量正确。\nPass')
        else:
            print('\nCases15:\n步骤:添加磁盘后验证剩余容量是否正确。\n预期结果:剩余容量正确。\n实际结果:剩余容量错误。\nFail')
        time.sleep(1)
        add1.click()  # 第6次添加，会有系统提示
        time.sleep(1)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '最多一次可添加5个磁盘':
            print('\nCases16:\n步骤:同时添加6块磁盘，查看系统响应。'
                  '\n预期结果:最多一次可添加5个磁盘\n实际结果:' + self.driver.find_element_by_xpath('/html/body/div[2]').text + '\nPass')
        else:
            print('\nCases16:\n步骤:同时添加6块磁盘，查看系统响应。'
                  '\n预期结果:最多一次可添加5个磁盘\n实际结果:' + self.driver.find_element_by_xpath('/html/body/div[2]').text + '\nFail')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[13]/i').click()  # 删除按钮
        time.sleep(1)
        pool5 = pool.text
        pool5 = int(re.sub('\D', '', pool5))
        if pool4 / 100 + 1 == pool5 / 100:
            print('\nCases17:\n步骤:删除磁盘后，验证容量是否回退。\n预期结果:容量回退成功。\n实际结果:容量回退成功。\nPass')
        else:
            print('\nCases17:\n步骤:删除磁盘后，验证容量是否回退。\n预期结果:容量回退成功。\n实际结果:容量回退失败。\nFail')
        time.sleep(1)
        share = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[10]/div/div[3]')  # 共享按钮
        share.click()
        time.sleep(1)
        if share.text == "共享":
            print('\nCases18:\n步骤:点击开启磁盘共享功能。\n预期结果:共享磁盘开启成功。\n实际结果:共享磁盘开启成功。\nPass')
        else:
            print('\nCases18:\n步骤:点击开启磁盘共享功能。\n预期结果:共享磁盘开启成功。\n实际结果:共享磁盘开启失败。\nFail')
        # 7.网络接口字段验证
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[13]/i').click()  # 删除所有磁盘
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[13]/i').click()
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[13]/i').click()
        self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[13]/i').click()
        time.sleep(1)
        vlan = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[13]/div/div[2]/div[1]/input')
        add2 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[13]/div/div[2]/div[2]/i')
        vlan.click()
        vlan.clear()
        vlan.send_keys("h@#asd")  # 7.1vlan为非法值，点击添加
        add2.click()
        time.sleep(1)
        tips8 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[14]').text
        if tips8 == '输入的数字范围在0-4095之间':
            print('\nCases19:\n步骤:vlan输入非法值时(h@#asd),点击添加。'
                  '\n预期结果:输入的数字范围在0-4095之间\n实际结果:' + tips8 + '\nPass')
        else:
            print('\nCases19:\n步骤:vlan输入非法值时(h@#asd),点击添加。'
                  '\n预期结果:输入的数字范围在0-4095之间\n实际结果:' + tips8 + '\nFail')
        vlan.clear()
        vlan.send_keys("4096")  # 7.2vlan输入范围外的值，点击添加
        add2.click()
        time.sleep(1)
        tips8 = self.driver.find_element_by_xpath('//*[@id="test_cIList"]/div[14]').text
        if tips8 == '输入的数字范围在0-4095之间':
            print('\nCases20:\n步骤:vlan输入超出范围的值(4096),点击添加。'
                  '\n预期结果:输入的数字范围在0-4095之间\n实际结果:' + tips8 + '\nPass')
        else:
            print('\nCases20:\n步骤:vlan输入超出范围的值(4096),点击添加。'
                  '\n预期结果:输入的数字范围在0-4095之间\n实际结果:' + tips8 + '\nFail')
        vlan.clear()
        vlan.send_keys("500")  # 合理的值
        add2.click()
        time.sleep(1)
        share.click()
        time.sleep(1)
        add1.click()
        time.sleep(1)  # 添加非共享磁盘
        next.click()
        time.sleep(2)

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

        next.click()  # 点击创建
        time.sleep(15)
        # 验证虚拟机是否创建成功
        if self.driver.find_element_by_xpath('//*[@id="test_vTab"]/div[3]/table/'
                                             'tbody/tr[1]/td[2]/div/div/span').text == "Test" + str(num):
            print('\nCases21:\n步骤:不选择ISO新建虚拟机，虚拟机配置如下:'
                  '\n<虚拟机名称>' + vm_name +
                  '\n<运行主机>' + running_host +
                  '\n<vCPU>' + v_cpu +
                  '\n<内存>' + memory +
                  '\n<声卡>' + sound_card +
                  '\n<磁盘>' + disk +
                  '\n<网络接口>' + network_interface +
                  '\n<系统版本>'+ system_version +
                  '\n<系统系列>' + system_family +
                  '\n预期结果:虚拟机创建成功。\n实际结果:虚拟机创建成功。\nPass')
        else:
            print('\nCases21:\n步骤:不选择ISO新建虚拟机，虚拟机配置如下:'
                  '\n<虚拟机名称>' + vm_name +
                  '\n<运行主机>' + running_host +
                  '\n<Vcpu>' + v_cpu +
                  '\n<内存>' + memory +
                  '\n<声卡>' + sound_card +
                  '\n<磁盘>' + disk +
                  '\n<网络接口>' + network_interface +
                  '\n<系统版本>' + system_version +
                  '\n<系统系列>' + system_family +
                  '\n预期结果:虚拟机创建成功。\n实际结果:虚拟机创建失败。\nFail')

        # 创建虚拟机模板
        self.driver.find_element_by_xpath(
            '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()
        time.sleep(6)
