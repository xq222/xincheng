import time

from xc_automation_test.src import base


class Login(base.NovaBase):

    def get_xpath(self):
        self.username = self.driver.find_element_by_xpath('//*[@id="test_username"]/div/div/input')
        self.password = self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/input')
        self.login = self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/div')

    def input_info(self, username_info, password_info):
        self.username.send_keys(username_info)
        self.password.send_keys(password_info)

    def get_result(self):
        self.tipsU = self.driver.find_element_by_xpath('//*[@id="test_username"]/div/div[2]')
        self.tipsP = self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div[2]')

    def login_clear(self):
        self.password.clear()
        self.username.clear()

    def account_password_empty(self):
        time.sleep(1)
        self.login.click()
        time.sleep(1)
        self.get_result()
        if self.tipsU.text == '请输入用户名。' and self.tipsP.text == '请输入密码。':
            print(f'\nCases01:\n步骤:账号密码均为空时，点击登录。\n预期结果: 请输入用户名。请输入密码。'
                  f'\n实际结果: {self.tipsU.text}{self.tipsP.text}\nPass')
        else:
            print('\nCases01:\n步骤:账号密码均为空时，点击登录。\n预期结果:请输入用户名。请输入密码。'
                  '\n实际结果: 未输入账号信息，提示错误。\nFail')

    def account_empty(self):
        time.sleep(1)
        self.input_info('', 'adminSss')
        time.sleep(1)
        self.login.click()
        time.sleep(1)
        if self.tipsU.text == '请输入用户名。':
            print('\nCases02:\n步骤:账号为空且密码输入(adminSss)，点击登录。'
                  '\n预期结果:请输入用户名。\n实际结果:' + self.tipsU.text + '\nPass')
        else:
            print('\nCases02:\n步骤:账号为空且密码输入(adminSss)，点击登录。'
                  '\n预期结果:请输入用户名。\n实际结果:未输入用户名，提示错误。\nFail')

    def password_empty(self):
        time.sleep(1)
        self.login_clear()
        self.input_info('admin', '')
        time.sleep(1)
        self.login.click()
        time.sleep(1)
        # print('密码为空时:' + self.tipsP.text)

    def account_not_exist(self):
        time.sleep(1)
        self.login_clear()
        self.input_info('12', '')
        time.sleep(1)
        self.login.click()
        time.sleep(1)
        # print('账号不存在时:' + self.tipsU.text)

    def account_illegally(self):
        time.sleep(1)
        self.login_clear()
        self.input_info('@#$%$', '')
        time.sleep(1)
        self.login.click()
        time.sleep(1)
        # print('账号不合法时:' + self.tipsU.text)

    def password_error(self):
        time.sleep(1)
        self.login_clear()
        self.input_info('admin', 'aaabbb')
        time.sleep(1)
        self.login.click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="login"]/form/p').text == '用户名或密码有误，请重新输入或 找回密码':
            print('\nCases03:\n步骤:admin账号输入错误密码(aaabbb)，点击登录。\n预期结果:用户名或密码有误，请重新输入或 找回密码'
                  '\n实际结果:' + self.driver.find_element_by_xpath('//*[@id="login"]/form/p').text + '\nPass')
        else:
            print('\nCases03:\n步骤:admin账号输入错误密码(aaabbb)，点击登录。\n预期结果:用户名或密码有误，请重新输入或 找回密码'
                  '\n实际结果:输入错误密码，提示错误。\nPass')

        time.sleep(2)
        # 跳转找回密码页面
        self.driver.find_element_by_id('test_reset').click()
        time.sleep(1)
        title = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]').text
        if title == '找回密码':
            print('\nCases04:\n步骤:验证找回密码页是否跳转成功。\n预期结果:跳转成功\n实际结果:跳转成功\nPass')
        else:
            print('\nCases04:\n步骤:验证找回密码页是否跳转成功。\n预期结果:跳转成功\n实际结果:跳转失败\nFail')

    def normal_login(self):
        self.driver.back()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_username"]/div/div/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/div').click()
        time.sleep(2)
        # 验证是否登录成功
        title = self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[1]/div/span/span[1]').text
        if title == '仪表盘':
            print('\nCases05:\n步骤:输入正确账号和密码(admin，admin)，点击登录。\n预期结果:登录成功\n实际结果:登录成功\nPass')
        else:
            print('\nCases05:\n步骤:输入正确账号和密码(admin，admin)，点击登录。\n预期结果:登录成功\n实际结果:登录失败\nFail')

    def cancel_login(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_dropdown"]/span/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dropdown-menu-3230"]/li[3]').click()
        time.sleep(2)
        print('注销成功')

    def test_login(self):
        # 返回登录页面
        self.driver.back()
        time.sleep(2)

        # 获取元素位置
        self.get_xpath()

        # 1.账号和密码均为空
        self.account_password_empty()

        # 2.账号为空
        self.account_empty()

        # 3.密码为空
        self.password_empty()

        # 4.不存在的账号
        self.account_not_exist()

        # 5.非法账号
        self.account_illegally()

        # 6.密码错误 + 找回密码
        self.password_error()

        # 7.正常登陆
        self.normal_login()

        # 8.注销登录
        # self.cancel_login()
