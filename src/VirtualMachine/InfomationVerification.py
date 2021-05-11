import re
import time

from xc_automation_test.src import base


class InfomationVerification(base.NovaBase):

    def test_Virtual_machine_infomation_verification(self):
        '''硬盘、网卡、快照、光驱、虚拟机配置信息'''
        self.driver.find_element_by_xpath('//*[@id="test_health1"]/div[3]/div[2]/div[2]').click()
        time.sleep(3)  # 跳转虚拟机页面
        '''1.虚拟机硬盘'''
        diskname = self.driver.find_element_by_xpath('//*[@id="test_vTab"]/div[3]/table/tbody'
                                                     '/tr[1]/td[2]/div/div/span').text  # 虚拟机名称
        diskram = self.driver.find_element_by_xpath('//*[@id="test_vTab"]'
                                                    '/div[3]/table/tbody/tr[1]/td[5]/div').text
        diskram = int(re.sub("\D", "", diskram))  # 取出总磁盘容量
        # 1.1判断磁盘名称回显
        vdiskname = self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]'
                                                      '/div[3]/table/tbody/tr[1]/td[2]/div').text
        if diskname in vdiskname:
            print('\nCases01:\n步骤:验证磁盘名称回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases01:\n步骤:验证磁盘名称回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 1.2判断磁盘容量是否对应
        disks = int(self.driver.find_element_by_xpath('//*[@id="test_vInfo"]'
                                                      '/div[3]/ul/li[3]/span[2]').text)  # 获取磁盘个数
        vdiskram = 0
        for n in range(1, disks + 1):
            a = self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]/div[3]'
                                                  '/table/tbody/tr[' + str(n) + ']/td[3]/div/div/span').text
            a = int(re.sub("\D", "", a))
            vdiskram = a + vdiskram
        if vdiskram == diskram:
            print('\nCases02:\n步骤:验证磁盘总容量回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases02:\n步骤:验证磁盘总容量回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        tips1 = self.driver.find_element_by_xpath('/html/body/div[2]')
        # 滚动条拖动到可见的元素去
        target = self.driver.find_element_by_id("test_vDisk")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[4]/div/ul[1]/li[2]').click()
        time.sleep(1.5)
        if tips1.text == "启动盘顺序及连接状态调整成功":
            print('\nCases03:\n步骤:点击硬盘开启启动盘按钮。\n预期结果:启动盘顺序及连接状态调整成功。'
                  '\n实际结果:启动盘顺序及连接状态调整成功。\nPass')
        else:
            print('\nCases03:\n步骤:点击硬盘开启启动盘按钮。\n预期结果:启动盘顺序及连接状态调整成功。'
                  '\n实际结果:' + tips1.text + '\nPass')
        # 1.5是否开启共享测试
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[4]/div/ul[1]/li[2]').click()  # 关闭启动盘
        time.sleep(1)
        shard = self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]/div[3]'
                                                  '/table/tbody/tr[1]/td[4]/div/ul[1]/li[3]')
        shard.click()
        time.sleep(1.5)
        if tips1.text == "磁盘开启共享成功":
            print('\nCases04:\n步骤:点击磁盘共享按钮。\n预期结果:磁盘开启共享成功。'
                  '\n实际结果:磁盘开启共享成功。\nPass')
        else:
            print('\nCases04:\n步骤:点击磁盘共享按钮。\n预期结果:磁盘开启共享成功。'
                  '\n实际结果:' + tips1.text + '\nPass')
        shard.click()  # 关闭共享
        time.sleep(1)
        # 1.6磁盘扩容
        self.driver.find_element_by_id('test_vDiskAdd').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_DiskAdd"]/div[1]/div/div/div[1]/input').click()
        time.sleep(1.5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(2)
        usable = self.driver.find_element_by_xpath('//*[@id="test_DiskAdd"]/div[2]/div/i').text
        usable = int(float(usable[5:-2]))  # 获取到可用的容量
        self.driver.find_element_by_xpath('//*[@id="test_DiskAddM"]/div[3]/button[1]').click()
        time.sleep(1)
        volume = self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]/div[3]/table/'
                                                   'tbody/tr[1]/td[3]/div/div/span').text
        volume = int(re.sub("\D", "", volume))

        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]/div[3]/table/tbody/tr[1]/'
                                          'td[4]/div/ul[1]/li[4]').click()
        time.sleep(2)
        inputdisk = self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]/div[3]'
                                                      '/table/tbody/tr[1]/td[3]/div/div/div/div[1]/input')
        inputdisk.clear()
        inputdisk.send_keys(' ')  # 磁盘容量为空格
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[4]/div/ul[2]/li[1]').click()
        time.sleep(2)
        if tips1.text == '请输入正确容量':
            print('\nCases05:\n步骤:扩容磁盘为空格时，点击保存。'
                  '\n预期结果:请输入正确容量\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases05:\n步骤:扩容磁盘为空格时，点击保存。'
                  '\n预期结果:请输入正确容量\n实际结果:' + tips1.text + '\nFail')
        time.sleep(1)
        inputdisk.clear()
        inputdisk.send_keys(volume)
        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[4]/div/ul[2]/li[1]').click()
        time.sleep(2)
        if tips1.text == '磁盘容量必须大于原来容量！':
            print('\nCases06:\n步骤:扩容磁盘小于原容量时:' + str(volume) + '，点击保存。'
                  '\n预期结果:磁盘容量必须大于原来容量！\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases06:\n步骤:扩容磁盘小于原容量时:' + str(volume) + '，点击保存。'
                  '\n预期结果:磁盘容量必须大于原来容量！\n实际结果:' + tips1.text + '\nFail')
        inputdisk.clear()
        time.sleep(1)
        inputdisk.send_keys(usable + 100)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[4]/div/ul[2]/li[1]').click()
        time.sleep(2)
        if tips1.text == '磁盘总空间不足！':
            print('\nCases07:\n步骤:扩容磁盘大于总容量时:' + str(usable + 100) + '，点击保存。'
                  '\n预期结果:磁盘总空间不足！\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases07:\n步骤:扩容磁盘大于总容量时:' + str(usable + 100) + '，点击保存。'
                  '\n预期结果:磁盘总空间不足！\n实际结果:' + tips1.text + '\nFail')
        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]/div[3]'
                                          '/table/tbody/tr[1]/td[4]/div/ul[2]/li[2]').click()  # 取消扩容
        # 删除磁盘
        self.driver.find_element_by_xpath('//*[@id="test_vDiskTab"]/div[3]/'
                                          'table/tbody/tr[1]/td[4]/div/ul[1]/li[5]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_DiskDel"]/span[1]/span').click()  # 永久删除
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_DiskDelM"]/div[3]/button[2]').click()
        time.sleep(1)
        if tips1.text == '硬盘删除成功':
            print('\nCases08:\n步骤:点击删除硬盘，点击保存。'
                  '\n预期结果:硬盘删除成功\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases08:\n步骤:点击删除硬盘，点击保存。'
                  '\n预期结果:硬盘删除成功\n实际结果:' + tips1.text + '\nFail')
        # 重新添加回硬盘
        self.driver.find_element_by_id('test_vDiskAdd').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_DiskAdd"]/div[1]/div/div/div[1]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_DiskAdd"]/div[3]/div/div[1]/input').send_keys(1)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_DiskAdd"]/div[3]/div/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_DiskAddM"]/div[3]/button[2]').click()
        time.sleep(2.5)
        if tips1.text == '硬盘添加成功':
            print('\nCases09:\n步骤:添加硬盘(1G)，点击保存。'
                  '\n预期结果:硬盘添加成功\n实际结果:' + tips1.text + '\nPass')
        else:
            print('\nCases09:\n步骤:添加硬盘(1G)，点击保存。'
                  '\n预期结果:硬盘添加成功\n实际结果:' + tips1.text + '\nFail')

        '''2.虚拟网卡'''
        self.driver.refresh()
        time.sleep(2)
        #  滚动条拖动到可见的元素去
        target = self.driver.find_element_by_id("test_vNetCard")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        self.driver.find_element_by_id('test_vNetCard').click()
        time.sleep(1)
        # 开启启动盘测试
        self.driver.find_element_by_xpath(
            '//*[@id="test_vNetCardTab"]/div[3]/table/tbody/tr/td[6]/div/ul/li[2]').click()
        time.sleep(2)
        tips2 = self.driver.find_element_by_xpath('/html/body/div[2]')
        if tips2.text == "启动盘顺序及连接状态调整成功":
            print('\nCases10:\n步骤:点击网卡开启启动盘按钮。\n预期结果:启动盘顺序及连接状态调整成功。'
                  '\n实际结果:启动盘顺序及连接状态调整成功。\nPass')
        else:
            print('\nCases10:\n步骤:点击网卡开启启动盘按钮。\n预期结果:启动盘顺序及连接状态调整成功。'
                  '\n实际结果:' + tips2.text + '\nFail')
        # 连接状态测试
        time.sleep(2)
        net = self.driver.find_element_by_xpath('//*[@id="test_vNetCardTab"]/div[3]/table/tbody/tr/td[6]/div/ul/li[1]')
        net.click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == "":
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/div[2]/div[3]/div[2]/div[3]/div[3]/button[1]').click()  # 取消断开
            time.sleep(1)
        else:
            print("网卡初始状态为断开:" + self.driver.find_element_by_xpath('/html/body/div[2]').text)

        # 删除虚拟网卡
        self.driver.find_element_by_xpath(
            '//*[@id="test_vNetCardTab"]/div[3]/table/tbody/tr/td[6]/div/ul/li[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[2]/div[3]/div[3]/button[2]').click()
        time.sleep(1)
        if tips2.text == '网卡删除成功':
            print('\nCases11:\n步骤:点击删除网卡，点击保存。'
                  '\n预期结果:网卡删除成功\n实际结果:' + tips2.text + '\nPass')
        else:
            print('\nCases11:\n步骤:点击删除网卡，点击保存。'
                  '\n预期结果:网卡删除成功\n实际结果:' + tips2.text + '\nFail')
        # 添加网卡
        self.driver.find_element_by_id('test_vNetCardAdd').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_NetCard"]/div[1]/div/div/div[1]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_NetCard"]/div[2]/div/div[1]/div/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_NetCard"]/div[2]/div/div[2]/div[1]/input').send_keys(1)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_NetCard"]/div[2]/div/div[2]/div[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_NetCardM"]/div[3]/button[2]').click()  # 点击添加
        time.sleep(2)
        if tips2.text == '添加网卡成功':
            print('\nCases12:\n步骤:添加网卡(vlan:1)，点击保存。'
                  '\n预期结果:添加网卡成功\n实际结果:' + tips2.text + '\nPass')
        else:
            print('\nCases12:\n步骤:添加网卡(vlan:1)，点击保存。'
                  '\n预期结果:添加网卡成功\n实际结果:' + tips2.text + '\nFail')

        '''3.快照'''
        self.driver.refresh()
        time.sleep(2)
        #  滚动条拖动到可见的元素去
        target = self.driver.find_element_by_id("test_vSnapShoot")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        self.driver.find_element_by_id('test_vSnapShoot').click()
        # 添加快照
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_vSnapShootTab"]'
                                          '/div[3]/table/tbody/tr/td[1]/div/label/span/span').click()
        time.sleep(1)
        self.driver.find_element_by_id('test_vSnapShootAdd').click()  # 点击添加
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_SnapShootCheck"]/span[1]').click()  # 取消自动命名
        time.sleep(1)
        # 名称输入为空
        if self.driver.find_element_by_xpath('//*[@id="test_SnapShootName"]'
                                                               '/div/div/div[2]').text == '请输入快照名称。':
            print('\nCases13:\n步骤:快照名称输入为空，点击保存。\n预期结果:请输入快照名称。\n实际结果:请输入快照名称。\nPass')
        else:
            print('\nCases13:\n步骤:快照名称输入为空，点击保存。'
                  '\n预期结果:请输入快照名称。\n实际结果:' + self.driver.find_element_by_xpath('//*[@id="test_SnapShootName"]'
                                                               '/div/div/div[2]').text + '\nPass')
        # 输入33个字符
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_SnapShootName"]/div/div/div[1]'
                                          '/input').send_keys('123456789123456789123456789123456')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_SnapShootM"]/div[3]/button[2]').click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="test_SnapShootName"]'
                                                               '/div/div/div[2]').text == '请输入正确的快照名称':
            print('\nCases14:\n步骤:快照名称超出限制后(123456789123456789123456789123456)，点击保存。\n预期结果:请输入正确的快照名称。'
                  '\n实际结果:请输入正确的快照名称。\nPass')
        else:
            print('\nCases14:\n步骤:快照名称超出限制后(123456789123456789123456789123456)，点击保存。'
                  '\n预期结果:请输入正确的快照名称。\n实际结果:' + self.driver.find_element_by_xpath('//*[@id="test_SnapShootName"]'
                                                               '/div/div/div[2]').text + '\nFail')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_SnapShootName"]/div/div/div[1]'
                                          '/input').clear()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_SnapShootName"]/div/div/div[1]'
                                          '/input').send_keys("No1")
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_SnapShootM"]/div[3]/button[2]').click()
        time.sleep(10)
        if self.driver.find_element_by_xpath(
                '//*[@id="test_vSnapShootTab"]/div[3]/table/tbody/tr/td[4]/div').text == '1':
            print('\nCases15:\n步骤:输入正确的名称(No1)，点击创建。\n预期结果:快照创建成功。\n实际结果:快照创建成功。\nPass')
        else:
            print('\nCases15:\n步骤:输入正确的名称(No1)，点击创建。\n预期结果:快照创建成功。\n实际结果:快照创建失败。\nFail')
        # 快照回滚
        self.driver.find_element_by_xpath(
            '//*[@id="test_vSnapShootTab"]/''div[3]/table/tbody/tr/td[2]/div/div').click()  # 展开快照
        time.sleep(2)
        ID = self.driver.find_element_by_xpath(
            '//*[@id="test_vSnapShootTab"]/div[3]/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr/td[1]/div').text
        self.driver.find_element_by_xpath('//*[@id="test_vSnapShootTab"]/div[3]'
                                          '/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr/td[5]/div/ul/li[1]').click()  # 回滚
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/'
                                          'div[3]/div[2]/div[3]/div[3]/button[2]').click()  # 点击确认
        time.sleep(5)
        now_id = self.driver.find_element_by_xpath(
            '//*[@id="test_vSnapShootTab"]/div[3]/table/tbody/tr[1]/td[5]/div').text
        if ID == now_id:
            print('\nCases16:\n步骤:点击快照回滚。\n预期结果:回滚成功。\n实际结果:回滚成功。\nPass')
        else:
            print('\nCases16:\n步骤:点击快照回滚。\n预期结果:回滚成功。\n实际结果:回滚失败。\nFail')

        # 删除快照
        self.driver.find_element_by_xpath('//*[@id="test_vSnapShootTab"]/'
                                          'div[3]/table/tbody/tr[1]/td[2]/div/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="test_vSnapShootTab"]/div[3]/table/tbody/tr[2]/td/div/div/div[3]/table/tbody/tr/td[5]/div/ul/li[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]'
                                          '/div[3]/div[2]/div[3]/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '快照删除成功':
            print('\nCases17:\n步骤:删除快照。\n预期结果:删除成功。\n实际结果:删除成功。\nPass')
        else:
            print('\nCases17:\n步骤:删除快照。\n预期结果:删除成功。\n实际结果:删除失败。\nFail')

        '''4.虚拟光驱'''
        self.driver.refresh()
        time.sleep(2)
        #  滚动条拖动到可见的元素去
        target = self.driver.find_element_by_id("test_vRambo")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        self.driver.find_element_by_id('test_vRambo').click()
        time.sleep(1)
        self.driver.find_element_by_id('test_vRamboAdd').click()  # 添加光驱
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_RamboName"]'
                                          '/div/div/div/div/input').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()  # 选择镜像
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_RamboM"]/div[3]/button[2]').click()
        time.sleep(2)
        tips3 = self.driver.find_element_by_xpath('/html/body/div[2]')
        if tips3.text == '光驱添加成功':
            print('\nCases18:\n步骤:选择镜像并点击添加光驱。\n预期结果:光驱添加成功。\n实际结果:光驱添加成功。\nPass')
        else:
            print('\nCases18:\n步骤:选择镜像并点击添加光驱。\n预期结果:光驱添加成功。\n实际结果:光驱添加失败。\nFail')
        # 弹出光驱
        self.driver.find_element_by_xpath('//*[@id="test_vRamboTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[3]/div/ul/li[1]').click()
        time.sleep(1)
        if tips3.text == '弹出光盘镜像成功':
            print('\nCases19:\n步骤:点击弹出ISO。\n预期结果:弹出光盘镜像成功。\n实际结果:弹出光盘镜像成功。\nPass')
        else:
            print('\nCases19:\n步骤:点击弹出ISO。\n预期结果:弹出光盘镜像成功。\n实际结果:弹出光盘镜像失败。\nFail')
        # 更换iso
        self.driver.find_element_by_xpath('//*[@id="test_vRamboTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[3]/div/ul/li[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_RamboChangeName"]'
                                          '/div/div/div/div/input').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()  # 选择镜像
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_RamboChangeM"]/div[3]/button[2]').click()
        time.sleep(2)
        if tips3.text == '更换光盘镜像成功':
            print('\nCases20:\n步骤:点击更换ISO。\n预期结果:更换光盘镜像成功。\n实际结果:更换光盘镜像成功。\nPass')
        else:
            print('\nCases20:\n步骤:点击更换ISO。\n预期结果:更换光盘镜像成功。\n实际结果:更换光盘镜像失败。\nFail')
        # 开启启动盘
        self.driver.find_element_by_xpath('//*[@id="test_vRamboTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[3]/div/ul/li[3]').click()
        time.sleep(2)
        if tips3.text == '启动盘顺序及连接状态调整成功':
            print('\nCases21:\n步骤:点击开启光驱启动盘。'
                  '\n预期结果:启动盘顺序及连接状态调整成功。\n实际结果:启动盘顺序及连接状态调整成功。\nPass')
        else:
            print('\nCases21:\n步骤:点击开启光驱启动盘。'
                  '\n预期结果:启动盘顺序及连接状态调整成功。\n实际结果:启动盘顺序及连接状态调整失败。\nFail')
        # 删除镜像启动盘
        self.driver.find_element_by_xpath('//*[@id="test_vRamboTab"]'
                                          '/div[3]/table/tbody/tr[1]/td[3]/div/ul/li[4]').click()  # 点击删除
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]'
                                          '/div[2]/div[3]/div[2]/div[3]/div[3]/button[2]').click()
        time.sleep(1)
        if tips3.text == '光驱删除成功':
            print('\nCases22:\n步骤:点击删除光驱。'
                  '\n预期结果:光驱删除成功。\n实际结果:光驱删除成功。\nPass')
        else:
            print('\nCases22:\n步骤:点击删除光驱。'
                  '\n预期结果:光驱删除成功。\n实际结果:光驱删除失败。\nFail')

        '''服务器信息及虚拟机配置'''
        # 1.服务器信息
        self.driver.refresh()
        time.sleep(2)
        #  滚动条拖动到可见的元素去
        target = self.driver.find_element_by_id("test_vDisk")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        hostname = self.driver.find_element_by_xpath('//*[@id="test_vTab"]/'
                                                     'div[3]/table/tbody/tr[1]/td[6]/div').text
        vhostname = self.driver.find_element_by_xpath('//*[@id="test_vInfo"]'
                                                      '/div[2]/ul/li[1]/span[2]').text
        if hostname == vhostname:
            print('\nCases23:\n步骤:验证所属主机名回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases23:\n步骤:验证所属主机名回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 2.虚拟机系统配置
        # 2.1磁盘个数
        time.sleep(1)
        disk = self.driver.find_elements_by_xpath('//*[@id="test_vDiskTab"]/div[3]/table/tbody/tr')
        disk = int(len(disk))
        vdisk = int(self.driver.find_element_by_xpath('//*[@id="test_vInfo"]'
                                                      '/div[3]/ul/li[3]/span[2]').text)
        if disk == vdisk:
            print('\nCases24:\n步骤:验证磁盘个数回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases24:\n步骤:验证磁盘个数回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 2.2网卡个数
        time.sleep(1)
        self.driver.find_element_by_id('test_vNetCard').click()
        time.sleep(1)
        netcard = self.driver.find_elements_by_xpath('//*[@id="test_vNetCardTab"]/div[3]/table/tbody/tr')
        netcard = int(len(netcard))
        vnetcard = int(self.driver.find_element_by_xpath('//*[@id="test_vInfo"]'
                                                         '/div[3]/ul/li[2]/span[2]').text)
        if netcard == vnetcard:
            print('\nCases25:\n步骤:验证网卡个数回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases25:\n步骤:验证网卡个数回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 2.快照个数
        time.sleep(1)
        self.driver.find_element_by_id('test_vSnapShoot').click()
        time.sleep(1)
        span = int(self.driver.find_element_by_xpath('//*[@id="test_vInfo"]'
                                                     '/div[3]/ul/li[1]/span[2]').text)
        vspan = 0
        for n in range(1, disk + 1):
            b = int(self.driver.find_element_by_xpath('//*[@id="test_vSnapShootTab"]'
                                                      '/div[3]/table/tbody/tr[' + str(n) + ']/td[4]/div').text)
            vspan = b + vspan
        if vspan == span:
            print('\nCases26:\n步骤:验证快照个数回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases26:\n步骤:验证快照个数回显是否正确。'
                  '\n预期结果:回显正确。\n实际结果:回显错误。\nPass')
