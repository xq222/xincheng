import time
import random

from xc_automation_test.src import base


class MutexOperation(base.NovaBase):

    def test_Virtual_machine_mutex_operation(self):
        '''虚拟机操作'''
        self.driver.find_element_by_xpath('//*[@id="test_health1"]/div[3]/div[2]/div[2]').click()
        time.sleep(4)  # 跳转虚拟机页面
        # 1.虚拟机开机/关机/互斥
        self.driver.find_element_by_xpath(
            '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[1]').click()  # 开机第一台虚拟机
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 确认开机
        time.sleep(5)
        tips = self.driver.find_element_by_xpath('/html/body/div[2]')
        # 1.1互斥
        self.driver.find_element_by_xpath(
            '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[2]').click()  # 开机状态下编辑虚拟机
        time.sleep(1)
        if tips.text == '':
            print('\nCases01\n步骤:点击虚拟机开机按钮。\n预期结果:虚拟机开机成功。\n实际结果:虚拟机开机失败。\nFail')
            # 关机下的操作
            # 1.2编辑虚拟机
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').clear()
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').send_keys(' ')  # 名称为空
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(1)
            if tips.text == '名称格式不正确':
                print('\nCases06\n步骤:编辑虚拟机，虚拟机名称为空。\n预期结果:名称格式不正确\n实际结果:名称格式不正确\nPass')
            else:
                print('\nCases06\n步骤:编辑虚拟机，虚拟机名称为空。\n预期结果:名称格式不正确\n实际结果:操作失败\nFail')
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').clear()
            num = random.randint(0, 999)
            # 名称输入含有中文的随机数
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').send_keys('虚拟机' + str(num))
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').clear()
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').send_keys(' ')  # cpu为空
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(1)
            if tips.text == 'vCPU格式不正确':
                print('\nCases07\n步骤:编辑虚拟机，vCPU为空。\n预期结果:vCPU格式不正确\n实际结果:vCPU格式不正确\nPass')
            else:
                print('\nCases07\n步骤:编辑虚拟机，vCPU为空。\n预期结果:vCPU格式不正确\n实际结果:操作失败\nFail')
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').clear()
            num2 = random.randint(1, 3)
            self.driver.find_element_by_xpath(  # 输入随机cpu
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').send_keys(num2)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').clear()
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').send_keys(' ')  # 内存为空
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(1)
            if tips.text == '内存格式不正确':
                print('\nCases08\n步骤:编辑虚拟机，内存为空。\n预期结果:内存格式不正确\n实际结果:内存格式不正确\nPass')
            else:
                print('\nCases08\n步骤:编辑虚拟机，内存为空。\n预期结果:内存格式不正确\n实际结果:操作失败\nFail')
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').clear()
            num3 = random.randint(1, 3)
            self.driver.find_element_by_xpath(  # 输入随机内存
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').send_keys(num3)
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(2)
            if tips.text == '虚拟机配置更新成功':
                print('\nCases09\n步骤:虚拟机正常编辑后，点击保存。\n预期结果:虚拟机配置更新成功\n实际结果:虚拟机配置更新成功\nPass')
            else:
                print('\nCases09\n步骤:虚拟机正常编辑后，点击保存。\n预期结果:虚拟机配置更新成功\n实际结果:保存失败\nFail')
            # 1.3克隆虚拟机
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[4]').click()  # 点击克隆
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vCloneM"]/div[3]/button[2]').click()  # 直接点击保存
            time.sleep(1)
            if self.driver.find_element_by_xpath(
                    '//*[@id="test_vClone"]/div[2]/form/div/div/div[2]').text == '请输入新的虚拟机名称':
                print('\nCases10\n步骤:克隆虚拟机时，虚拟机名称为空时。\n预期结果:请输入新的虚拟机名称\n实际结果:请输入新的虚拟机名称\nPass')
            else:
                print('\nCases10\n步骤:克隆虚拟机时，虚拟机名称为空时。\n预期结果:请输入新的虚拟机名称\n实际结果:操作失败\nFail')

            self.driver.find_element_by_xpath('//*[@id="test_vClone"]/div[2]/form/div/div/div[1]/input') \
                .send_keys(self.driver.find_element_by_xpath('//*[@id="test_vClone"]/div[1]/div[2]').text)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_vCloneM"]/div[3]/button[2]').click()  # 名称重复点击保存
            time.sleep(1)
            if tips.text == '虚拟机名称重复':
                print('\nCases11\n步骤:克隆虚拟机时，虚拟机名称重复时。\n预期结果:虚拟机名称重复\n实际结果:虚拟机名称重复\nPass')
            else:
                print('\nCases11\n步骤:克隆虚拟机时，虚拟机名称重复时。\n预期结果:虚拟机名称重复\n实际结果:操作失败\nFail')
            num4 = random.randint(1, 999)
            self.driver.find_element_by_xpath('//*[@id="test_vClone"]/div[2]/form/div/div/div[1]/input').clear()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vClone"]/div[2]/form/div/div/div[1]/input').send_keys('克隆虚拟机' + str(num4))
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_vCloneM"]/div[3]/button[2]').click()  # 保存
            time.sleep(10)
            self.driver.refresh()
            time.sleep(2)
            VMname = self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/span').text
            if VMname == '克隆虚拟机' + str(num4):
                print('\nCases12\n步骤:新虚拟机名称为:' + '克隆虚拟机' + str(num4) + '\n预期结果:克隆成功\n实际结果:克隆成功\nPass')
            else:
                print('\nCases12\n步骤:新虚拟机名称为:' + '克隆虚拟机' + str(num4) + '\n预期结果:克隆成功\n实际结果:克隆失败或仍在克隆中\nFail')

            # 1.4启动桌面
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[5]').click()
            time.sleep(1)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '此虚拟机已关闭！请开机！':
                print('\nCases13\n步骤:虚拟机关闭时点击启动桌面按钮。\n预期结果:此虚拟机已关闭！请开机！\n实际结果:此虚拟机已关闭！请开机！\nPass')
            else:
                print('\nCases13\n步骤:虚拟机关闭时点击启动桌面按钮。\n预期结果:此虚拟机已关闭！请开机！\n实际结果:操作失败\nFail')
            # 1.5虚拟机迁移
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[6]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="test_vMig"]/div[3]/form/div[1]/div/div/div/input').click()
            time.sleep(2)
            IPname = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').text
            self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_vMigM"]/div[3]/button[2]').click()  # 迁移
            time.sleep(1)
            a = self.driver.find_element_by_xpath('/html/body/div[2]').text
            time.sleep(3)
            self.driver.refresh()
            time.sleep(2)
            IPname2 = self.driver.find_element_by_xpath('//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[6]/div').text
            if IPname == IPname2:
                print('\nCases14\n步骤:虚拟机关闭时迁移虚拟机。\n预期结果:虚拟机迁移成功\n实际结果:虚拟机迁移成功\nPass')
            else:
                print('\nCases14\n步骤:虚拟机关闭时迁移虚拟机。\n预期结果:虚拟机迁移成功\n实际结果:虚拟机迁移失败\nFail')
            # 1.6导出文件描述
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[8]').click()
            time.sleep(1)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '信息正在收集中！ 稍后将自动开始下载。':
                print('\nCases15\n步骤:虚拟机关闭时点击导出描述文件。\n预期结果:信息正在收集中！ 稍后将自动开始下载。\n实际结果:信息正在收集中！ 稍后将自动开始下载。\nPass')
            else:
                print('\nCases15\n步骤:虚拟机关闭时点击导出描述文件。\n预期结果:信息正在收集中！ 稍后将自动开始下载。\n实际结果:操作失败\nFail')
        else:
            # 开机情况下的操作
            print('\nCases01\n步骤:点击虚拟机开机按钮。\n预期结果:虚拟机开机成功。\n实际结果:虚拟机开机成功。\nPass')

            print('\nCases02\n步骤:虚拟机开机后，点击编辑按钮。\n预期结果:请先关闭虚拟机电源\n实际结果:请先关闭虚拟机电源\nPass')
            time.sleep(4)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[3]').click()  # 开机状态下转换模板
            time.sleep(1)
            if tips.text == '请先关闭虚拟机电源':
                print('\nCases03\n步骤:虚拟机开机后，点击转换模板。\n预期结果:请先关闭虚拟机电源\n实际结果:请先关闭虚拟机电源\nPass')
            else:
                print('\nCases03\n步骤:虚拟机开机后，点击转换模板。\n预期结果:请先关闭虚拟机电源\n实际结果:' + tips.text + '\nFail')
            time.sleep(4)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[7]').click()  # 开机状态下删除虚拟机
            time.sleep(1)
            if tips.text == '请先关闭虚拟机电源':
                print('\nCases04\n步骤:虚拟机开机后，点击删除虚拟机。\n预期结果:请先关闭虚拟机电源\n实际结果:请先关闭虚拟机电源\nPass')
            else:
                print('\nCases04\n步骤:虚拟机开机后，点击删除虚拟机。\n预期结果:请先关闭虚拟机电源\n实际结果:'+ tips.text + '\nFail')
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[1]').click()  # 关机虚拟机
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/div[3]/div[2]/div/div[2]/form/div[2]/div/div/input').send_keys('admin')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 确认关机
            time.sleep(3.5)
            if tips.text == '虚拟机电源关闭成功':
                print('\nCases05\n步骤:点击虚拟机关机按钮。\n预期结果:虚拟机电源关闭成功\n实际结果:虚拟机电源关闭成功\nPass')
            else:
                print('\nCases05\n步骤:点击虚拟机关机按钮。\n预期结果:虚拟机电源关闭成功\n实际结果:'+ tips.text + '\nFail')
            # 关机下的操作
            # 1.2编辑虚拟机
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[2]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').clear()
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').send_keys(' ')  # 名称为空
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(1)
            if tips.text == '名称格式不正确':
                print('\nCases06\n步骤:编辑虚拟机，虚拟机名称为空。\n预期结果:名称格式不正确\n实际结果:名称格式不正确\nPass')
            else:
                print('\nCases06\n步骤:编辑虚拟机，虚拟机名称为空。\n预期结果:名称格式不正确\n实际结果:操作失败\nFail')
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').clear()
            num = random.randint(0, 999)
            # 名称输入含有中文的随机数
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').send_keys('虚拟机' + str(num))
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').clear()
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').send_keys(' ')  # cpu为空
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(1)
            if tips.text == 'vCPU格式不正确':
                print('\nCases07\n步骤:编辑虚拟机，vCPU为空。\n预期结果:vCPU格式不正确\n实际结果:vCPU格式不正确\nPass')
            else:
                print('\nCases07\n步骤:编辑虚拟机，vCPU为空。\n预期结果:vCPU格式不正确\n实际结果:操作失败\nFail')
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').clear()
            num2 = random.randint(1, 3)
            self.driver.find_element_by_xpath(  # 输入随机cpu
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input').send_keys(num2)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').clear()
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').send_keys(' ')  # 内存为空
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(1)
            if tips.text == '内存格式不正确':
                print('\nCases08\n步骤:编辑虚拟机，内存为空。\n预期结果:内存格式不正确\n实际结果:内存格式不正确\nPass')
            else:
                print('\nCases08\n步骤:编辑虚拟机，内存为空。\n预期结果:内存格式不正确\n实际结果:操作失败\nFail')
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').clear()
            num3 = random.randint(1, 3)
            self.driver.find_element_by_xpath(  # 输入随机内存
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input').send_keys(num3)
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[2]/li[1]').click()  # 保存
            time.sleep(1)
            if tips.text == '虚拟机配置更新成功':
                print('\nCases09\n步骤:虚拟机正常编辑后，点击保存。\n预期结果:虚拟机配置更新成功\n实际结果:虚拟机配置更新成功\nPass')
            else:
                print('\nCases09\n步骤:虚拟机正常编辑后，点击保存。\n预期结果:虚拟机配置更新成功\n实际结果:保存失败\nFail')

            # 1.3克隆虚拟机
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[4]').click()  # 点击克隆
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vCloneM"]/div[3]/button[2]').click()  # 直接点击保存
            time.sleep(1)
            if self.driver.find_element_by_xpath(
                    '//*[@id="test_vClone"]/div[2]/form/div/div/div[2]').text == '请输入新的虚拟机名称':
                print('\nCases10\n步骤:克隆虚拟机时，虚拟机名称为空时。\n预期结果:请输入新的虚拟机名称\n实际结果:请输入新的虚拟机名称\nPass')
            else:
                print('\nCases10\n步骤:克隆虚拟机时，虚拟机名称为空时。\n预期结果:请输入新的虚拟机名称\n实际结果:操作失败\nFail')

            self.driver.find_element_by_xpath('//*[@id="test_vClone"]/div[2]/form/div/div/div[1]/input') \
                .send_keys(self.driver.find_element_by_xpath('//*[@id="test_vClone"]/div[1]/div[2]').text)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_vCloneM"]/div[3]/button[2]').click()  # 名称重复点击保存
            time.sleep(1)
            if tips.text == '虚拟机名称重复':
                print('\nCases11\n步骤:克隆虚拟机时，虚拟机名称重复时。\n预期结果:虚拟机名称重复\n实际结果:虚拟机名称重复\nPass')
            else:
                print('\nCases11\n步骤:克隆虚拟机时，虚拟机名称重复时。\n预期结果:虚拟机名称重复\n实际结果:操作失败\nFail')
            num4 = random.randint(1, 999)
            self.driver.find_element_by_xpath('//*[@id="test_vClone"]/div[2]/form/div/div/div[1]/input').clear()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="test_vClone"]/div[2]/form/div/div/div[1]/input').send_keys('克隆虚拟机' + str(num4))
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_vCloneM"]/div[3]/button[2]').click()  # 保存
            time.sleep(10)
            self.driver.refresh()
            time.sleep(2)
            VMname = self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/span').text
            if VMname == '克隆虚拟机' + str(num4):
                print('\nCases12\n步骤:新虚拟机名称为:'+'克隆虚拟机' + str(num4) + '\n预期结果:克隆成功\n实际结果:克隆成功\nPass')
            else:
                print('\nCases12\n步骤:新虚拟机名称为:'+'克隆虚拟机' + str(num4) + '\n预期结果:克隆成功\n实际结果:克隆失败或仍在克隆中\nFail')
            # 1.4启动桌面
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[5]').click()
            time.sleep(2)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '此虚拟机已关闭！请开机！':
                print('\nCases13\n步骤:虚拟机关闭时点击启动桌面按钮。\n预期结果:此虚拟机已关闭！请开机！\n实际结果:此虚拟机已关闭！请开机！\nPass')
            else:
                print('\nCases13\n步骤:虚拟机关闭时点击启动桌面按钮。\n预期结果:此虚拟机已关闭！请开机！\n实际结果:操作失败\nFail')
            # 1.5虚拟机迁移
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[6]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="test_vMig"]/div[3]/form/div[1]/div/div/div/input').click()
            time.sleep(2)
            IPname = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').text
            self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_vMigM"]/div[3]/button[2]').click()  # 迁移
            time.sleep(5)
            self.driver.refresh()
            time.sleep(2)
            IPname2 = self.driver.find_element_by_xpath('//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[6]/div').text
            if IPname == IPname2:
                print('\nCases14\n步骤:虚拟机关闭时迁移虚拟机。\n预期结果:虚拟机迁移成功\n实际结果:虚拟机迁移成功\nPass')
            else:
                print('\nCases14\n步骤:虚拟机关闭时迁移虚拟机。\n预期结果:虚拟机迁移成功\n实际结果:虚拟机迁移失败\nFail')
            # 1.6导出文件描述
            self.driver.find_element_by_xpath(
                '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[8]').click()
            time.sleep(1)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '信息正在收集中！ 稍后将自动开始下载。':
                print('\nCases15\n步骤:虚拟机关闭时点击导出描述文件。\n预期结果:信息正在收集中！ 稍后将自动开始下载。\n实际结果:信息正在收集中！ 稍后将自动开始下载。\nPass')
            else:
                print('\nCases15\n步骤:虚拟机关闭时点击导出描述文件。\n预期结果:信息正在收集中！ 稍后将自动开始下载。\n实际结果:操作失败\nFail')
        # 下面删除虚拟机
        time.sleep(1)
        # self.driver.refresh()
        # time.sleep(3)
        # for vm_num in range(1, 5):  # 位置在Splicer-03上面的虚拟机全部删除。
        #     if self.driver.find_element_by_xpath(
        #             '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[2]/div/div/span').text == 'win7':
        #         break
        #     else:
        #         self.driver.find_element_by_xpath(
        #             '//*[@id="test_vTab"]/div[3]/table/tbody/tr[1]/td[10]/div/ul[1]/li[7]').click()  # 点击删除
        #         time.sleep(2)
        #         self.driver.find_element_by_xpath(
        #             '//*[@id="content"]/div[3]/div[2]/div/div[2]/form/div[2]/div/div/input').send_keys('admin')
        #         time.sleep(1)
        #         self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 确认删除
        #         time.sleep(1)
        #         self.driver.find_element_by_xpath('//*[@id="test_vDel"]/span[1]/span').click()  # 勾选永久
        #         time.sleep(1)
        #         self.driver.find_element_by_xpath('//*[@id="test_vDelM"]/div[3]/button[2]').click()  # 最终删除
        #         time.sleep(2)


