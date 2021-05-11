import time
import random

from xc_automation_test.src import base
#from selenium.common import exceptions as selenium_e
from selenium.common.exceptions import NoSuchElementException



class StorageDetails(base.NovaBase):

    def test_storage_details(self):
        allram = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                   'div[2]/div[3]/div[3]/div[3]/div/div[3]/p').text
        useram = self.driver.find_element_by_xpath('//*[@id="r_content"]/'
                                                   'div[2]/div[3]/div[3]/div[4]/div/div[3]/p').text
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/div[2]/div[3]/div[2]/div[2]/span').click()
        time.sleep(4)
        # 存储详情
        useram2 = self.driver.find_element_by_xpath('//*[@id="test_pool_01"]/div[3]/table/tbody/tr/td[2]/div').text
        if useram2 in useram:
            print('\nCases01:\n步骤:验证用户总容量回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases01:\n步骤:验证用户总容量回显。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 跳转告警
        self.driver.find_element_by_xpath('//*[@id="test_pool_01"]/'
                                          'div[3]/table/tbody/tr/td[8]/div/ul/li[1]').click()
        time.sleep(1)
        title = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[1]/div/span[2]/span[1]').text
        if title == '事件和告警':
            print('\nCases02:\n步骤:验证跳转告警功能。\n预期结果:跳转成功。\n实际结果:跳转成功。\nPass')
        else:
            print('\nCases02:\n步骤:验证跳转告警功能。\n预期结果:跳转成功。\n实际结果:跳转失败。\nFail')
        self.driver.back()
        time.sleep(2.5)
        # 跳转事件
        self.driver.find_element_by_xpath('//*[@id="test_pool_01"]/div[3]/table/tbody/tr/td[8]/div/ul/li[2]').click()
        time.sleep(1)
        title2 = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[1]/div/span[2]/span[1]').text
        if title2 == '事件和告警':
            print('\nCases03:\n步骤:验证跳转事件功能。\n预期结果:跳转成功。\n实际结果:跳转成功。\nPass')
        else:
            print('\nCases03:\n步骤:验证跳转事件功能。\n预期结果:跳转成功。\n实际结果:跳转失败。\nFail')
        self.driver.back()
        time.sleep(2.5)
        # 跳转任务
        self.driver.find_element_by_xpath('//*[@id="test_pool_01"]/div[3]/table/tbody/tr/td[8]/div/ul/li[3]').click()
        time.sleep(1)
        title3 = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[1]/div/span[2]/span[1]').text
        if title3 == '任务':
            print('\nCases04:\n步骤:验证跳转任务功能。\n预期结果:跳转成功。\n实际结果:跳转成功。\nPass')
        else:
            print('\nCases04:\n步骤:验证跳转任务功能。\n预期结果:跳转成功。\n实际结果:跳转失败。\nFail')
        self.driver.back()
        time.sleep(2.5)
        # 存储池属性
        name1 = self.driver.find_element_by_xpath('//*[@id="test_pool_01"]/div[3]/table/tbody/tr/td[1]/div').text
        name2 = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[2]/div[3]/div[1]/div[2]/ul/li[1]/span[2]').text
        allram2 = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[2]/div[3]/div[1]/div[2]/ul/li[2]/span[2]').text
        if name1 == name2 and allram2 in allram:
            print('\nCases05:\n步骤:验证存储池信息回显。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases05:\n步骤:验证存储池信息回显。\n预期结果:回显正确。\n实际结果:回显失败。\nFail')
        time.sleep(2)

        # 视图模块
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_id('test_view_btn01').click()
        time.sleep(1)
        # 1.nfs视图
        self.driver.find_element_by_id('test_create_btn01').click()
        time.sleep(2)
        num1 = random.randint(0, 999)
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div[2]/div/form/div[2]/div/div/div/input').send_keys('nfs' + str(num1))
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 添加nfs视图
        time.sleep(15)
        if self.driver.find_element_by_xpath(
                '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').text == 'nfs' + str(num1):
            print('\nCases06:\n步骤:添加nfs视图(名称:nfs' + str(num1) + ')。\n预期结果:新建成功。\n实际结果:新建成功。\nPass')
        else:
            print('\nCases06:\n步骤:添加nfs视图(名称:nfs' + str(num1) + ')。\n预期结果:新建成功。\n实际结果:新建失败。\nFail')
        self.driver.find_element_by_xpath(
            '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[1]/div/label/span').click()
        self.driver.find_element_by_id('test_del_btn01').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div[4]/button[2]').click()  # 删除nfs视图
        time.sleep(5)
        try:
            assert self.driver.find_element_by_xpath(
                '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').is_displayed()
            if self.driver.find_element_by_xpath(
                    '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').text == 'nfs' + str(num1):
                print('\nCases07:\n步骤:删除nfs视图。\n预期结果:删除成功。\n实际结果:删除失败。\nFail')
            else:
                print('\nCases07:\n步骤:删除nfs视图。\n预期结果:删除成功。\n实际结果:删除成功。\nPass')
        except NoSuchElementException:
            print('\nCases07:\n步骤:删除nfs视图。\n预期结果:删除成功。\n实际结果:删除成功。\nPass')

        # 2.sam视图
        self.driver.find_element_by_id('test_create_btn01').click()
        time.sleep(2)
        num2 = random.randint(0, 999)
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div[2]/div/form/div[2]/div/div/div/input').send_keys('sam' + str(num2))
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div[2]/div/form/div[5]/div/div/label[2]/span[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 添加sam视图
        time.sleep(8)
        if self.driver.find_element_by_xpath(
                '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').text == 'sam' + str(num2):
            print('\nCases08:\n步骤:添加sam视图(名称:sam' + str(num2) + ')。\n预期结果:新建成功。\n实际结果:新建成功。\nPass')
        else:
            print('\nCases08:\n步骤:添加sam视图(名称:sam' + str(num2) + ')。\n预期结果:新建成功。\n实际结果:新建失败。\nFail')
        self.driver.find_element_by_xpath(
            '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[1]/div/label/span').click()
        self.driver.find_element_by_id('test_del_btn01').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[1]/div[2]/label/span[1]').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 物理删除sam视图
        time.sleep(5)
        try:
            assert self.driver.find_element_by_xpath(
                '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').is_displayed()
            if self.driver.find_element_by_xpath(
                    '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').text == 'sam' + str(num2):
                print('\nCases09:\n步骤:物理删除sam视图。\n预期结果:物理删除成功。\n实际结果:物理删除失败。\nFail')
            else:
                print('\nCases09:\n步骤:物理删除sam视图。\n预期结果:物理删除成功。\n实际结果:物理删除成功。\nPass')
        except NoSuchElementException:
            print('\nCases09:\n步骤:物理删除sam视图。\n预期结果:物理删除成功。\n实际结果:物理删除成功。\nPass')

        self.driver.find_element_by_id('test_create_btn01').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div[2]/div/form/div[2]/div/div/div/input').send_keys('sam' + str(num2))
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div[2]/div/form/div[5]/div/div/label[2]/span[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 添加sam视图
        time.sleep(8)
        self.driver.find_element_by_xpath(
            '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[1]/div/label/span').click()
        self.driver.find_element_by_id('test_del_btn01').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/button[2]').click()  # 逻辑删除sam视图
        time.sleep(5)
        try:
            assert self.driver.find_element_by_xpath(
                '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').is_displayed()
            if self.driver.find_element_by_xpath(
                    '//*[@id="test_view_con01"]/div[3]/table/tbody/tr/td[2]/div').text == 'sam' + str(num2):
                print('\nCases10:\n步骤:逻辑删除sam视图。\n预期结果:逻辑删除成功。\n实际结果:逻辑删除失败。\nFail')
            else:
                print('\nCases10:\n步骤:逻辑删除sam视图。\n预期结果:逻辑删除成功。\n实际结果:逻辑删除成功。\nPass')
        except NoSuchElementException:
            print('\nCases10:\n步骤:逻辑删除sam视图。\n预期结果:逻辑删除成功。\n实际结果:逻辑删除成功。\nPass')

        # ISCSI模块
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_id('test_iscsi_btn01').click()
        time.sleep(1)
        # 添加客户端
        self.driver.find_element_by_id('test_i_create01').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/form/div[2]/div/label/span[1]').click()
        time.sleep(1)
        num = random.randint(1, 9)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys(num)  # 名称尾部输入个随机数
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/form/div[6]/div/div/div/label/span[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[2]/div/form/div[7]/div/div/div[2]/input').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/form/div[8]/div/div/div[1]/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/button[2]').click()  # 点击添加客户端
        time.sleep(20)
        lastname = self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[1]/td[3]/div/div').text
        if int(lastname[-1]) == num:
            print('\nCases11:\n步骤:新建iscsi客户端，名称随机。\n预期结果:新建成功。\n实际结果:新建成功。\nPass')
        else:
            print('\nCases11:\n步骤:新建iscsi客户端，名称随机。\n预期结果:新建成功。\n实际结果:新建失败。\nFail')
        # 添加/编辑/删除共享卷
        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[1]/div/label/span').click()
        self.driver.find_element_by_xpath('//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[2]/div/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[1]/td[10]/div/div/p/i').click()  # 点击添加
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="addClient"]/div[1]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('10000')
        self.driver.find_element_by_xpath('//*[@id="addClient"]/div[1]/div[2]/div/div[1]/div/i').click()
        self.driver.find_element_by_xpath('//*[@id="addClient"]/div[1]/div[3]/button[2]').click()  # 添加共享卷
        time.sleep(25)  # 虚拟机环境添加较慢

        if self.driver.find_element_by_xpath(
                '//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[7]/div/div').text == '1':
            print('\nCases12:\n步骤:添加共享卷(1000MB)。\n预期结果:新建成功。\n实际结果:新建成功。\nPass')
        else:
            print('\nCases12:\n步骤:添加共享卷(1000MB)。\n预期结果:新建成功。\n实际结果:新建失败。\nFail')

        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[1]/div/label/span').click()
        self.driver.find_element_by_xpath('//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[2]/div/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[2]/td/div'
            '/div/div[3]/table/tbody/tr/td[7]/div/div[1]/p[2]/i').click()  # 点击编辑共享卷

        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[2]'
            '/td/div/div/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input').clear()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[2]/td/div/'
            'div/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input').send_keys('10.9')
        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[2]/td/div/div/'
            'div[3]/table/tbody/tr/td[7]/div/div[2]/p[1]').click()  # 保存编辑
        time.sleep(15)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_id('test_iscsi_btn01').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[1]/div/label/span').click()
        self.driver.find_element_by_xpath('//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[2]/div/div').click()
        time.sleep(1)
        if (self.driver.find_element_by_xpath(
                '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[2]'
                '/td/div/div/div[3]/table/tbody/tr/td[3]/div/div/span').text)[0:-2] == str(10.9):
            print('\nCases13:\n步骤:编辑共享卷(1000MB>10.9GB)。\n预期结果:编辑成功。\n实际结果:编辑成功。\nPass')
        else:
            print('\nCases13:\n步骤:编辑共享卷(1000MB>10.9GB)。\n预期结果:编辑成功。\n实际结果:编辑失败。\nFail')

        self.driver.find_element_by_xpath('//*[@id="test_share_con01"]/div[3]/table/tbody/tr[2]/'
                                          'td/div/div/div[3]/table/tbody/tr/td[7]/div/div[1]/p[1]/i').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/button[2]').click()
        time.sleep(20)
        if self.driver.find_element_by_xpath(
                '//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[7]/div/div').text == '0':
            print('\nCases14:\n步骤:删除共享卷。\n预期结果:删除成功。\n实际结果:删除成功。\nPass')
        else:
            print('\nCases14:\n步骤:删除共享卷。\n预期结果:删除成功。\n实际结果:删除失败。\nFail')

        self.driver.find_element_by_xpath(
            '//*[@id="test_share_con01"]/div[3]/table/tbody/tr/td[1]/div/label/span').click()
        self.driver.find_element_by_id('test_i_del01').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/button[2]').click()
        time.sleep(8)

        try:
            assert self.driver.find_element_by_xpath(
                '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[1]/td[3]/div/div').is_displayed()
            if self.driver.find_element_by_xpath(
                    '//*[@id="test_share_con01"]/div[3]/table/tbody/tr[1]/td[3]/div/div').text == lastname:
                print('\nCases15:\n步骤:删除客户端。\n预期结果:删除成功。\n实际结果:删除失败。\nFail')
            else:
                print('\nCases15:\n步骤:删除客户端。\n预期结果:删除成功。\n实际结果:删除成功。\nPass')
        except NoSuchElementException:
            print('\nCases15:\n步骤:删除客户端。\n预期结果:删除成功。\n实际结果:删除成功。\nPass')