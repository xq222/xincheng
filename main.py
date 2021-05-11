import HTMLTestRunner, unittest, time

from xc_automation_test.src.Login.Login import Login
from xc_automation_test.src.Dashboard.Dashboard import Dashboard
from xc_automation_test.src.Server.ServerOverview import ServerOverview
from xc_automation_test.src.Server.ServerDetails import ServerDetails
from xc_automation_test.src.VirtualMachine.VirtualMachineOverview import VirtualMachineOverview
from xc_automation_test.src.VirtualMachine.NotSelectIso import NotSelectIso
from xc_automation_test.src.VirtualMachine.SelectIso import SelectIso
from xc_automation_test.src.VirtualMachine.TemplateCreation import TemplateCreation
from xc_automation_test.src.VirtualMachine.TemplateIso import TemplateIso
from xc_automation_test.src.VirtualMachine.InfomationVerification import InfomationVerification
from xc_automation_test.src.VirtualMachine.MutexOperation import MutexOperation
from xc_automation_test.src.Storage.StorageOverview import StorageOverview
from xc_automation_test.src.Storage.StorageDetails import StorageDetails
from xc_automation_test.src.LogAudit.Alarm import Alarm
from xc_automation_test.src.LogAudit.Task import Task
from xc_automation_test.src.SystemConfiguration.SystemConfiguration import SystemConfiguration
from xc_automation_test.src.OpenStack.OpenStack import OpenStack

# 设置报告文件保存路径
now = time.strftime("%Y-%m-%d %H-%M", time.localtime())
# 自定义测试报告地址
report_path = "E:/result/" + now + "Nova-result.html"
file_path = open(report_path, 'wb')


for i in range(1, 2):  # 执行300遍
    Suite = unittest.TestSuite()
    # 构建suite
    Cases = [Login('test_login'),
             Dashboard('test_dashboard'),
             ServerOverview('test_server_overview'),
             ServerDetails('test_server_details'),
             VirtualMachineOverview('test_virtual_machine_overview'),
             SelectIso('test_Virtual_machine_select_iso'),
             NotSelectIso('test_Virtual_machine_not_select_iso'),
             TemplateCreation('test_Virtual_machine_template_creation'),
             TemplateIso('test_Virtual_machine_template_iso'),
             InfomationVerification('test_Virtual_machine_infomation_verification'),
             MutexOperation('test_Virtual_machine_mutex_operation'),
             StorageOverview('test_storage_overview'),
             StorageDetails('test_storage_details'),
             Task('test_task'),
             Alarm('test_alarm'),
             SystemConfiguration('test_system_configuration'),
             OpenStack('test_openStack')]


    Suite.addTests(Cases)
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestReportCN(
        stream=file_path, title=u"Nova物理环境UI自动化测试报告", description=u"测试环境:192.168.3.240")
    # 开始执行测试套件
    runner.run(Suite)
    print('第' + str(i) + '次执行完成，详情请查看测试报告。')
