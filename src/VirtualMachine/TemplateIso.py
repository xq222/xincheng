import time

from xc_automation_test.src import base


class TemplateIso(base.NovaBase):

    def test_Virtual_machine_template_iso(self):
        '''虚拟机检索、删除模板、镜像操作'''
        self.driver.find_element_by_xpath('//*[@id="test_health1"]/div[3]/div[2]/div[2]').click()
        time.sleep(2)  # 跳转虚拟机页面
        # 检索虚拟机
        self.driver.find_element_by_id('test_vSearch').send_keys('Test')
        time.sleep(2)
        vname = self.driver.find_element_by_xpath('//*[@id="test_vTab"]/div[3]/'
                                                  'table/tbody/tr[1]/td[2]/div/div/span').text
        if 'Test' in vname:
            print('\nCases01:\n步骤:验证检索虚拟机的功能(条件:Test)。\n预期结果:检索成功。\n实际结果:检索成功。\nPass')
        else:
            print('\nCases01:\n步骤:验证检索虚拟机的功能(条件:Test)。\n预期结果:检索成功。\n实际结果:检索失败。\nFail')
        self.driver.refresh()
        time.sleep(2.5)
        # 删除模板
        self.driver.find_element_by_id('template').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="test_temTab"]/div[3]/'
                                          'table/tbody/tr[1]/td[7]/div/ul/li').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]'
                                          '/div[3]/div[3]/button[2]').click()
        time.sleep(2)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '模板删除成功，请查看模板列表':
            print('\nCases02:\n步骤:点击删除虚拟机模板。\n预期结果:模板删除成功，请查看模板列表'
                  '\n实际结果:模板删除成功，请查看模板列表\nPass')
        else:
            print('\nCases02:\n步骤:点击删除虚拟机模板。\n预期结果:模板删除成功，请查看模板列表'
                  '\n实际结果:' + self.driver.find_element_by_xpath('/html/body/div[2]').text + '\nPass')

        # self.driver.refresh()
        # time.sleep(2.5)
        # 编辑、删除镜像
        # self.driver.find_element_by_id('iso').click()
        # time.sleep(3)
        # #编辑
        # self.driver.find_element_by_xpath('//*[@id="test_isoTab"]/div[3]'
        #                                   '/table/tbody/tr[1]/td[8]/div/ul/li[2]').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="test_isoTab"]/div[3]/table/'
        #                                   'tbody/tr[1]/td[4]/div/div/div[1]/input').click()#系统类别下拉框
        # time.sleep(2)
        # self.driver.find_element_by_xpath('/html/body/div[2]/'
        #                                   'div[1]/div[1]/ul/li[1]').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="test_isoTab"]/div[3]/'
        #                                   'table/tbody/tr[1]/td[8]/div/ul/li[1]').click()#1.系统版本为空，直接点击保存
        # time.sleep(1)
        # print('当系统版本为空时:请选择系统版本')
        #
        # self.driver.find_element_by_xpath('//*[@id="test_isoTab"]/div[3]/table/'
        #                                   'tbody/tr[1]/td[5]/div/div/div[1]/span/span/i').click()#版本下拉框
        # time.sleep(2)
        # self.driver.find_element_by_xpath('/html/body/div[4]/'
        #                                   'div[1]/div[1]/ul/li[1]').click()#2.选择系统版本
        # self.driver.find_element_by_xpath('//*[@id="test_isoTab"]/div[3]/'
        #                                   'table/tbody/tr[1]/td[8]/div/ul/li[1]').click()
        # time.sleep(2.5)
        # print(self.driver.find_element_by_xpath('/html/body/div[2]').text)
        # 删除镜像
        # self.driver.find_element_by_xpath('//*[@id="test_isoTab"]/'
        #                                   'div[3]/table/tbody/tr[1]/td[8]/div/ul/li[3]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="content"]/'
        #                                   'div[3]/div[3]/button[2]').click()
        # time.sleep(1.5)
        # print(self.driver.find_element_by_xpath('/html/body/div[2]').text)
