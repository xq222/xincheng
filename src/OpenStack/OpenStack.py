import time
import random




class OpenStack(base.NovaBase):

    def test_openStack(self):
        #生态集成
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[7]/div[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[7]/div[2]/div/div[2]/div/span').click()
        time.sleep(3)
        # 新建pool
        self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]/div/div/div[1]/div/button[1]').click()
        time.sleep(2)
        num2 = random.randint(0, 999)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div/form/div[1]/div/div/input').send_keys(
            'pool' + str(num2))
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div/form/div[2]/div/div/div/input').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[2]/div/form/div[4]/div/div/div[1]/input').send_keys('10')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/button[2]').click()
        time.sleep(15)
        self.driver.refresh()
        time.sleep(2)
        if self.driver.find_element_by_xpath(
                '//*[@id="r_content"]/div[2]/div[2]/div/div/div[2]/div[3]/table/tbody/tr/td[2]/div').text == 'pool' + str(
            num2):
            print('\nCases01:\n步骤:新建pool(10G)，点击保存。\n预期结果:新建成功。\n实际结果:新建成功。\nPass')
        else:
            print('\nCases01:\n步骤:新建pool(10G)，点击保存。\n预期结果:新建成功。\n实际结果:新建失败。\nFail')
        self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[2]/div/div/div[2]/div[3]/table/tbody/tr/td[5]/div/div/i[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/form/div[2]/div/div/input').send_keys(
            'admin')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[2]/label/span[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/button[2]').click()
        time.sleep(2)
        if self.driver.find_element_by_xpath('/html/body/div[3]').text == '删除成功':
            print('\nCases02:\n步骤:删除pool，点击保存。\n预期结果:删除成功。\n实际结果:删除成功。\nPass')

        else:
            print('\nCases02:\n步骤:删除pool，点击保存。\n预期结果:删除成功。\n实际结果:删除失败。\nFail')


