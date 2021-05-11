import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


from xc_automation_test.src import base


class Dashboard(base.NovaBase):

    def test_dashboard(self):
        self.server_IP = ['192.168.1.217', '192.168.1.218', '192.168.1.219']
        self.server_name = ['xc-cdh-node-1', 'xc-cdh-node-2', 'xc-cdh-node-3']

        # 数据获取
        self.dashboard_loc = (By.XPATH, '//*[@id="nav"]/div/ul/li[2]/div/p/span')  # 仪表盘按钮
        self.status_loc = (By.XPATH, '//*[@id="test_health1"]/div[2]/div/p')  # 健康状态
        self.server_online_loc = (By.XPATH, '//*[@id="test_health1"]/div[3]/div[1]/div[2]/div/div[1]/div/p')  # 服务器在线数量
        self.pool_online_loc = (By.XPATH, '//*[@id="test_health1"]/div[3]/div[3]/div[2]/div/div[1]/div/p')  # 存储池在线数量
        self.data_ratio_loc = (By.XPATH, '//*[@id="test_rate"]/span')  # 数据同步比率
        self.data_sta_loc = (By.XPATH, '//*[@id="test_status"]')  # 数据是否可用
        self.cpu_num_loc = (By.XPATH, '//*[@id="r_content"]/div[2]/div[3]/div[3]/div[1]/div/div[3]/p')  # CPU总个数
        self.mem_capacity_loc = (By.XPATH, '//*[@id="r_content"]/div[2]/div[3]/div[3]/div[2]/div/div[3]/p')  # 总内存
        self.physical_capacity_loc = (By.XPATH, '//*[@id="r_content"]/div[2]/div[3]/div[3]/div[3]/div/div[3]/p')  # 物理总量
        self.user_capacity_loc = (By.XPATH, '//*[@id="r_content"]/div[2]/div[3]/div[3]/div[4]/div/div[3]/p')  # 用户总容量

        self.alarm_general_loc = (
            By.XPATH, '//*[@id="r_content"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[1]/ul/li[1]/span')  # 普通告警
        self.alarm_error_loc = (
            By.XPATH, '//*[@id="r_content"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[1]/ul/li[2]/span')  # 错误告警
        self.alarm_severity_loc = (
            By.XPATH, '//*[@id="r_content"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[1]/ul/li[3]/span')  # 严重告警

        self.alarm_auto_dispose_loc = (
            By.XPATH, '//*[@id="r_content"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[2]/ul/li[1]/span')  # 自动处理
        self.alarm_hands_dispose_loc = (
            By.XPATH, '//*[@id="r_content"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[2]/ul/li[2]/span')  # 手动处理
        self.alarm_un_dispose_loc = (
            By.XPATH, '//*[@id="r_content"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[2]/ul/li[3]/span')  # 未处理

        self.capacity_use_loc = (By.XPATH, '//*[@id="r_content"]/div[2]/div[4]/div[3]/div[1]/canvas')  # 容量使用趋势

        # 数据验证
        self.status = self.driver.find_element(*self.status_loc).text
        self.server_online = self.driver.find_element(*self.server_online_loc).text
        self.pool_online = self.driver.find_element(*self.pool_online_loc).text
        try:
            assert self.status == u'健康' or self.status == u'良好'
            assert int(self.server_online) >= 1
            assert int(self.pool_online) >= 1
            print('\nCases01:\n步骤:验证健康状态各数据回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        except NoSuchElementException:
            print('\nCases01:\n步骤:验证健康状态各数据回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        self.data_ratio = self.driver.find_element(*self.data_ratio_loc).text
        self.data_sta = self.driver.find_element(*self.data_sta_loc).text
        try:
            assert float(self.data_ratio[:-1]) <= 100
            assert self.data_sta == '数据可用'
            print('\nCases02:\n步骤:验证数据状态回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        except NoSuchElementException:
            print('\nCases02:\n步骤:验证数据状态回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 告警验证
        self.alarm_general = self.driver.find_element(*self.alarm_general_loc).text
        self.alarm_error = self.driver.find_element(*self.alarm_error_loc).text
        self.alarm_severity = self.driver.find_element(*self.alarm_severity_loc).text

        self.alarm_auto_dispose = self.driver.find_element(*self.alarm_auto_dispose_loc).text
        self.alarm_hands_dispose = self.driver.find_element(*self.alarm_hands_dispose_loc).text
        self.alarm_un_dispose = self.driver.find_element(*self.alarm_un_dispose_loc).text

        self.alarm_priority_nums = int(self.alarm_general[:-1]) + int(self.alarm_error[:-1]) + int(
            self.alarm_severity[:-1])
        self.alarm_status_nums = int(self.alarm_auto_dispose[:-1]) + int(self.alarm_hands_dispose[:-1]) + int(
            self.alarm_un_dispose[:-1])
        try:
            assert self.alarm_priority_nums == self.alarm_status_nums
            print('\nCases03:\n步骤:验证告警数量回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        except NoSuchElementException:
            print('\nCases03:\n步骤:验证告警数量回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 云平台容量状态验证
        self.cpu_num = self.driver.find_element(*self.cpu_num_loc).text
        self.mem_capacity = self.driver.find_element(*self.mem_capacity_loc).text
        self.physical_capacity = self.driver.find_element(*self.physical_capacity_loc).text
        self.user_capacity = self.driver.find_element(*self.user_capacity_loc).text

        if self.cpu_num[7:] == '0' or self.cpu_num[7:] == '数据异常':
            print('\nCases04:\n步骤:验证容量状态回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        elif self.mem_capacity[4:] == '0' or self.mem_capacity[4:] == '数据异常':
            print('\nCases04:\n步骤:验证容量状态回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        elif self.physical_capacity[4:] == '0' or self.physical_capacity[4:] == '数据异常':
            print('\nCases04:\n步骤:验证容量状态回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        elif self.user_capacity[4:] == '0' or self.user_capacity[4:] == '数据异常':
            print('\nCases04:\n步骤:验证容量状态回显情况。\n预期结果:回显正确。\n实际结果:回显错误。\nFail')
        else:
            print('\nCases04:\n步骤:验证容量状态回显情况。\n预期结果:回显正确。\n实际结果:回显正确。\nPass')

        # 点击容量使用趋势，跳转性能分析页面
        self.driver.find_element(*self.capacity_use_loc).click()
        time.sleep(2)
        self.performance_analysis = self.driver.find_element_by_xpath('//*[@id="r_content"]'
                                                                      '/div[2]/div[1]/div/span/span[1]').text
        try:
            assert self.performance_analysis == '性能分析'
            print('\nCases05:\n步骤:点击容量趋势模块。\n预期结果:跳转性能分析页面。\n实际结果:跳转性能分析页面。\nPass')
        except NoSuchElementException:
            print('\nCases05:\n步骤:点击容量趋势模块。\n预期结果:跳转性能分析页面。\n实际结果:跳转失败。\nFail')
        time.sleep(1)

        # 返回仪表盘页面
        self.driver.find_element(*self.dashboard_loc).click()
        time.sleep(2)
        # 获取服务器资源利用率IP
        self.server_cpu_use1 = self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[5]/div/div[2]/div[1]/div[2]/ul/li[1]/span[1]').text
        self.server_cpu_use2 = self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[5]/div/div[2]/div[1]/div[2]/ul/li[2]/span[1]').text
        self.server_cpu_use3 = self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[5]/div/div[2]/div[1]/div[2]/ul/li[3]/span[1]').text
        self.server_cpu_use_IP = [self.server_cpu_use1, self.server_cpu_use2, self.server_cpu_use3]
        self.server_mem_use1 = self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[5]/div/div[2]/div[2]/div[2]/ul/li[1]/span[1]').text
        self.server_mem_use2 = self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[5]/div/div[2]/div[2]/div[2]/ul/li[2]/span[1]').text
        self.server_mem_use3 = self.driver.find_element_by_xpath(
            '//*[@id="r_content"]/div[2]/div[5]/div/div[2]/div[2]/div[2]/ul/li[3]/span[1]').text
        self.server_mem_use_IP = [self.server_mem_use1, self.server_mem_use2, self.server_mem_use3]

        if set(self.server_cpu_use_IP).issubset(set(self.server_IP)):
            if set(self.server_mem_use_IP).issubset(set(self.server_IP)):
                print('\nCases06:\n步骤:验证服务器资源利用率IP回显情况。'
                      '\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        else:
            print('\nCases06:\n步骤:验证服务器资源利用率IP回显情况。'
                  '\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 验证事件告警模块是否存在
        try:
            assert self.driver.find_element_by_xpath(
                '//*[@id="r_content"]/div[2]/div[7]/div[1]/div[3]/div[1]').is_displayed()
            print('\nCases07:\n步骤:验证事件与告警模块回显情况。'
                  '\n预期结果:回显正确。\n实际结果:回显正确。\nPass')
        except NoSuchElementException:
            print('\nCases07:\n步骤:验证事件与告警模块回显情况。'
                  '\n预期结果:回显正确。\n实际结果:回显错误。\nFail')

        # 跳转任务页面
        self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[7]/div[2]/div[4]/div[1]/canvas').click()
        time.sleep(2)
        try:
            title = self.driver.find_element_by_xpath('//*[@id="r_content"]/div[2]/div[1]/div/span[2]/span[1]').text
            assert title == '任务'
            print('\nCases08:\n步骤:点击任务模块。'
                  '\n预期结果:跳转任务页面。\n实际结果:跳转任务页面。\nPass')
        except NoSuchElementException:
            print('\nCases08:\n步骤:点击任务模块。'
                  '\n预期结果:跳转任务页面。\n实际结果:跳转失败。\nFail')
