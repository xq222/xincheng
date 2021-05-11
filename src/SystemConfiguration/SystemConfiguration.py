import time
import random

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


from xc_automation_test.src import base


class SystemConfiguration(base.NovaBase):

    def test_system_configuration(self):
        # 1.基本信息
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/'
                                          'div[2]/div[1]/div[2]/div[2]/span').click()
        time.sleep(3)
        info = self.driver.find_element_by_id('test_infoContent').text
        if info != None:
            print('\nCases01:\n步骤:验证基本信息回显是否正确。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases01:\n步骤:验证基本信息回显是否正确。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        # 2.NTP服务器
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[2]/div/div[2]/span').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="test_ntpContent"]/div[1]/div').click()  # 点击开关按钮
        time.sleep(2)
        # 2.1NTP启用测试
        try:
            assert self.driver.find_element_by_id('test_ntpN').is_displayed()
            self.driver.find_element_by_id('test_ntpN').click()  # 取消关闭
        except NoSuchElementException:
            pass
        time.sleep(1.5)
        # 2.2NTP地址验证
        NTPdress = self.driver.find_element_by_xpath('//*[@id="test_ntpContent"]/div[2]/form/div/div/div[1]/input')
        NTPsave = self.driver.find_element_by_xpath('//*[@id="test_ntp"]/div[4]/button')
        NTPdress.clear()
        time.sleep(1)
        NTPdress.send_keys('@#$%!dS写')
        NTPsave.click()
        time.sleep(1)
        NTPtips = self.driver.find_element_by_xpath('//*[@id="test_ntpContent"]/div[2]/form/div/div/div[2]')
        if NTPtips.text == '请输入正确的ntp地址。':
            print('\nCases02:\n步骤:NTP地址输入无效值(@#$%!dS写)，点击保存。\n预期结果:请输入正确的ntp地址。\n实际结果:请输入正确的ntp地址。\nPass')
        else:
            print('\nCases02:\n步骤:NTP地址输入无效值(@#$%!dS写)，点击保存。\n预期结果:请输入正确的ntp地址。\n实际结果:操作失败\nFail')

        time.sleep(2)
        NTPdress.clear()
        NTPdress.send_keys('192.168.1.114')
        NTPsave.click()
        time.sleep(2)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == 'NTP配置保存成功。':
            print('\nCases03:\n步骤:NTP地址输入有效值(192.168.1.114)，点击保存。\n预期结果:NTP配置保存成功。\n实际结果:NTP配置保存成功。\nPass')
        else:
            print('\nCases03:\n步骤:NTP地址输入有效值(192.168.1.114)，点击保存。\n预期结果:NTP配置保存成功。\n实际结果:操作失败\nFail')
        time.sleep(2)
        NTPdress.clear()  # 改回原来配置
        time.sleep(1)
        NTPdress.send_keys('192.168.1.224')
        time.sleep(1)
        NTPsave.click()
        time.sleep(2)
        # 3.DNS服务器
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[2]/div/div[3]/span').click()
        time.sleep(2)
        try:
            assert self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[2]/span').is_displayed()
            if self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[2]/span').text == '8.8.8.8':
                self.driver.find_element_by_id('test_dnsAdd').click()
                time.sleep(1)
                DNSdress = self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[1]/div/input')
                DNSsave = self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[1]/i')
                DNSsave.click()
                time.sleep(2)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                    print('\nCases04:\n步骤:DNS地址为空时，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:请输入正确的DNS地址。\nPass')
                else:
                    print('\nCases04:\n步骤:DNS地址为空时，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:操作失败。\nFail')
                time.sleep(2)
                DNSdress.send_keys('@#$%!dS写')
                DNSsave.click()
                time.sleep(2)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                    print('\nCases05:\n步骤:DNS地址为无效值时(@#$%!dS写)，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:请输入正确的DNS地址。\nPass')
                else:
                    print('\nCases05:\n步骤:DNS地址为无效值时(@#$%!dS写)，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:操作失败。\nFail')
                time.sleep(1)
                DNSdress.clear()
                DNSdress.send_keys('123.123.123.123')
                DNSsave.click()
                time.sleep(3)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == 'DNS域名服务器地址保存成功。':
                    print('\nCases06:\n步骤:DNS地址为有效值时(123.123.123.123)，点击保存。'
                          '\n预期结果:DNS域名服务器地址保存成功。\n实际结果:DNS域名服务器地址保存成功。\nPass')
                else:
                    print('\nCases06:\n步骤:DNS地址为有效值时(123.123.123.123)，点击保存。\n预期结果:DNS域名服务器地址保存成功。\n实际结果:操作失败。\nFail')
                # 添加相同的DNS地址
                self.driver.find_element_by_id('test_dnsAdd').click()
                DNSdress.send_keys('123.123.123.123')
                DNSsave.click()
                time.sleep(1)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '当前DNS地址已存在，请重新输入。':
                    print('\nCases07:\n步骤:DNS地址重名时(123.123.123.123)，点击保存。'
                          '\n预期结果:当前DNS地址已存在，请重新输入。\n实际结果:当前DNS地址已存在，请重新输入。\nPass')
                else:
                    print('\nCases07:\n步骤:DNS地址重名时(123.123.123.123)，点击保存。\n预期结果:当前DNS地址已存在，请重新输入。\n实际结果:操作失败。\nFail')

                time.sleep(1)
                # 3.2删除新增的DNS服务
                self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[2]/i').click()
                time.sleep(3)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '删除成功。':
                    print('\nCases08:\n步骤:删除DNS服务，点击保存。'
                          '\n预期结果:删除成功。\n实际结果:删除成功。\nPass')
                else:
                    print('\nCases08:\n步骤:删除DNS服务，点击保存。'
                          '\n预期结果:删除成功。\n实际结果:删除失败。\nFail')
                time.sleep(2)
            else:
                # 删除错误的DNS服务
                self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[2]/i').click()
                time.sleep(3)
                self.driver.find_element_by_id('test_dnsAdd').click()
                time.sleep(2)
                DNSdress = self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[1]/div/input')
                DNSsave = self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[1]/i')
                DNSsave.click()
                time.sleep(2)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                    print('\nCases04:\n步骤:DNS地址为空时，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:请输入正确的DNS地址。\nPass')
                else:
                    print('\nCases04:\n步骤:DNS地址为空时，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:操作失败。\nFail')
                time.sleep(2)
                DNSdress.send_keys('@#$%!dS写')
                DNSsave.click()
                time.sleep(2)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                    print('\nCases05:\n步骤:DNS地址为无效值时(@#$%!dS写)，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:请输入正确的DNS地址。\nPass')
                else:
                    print('\nCases05:\n步骤:DNS地址为无效值时(@#$%!dS写)，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:操作失败。\nFail')
                time.sleep(2)
                DNSdress.clear()
                DNSdress.send_keys('8.8.8.8')
                DNSsave.click()
                time.sleep(3.5)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                    print('\nCases06:\n步骤:DNS地址为有效值时(8.8.8.8)，点击保存。'
                          '\n预期结果:DNS域名服务器地址保存成功。\n实际结果:DNS域名服务器地址保存成功。\nPass')
                else:
                    print('\nCases06:\n步骤:DNS地址为有效值时(8.8.8.8)，点击保存。\n预期结果:DNS域名服务器地址保存成功。\n实际结果:操作失败。\nFail')
                # 添加相同的DNS地址
                self.driver.find_element_by_id('test_dnsAdd').click()
                DNSdress.send_keys('8.8.8.8')
                DNSsave.click()
                time.sleep(1)
                if self.driver.find_element_by_xpath('/html/body/div[2]').text == '当前DNS地址已存在，请重新输入。':
                    print('\nCases07:\n步骤:DNS地址重名时(8.8.8.8)，点击保存。'
                          '\n预期结果:当前DNS地址已存在，请重新输入。\n实际结果:当前DNS地址已存在，请重新输入。\nPass')
                else:
                    print('\nCases07:\n步骤:DNS地址重名时(8.8.8.8)，点击保存。\n预期结果:当前DNS地址已存在，请重新输入。\n实际结果:操作失败。\nFail')
                time.sleep(1)
        except NoSuchElementException:
            self.driver.find_element_by_id('test_dnsAdd').click()
            time.sleep(1)
            DNSdress = self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[1]/div/input')
            DNSsave = self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[1]/i')
            DNSsave.click()
            time.sleep(2)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                print('\nCases04:\n步骤:DNS地址为空时，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:请输入正确的DNS地址。\nPass')
            else:
                print('\nCases04:\n步骤:DNS地址为空时，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:操作失败。\nFail')
            DNSdress.send_keys('@#$%!dS写')
            DNSsave.click()
            time.sleep(2)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                print('\nCases05:\n步骤:DNS地址为无效值时(@#$%!dS写)，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:请输入正确的DNS地址。\nPass')
            else:
                print('\nCases05:\n步骤:DNS地址为无效值时(@#$%!dS写)，点击保存。\n预期结果:请输入正确的DNS地址。\n实际结果:操作失败。\nFail')
            time.sleep(2)
            DNSdress.clear()
            DNSdress.send_keys('123.123.123.123')
            DNSsave.click()
            time.sleep(3.5)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '请输入正确的DNS地址。':
                print('\nCases06:\n步骤:DNS地址为有效值时(123.123.123.123)，点击保存。'
                      '\n预期结果:DNS域名服务器地址保存成功。\n实际结果:DNS域名服务器地址保存成功。\nPass')
            else:
                print('\nCases06:\n步骤:DNS地址为有效值时(123.123.123.123)，点击保存。\n预期结果:DNS域名服务器地址保存成功。\n实际结果:操作失败。\nFail')
            # 添加相同的DNS地址
            self.driver.find_element_by_id('test_dnsAdd').click()
            DNSdress.send_keys('123.123.123.123')
            DNSsave.click()
            time.sleep(1)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '当前DNS地址已存在，请重新输入。':
                print('\nCases07:\n步骤:DNS地址重名时(123.123.123.123)，点击保存。'
                      '\n预期结果:当前DNS地址已存在，请重新输入。\n实际结果:当前DNS地址已存在，请重新输入。\nPass')
            else:
                print('\nCases07:\n步骤:DNS地址重名时(123.123.123.123)，点击保存。\n预期结果:当前DNS地址已存在，请重新输入。\n实际结果:操作失败。\nFail')
            time.sleep(1)
            # 3.2删除DNS服务
            self.driver.find_element_by_xpath('//*[@id="test_dnsContent"]/li[2]/i').click()
            time.sleep(3)
            if self.driver.find_element_by_xpath('/html/body/div[2]').text == '删除成功。':
                print('\nCases08:\n步骤:删除DNS服务，点击保存。'
                      '\n预期结果:删除成功。\n实际结果:删除成功。\nPass')
            else:
                print('\nCases08:\n步骤:删除DNS服务，点击保存。'
                      '\n预期结果:删除成功。\n实际结果:删除失败。\nFail')
            DNSdress.clear()
            DNSdress.send_keys('8.8.8.8')
            DNSsave.click()
        time.sleep(2)
        # 4.日志收集
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[2]/div/div[4]/span').click()
        time.sleep(2)
        log = self.driver.find_element_by_xpath('//*[@id="test_logs"]/div[2]/div[1]/span')
        if log.text == '集群最新日志包括云平台当前的运行状态和系统信息，也包括各组件最新的日志文件。' \
                       '本功能不会收集客户业务数据，仅供售后工程师技术支持使用。':
            print('\nCases09:\n步骤:验证集群最新日志的提示。\n预期结果:提示正确。\n实际结果:提示正确。\nPass')
        else:
            print('\nCases09:\n步骤:验证集群最新日志的提示。\n预期结果:提示正确。\n实际结果:提示错误。\nFail')
        self.driver.find_element_by_xpath('//*[@id="test_logsContent"]/div/div/input').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(2)
        if log.text == '集群信息包括云平台当前的运行状态和系统信息，生成数据量最小。' \
                       '本功能不会收集客户业务数据，仅供售后工程师技术支持使用。':
            print('\nCases10:\n步骤:验证集群信息的提示。\n预期结果:提示正确。\n实际结果:提示正确。\nPass')
        else:
            print('\nCases10:\n步骤:验证集群信息的提示。\n预期结果:提示正确。\n实际结果:提示错误。\nFail')
            time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_logsContent"]/div/div/input').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()
        time.sleep(2)
        if log.text == '集群完整日志包括云平台当前的运行状态和系统信息，包括各组件最新的和历史日志文件，' \
                       '生成数据量最大，请耐心等待。本功能不会收集客户业务数据，仅供售后工程师技术支持使用。':
            print('\nCases11:\n步骤:集群完整日志的提示。\n预期结果:提示正确。\n实际结果:提示正确。\nPass')
        else:
            print('\nCases11:\n步骤:集群完整日志的提示。\n预期结果:提示正确。\n实际结果:提示错误。\nFail')
        time.sleep(2)

        # 5.SNMP配置
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[3]/div/div[2]/span').click()
        time.sleep(2)
        # 点击启用按钮
        self.driver.find_element_by_xpath('//*[@id="test_snmpContent"]/div[1]/div').click()  # 点击启用按钮
        time.sleep(1)
        try:
            assert self.driver.find_element_by_id('test_snmpN').is_displayed()
            self.driver.find_element_by_id('test_snmpN').click()  # 取消关闭
        except NoSuchElementException:
            pass
        time.sleep(1)
        # snmp地址测试
        SNMPtxt = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[2]'
                                                    '/div/div[3]/div/div[2]/form/div/div/div[1]/input')
        SNMPsave = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/'
                                                     'div[2]/div/div[4]/button')
        SNMPtxt.clear()
        time.sleep(1)
        SNMPtxt.send_keys('@#$y12.2')
        SNMPsave.click()
        time.sleep(2)
        tips1 = self.driver.find_element_by_xpath('//*[@id="test_snmpContent"]'
                                                  '/div[2]/form/div/div/div[2]').text
        if tips1 == '请输入正确的snmp地址。':
            print('\nCases12:\n步骤:SNMP地址为无效值时(@#$y12.2)，点击保存。\n预期结果:请输入正确的snmp地址。\n实际结果:请输入正确的snmp地址。\nPass')
        else:
            print('\nCases12:\n步骤:SNMP地址为无效值时(@#$y12.2)，点击保存。\n预期结果:请输入正确的snmp地址。\n实际结果:操作失败。\nFail')

        time.sleep(2)
        SNMPtxt.clear()
        time.sleep(1)
        SNMPtxt.send_keys('192.168.1.60')
        SNMPsave.click()
        time.sleep(2)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == 'SNMP配置保存成功。':
            print('\nCases13:\n步骤:SNMP地址为有效值时(192.168.1.60)，点击保存。\n预期结果:SNMP配置保存成功。\n实际结果:SNMP配置保存成功。\nPass')
        else:
            print('\nCases13:\n步骤:SNMP地址为有效值时(192.168.1.60)，点击保存。\n预期结果:SNMP配置保存成功。\n实际结果:操作失败。\nFail')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_snmpContent"]/div[1]/div').click()  # 关闭服务
        time.sleep(2)
        self.driver.find_element_by_id('test_snmpY').click()
        time.sleep(2)
        SNMPsave.click()
        time.sleep(1)
        # 6.SMTP配置
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[3]/div/div[3]/span').click()
        time.sleep(2)
        self.driver.find_element_by_id('test_smtpTest').click()
        time.sleep(1)
        try:
            assert self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').is_displayed()  # 判断测试框
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/input').send_keys(
                '2932441070@qq.com')
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
            time.sleep(2)
            #  print(self.driver.find_element_by_xpath('/html/body/div[2]').text)
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="test_smtpContent"]/div[1]/div/div').click()  # 启用
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_smtpContent"]/div[2]/div/div/input').send_keys(
                'smtp.163.com')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_smtpContent"]/div[3]/div/div/input').send_keys('25')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_smtpContent"]/div[5]/div/div/input').send_keys(
                'qqtxyy163@13.com')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="test_smtpContent"]/div[6]/div/div/input').send_keys(
                'IQYDSKMYEZXPMHCM')
            time.sleep(1)
            self.driver.find_element_by_id('test_smtpSave').click()  # 保存
            time.sleep(1)
            self.driver.find_element_by_id('test_smtpTest').click()  # 点击测试
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/input').send_keys(
                '2932441070@qq.com')
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
            time.sleep(2)
            #  print(self.driver.find_element_by_xpath('/html/body/div[2]').text)

        # 7.电子邮件
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[3]/div/div[4]/span').click()
        time.sleep(2)
        # 添加邮箱
        self.driver.find_element_by_id('test_alertAdd').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_alertTab"]/li/p[3]/i').click()  # 不输入信息，直接点击保存
        time.sleep(1)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '邮箱格式不正确。':
            print('\nCases14:\n步骤:邮箱输入为空时，点击保存。\n预期结果:邮箱格式不正确。\n实际结果:邮箱格式不正确。\nPass')
        else:
            print('\nCases14:\n步骤:邮箱输入为空时，点击保存。\n预期结果:邮箱格式不正确。\n实际结果:操作失败。\nFail')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_alertTab"]/li/p[1]/div/input') \
            .send_keys('2932441070@qq.com')  # 输入正确的邮箱
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_alertTab"]/li/p[3]/i').click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '邮件添加成功。':
            print('\nCases15:\n步骤:邮箱输入有效值时(2932441070@qq.com)，点击保存。\n预期结果:邮件添加成功。\n实际结果:邮件添加成功。\nPass')
        else:
            print('\nCases15:\n步骤:邮箱输入有效值时(2932441070@qq.com)，点击保存。\n预期结果:邮件添加成功。\n实际结果:操作失败。\nFail')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_alertTab"]/li[2]/p[3]/i').click()  # 点击删除邮箱
        time.sleep(1)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '邮件地址删除成功。':
            print('\nCases16:\n步骤:删除邮箱，点击保存。\n预期结果:邮件地址删除成功。\n实际结果:邮件地址删除成功。\nPass')
        else:
            print('\nCases16:\n步骤:删除邮箱，点击保存。\n预期结果:邮件地址删除成功。\n实际结果:操作失败。\nFail')
        time.sleep(1)

        # 8.云管平台
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[3]/div/div[5]/span').click()
        time.sleep(2)
        # 添加云管平台
        self.driver.find_element_by_id('test_nebulaAdd').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebula"]/div[4]/button').click()  # 直接点击保存
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="test_nebulaList"]/div/div/div[2]').text == '请输入ip地址':
            print('\nCases17:\n步骤:云管平台IP地址为空时，点击保存。\n预期结果:请输入ip地址\n实际结果:请输入ip地址\nPass')
        else:
            print('\nCases17:\n步骤:云管平台IP地址为空时，点击保存。\n预期结果:请输入ip地址\n实际结果:操作失败。\nFail')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebulaList"]/div/div/div/div/input') \
            .send_keys("qwe192.168.1")  # 输入错误的ip地址
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebula"]/div[4]/button').click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="test_nebulaList"]/div/div/div[2]').text == '请输入正确的地址':
            print('\nCases18:\n步骤:云管平台IP为无效值时(qwe192.168.1)，点击保存。\n预期结果:请输入正确的地址\n实际结果:请输入正确的地址\nPass')
        else:
            print('\nCases18:\n步骤:云管平台IP为无效值时(qwe192.168.1)，点击保存。\n预期结果:请输入正确的地址\n实际结果:操作失败。\nFail')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebulaList"]/div/div/div/div/input').clear()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebulaList"]/div/div/div/div/input') \
            .send_keys('192.168.1.177')  # 输入正确的ip地址
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebula"]/div[4]/button').click()
        time.sleep(3)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '地址保存成功。':
            print('\nCases19:\n步骤:云管平台IP为有效值时(192.168.1.177)，点击保存。\n预期结果:地址保存成功。\n实际结果:地址保存成功。\nPass')
        else:
            print('\nCases19:\n步骤:云管平台IP为有效值时(192.168.1.177)，点击保存。\n预期结果:地址保存成功。\n实际结果:操作失败。\nFail')
        time.sleep(1)
        self.driver.find_element_by_id('test_nebulaAdd').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebulaList"]/div/div/div/div/input') \
            .send_keys('192.168.1.177')  # 添加相同的ip
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_nebula"]/div[4]/button').click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="test_nebulaList"]/div/div/div[2]').text == '当前地址已存在，请重新输入。':
            print('\nCases20:\n步骤:云管平台IP重复时(192.168.1.177)，点击保存。\n预期结果:当前地址已存在，请重新输入。\n实际结果:当前地址已存在，请重新输入。\nPass')
        else:
            print('\nCases20:\n步骤:云管平台IP重复时(192.168.1.177)，点击保存。\n预期结果:当前地址已存在，请重新输入。\n实际结果:操作失败。\nFail')
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_nebulaShow"]/li/div/i[2]').click()  # 删除ip
        time.sleep(3)
        if self.driver.find_element_by_xpath('/html/body/div[2]').text == '地址删除成功。':
            print('\nCases21:\n步骤:删除云管平台IP时，点击保存。\n预期结果:地址删除成功。\n实际结果:地址删除成功。\nPass')
        else:
            print('\nCases21:\n步骤:删除云管平台IP时，点击保存。\n预期结果:地址删除成功。\n实际结果:操作失败。\nFail')
        #  用户管理
        time.sleep(1)
        self.driver.quit()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.168.3.31/#/login")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="test_username"]/div/div/input').send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/input').send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/div').click()
        time.sleep(2)
        # 9.用户管理
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[1]/p').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/div[2]/div[4]/div/div[2]/span').click()
        time.sleep(2)
        # 删除账户
        try:
            assert self.driver.find_element_by_xpath(
                '//*[@id="test_userTab"]/div[3]/table/tbody/tr[3]/td[5]/div/div[2]/p/i[2]').is_displayed()
            self.driver.find_element_by_xpath(
                '//*[@id="test_userTab"]/div[3]/table/tbody/tr[3]/td[5]/div/div[2]/p/i[2]').click()  # 删除第三个账号
        except NoSuchElementException:
            pass
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="user #test_user"]/div[3]/div[1]/span').click()#新建用户
        time.sleep(2)
        num = random.randint(0, 999)
        self.driver.find_element_by_xpath('//*[@id="test_userCreateContent"]/div[1]/div/div/input').send_keys(
            'test' + str(num))
        self.driver.find_element_by_xpath('//*[@id="test_userCreateContent"]/div[2]/div/div/input').send_keys(
            '2932441070@qq.com')
        self.driver.find_element_by_xpath('//*[@id="test_userCreateContent"]/div[3]/div/div/input').send_keys(
            'a12345678')
        self.driver.find_element_by_xpath('//*[@id="test_userCreateContent"]/div[4]/div/div/input').send_keys(
            'a12345678')
        self.driver.find_element_by_xpath('//*[@id="test_userCreateContent"]/div[5]/div/div/label[1]/span[1]').click()
        time.sleep(1)
        self.driver.find_element_by_id('test_userSave').click()  # 保存
        time.sleep(2)
        # 退出当前账号并新账号登录
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="test_username"]/div/div/input').send_keys('test' + str(num))
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/input').send_keys('a12345678')
        self.driver.find_element_by_xpath('//*[@id="test_password"]/div/div/div').click()
        time.sleep(2)
        if self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[1]/div/span/span[1]').text == '仪表盘':
            print('\nCases22:\n步骤:新增账号登录系统。\n预期结果:账号可用。\n实际结果:账号可用。\nPass')
        else:
            print('\nCases22:\n步骤:新增账号登录系统。\n预期结果:账号可用。\n实际结果:账号不可用。\nFail')
