import argparse

class TestCases:
    def __init__(self, name=None, expect_result=None):
        self.name = name
        self.expect = expect_result

        self.parser = argparse.ArgumentParser()  # 创建命令解析器
        self.add_arguments()   # 方法 ： 添加命令

        self.args, _ = self.parser.parse_known_args()

        self.address = self.args.RestServerIpAddress
        self.port = self.args.RestServerIpPort
        self.peripheral_address = self.args.PeripheralIpAddress
        self.chassis_id = self.args.ChassisId
        self.slot_id = self.args.SlotId
        self.instance_name = self.args.InstanceName

    def add_arguments(self):
        # 添加命令行参数
        self.parser.add_argument('--RestServerIpAddress', type=str, help='REST Server IP Address')
        self.parser.add_argument('--RestServerIpPort', type=int, help='REST Server Port')
        self.parser.add_argument('--PeripheralIpAddress', type=str, help='Peripheral IP Address')
        self.parser.add_argument('--ChassisId', type=str, help='Chassis ID')
        self.parser.add_argument('--SlotId', type=str, help='Slot ID')
        self.parser.add_argument('--InstanceName', type=str, help='Instance Name')

# 创建 TestCases 类的实例
test_case = TestCases(name="Test Case 1", expect_result="Success")

# 打印实例的属性，查看是否正确初始化
print(f"Name: {test_case.name}")
print(f"Expected Result: {test_case.expect}")
print(f"Address: {test_case.address}")
print(f"Port: {test_case.port}")
print(f"Peripheral Address: {test_case.peripheral_address}")
print(f"Chassis ID: {test_case.chassis_id}")
print(f"Slot ID: {test_case.slot_id}")
print(f"Instance Name: {test_case.instance_name}")
'''
在这个示例中，我们首先定义了 TestCases 类，然后在类中添加了一个 add_arguments 方法来定义命令行参数。
接着，我们创建了一个 TestCases 类的实例 test_case，并传入了 name 和 expect_result 参数。

请注意，要使这段代码正常工作，你需要从命令行运行脚本并提供相应的参数。如果你不提供参数，self.address 等属性将被设置为 None。

最后，我们打印出实例的各个属性，以验证它们是否被正确初始化。
请注意，这个示例假设所有命令行参数都是通过环境变量或在命令行中直接提供，因为 parse_known_args() 方法需要实际的命令行参数来进行解析。
'''

'''
右键直接运行的结果
D:\SoftWare\ana\python.exe D:/PythonProject/learnTest/args2.py
Name: Test Case 1
Expected Result: Success
Address: None
Port: None
Peripheral Address: None
Chassis ID: None
Slot ID: None
Instance Name: None
'''


'''
命令行参数运行的结果：
# 创建 TestCases 类的实例，需要通过命令行传递参数
# python args2.py \
--RestServerIpAddress 192.168.1.1 
--RestServerIpPort 8080 
--PeripheralIpAddress 10.0.0.1 
--ChassisId CHASSIS1 
--SlotId SLOT1 
--InstanceName INSTANCE1

(base) D:\PythonProject\learnTest>python args2.py --RestServerIpAddress 192.168.1.1 --RestServerIpPort 8080 --PeripheralIpAddress 10.0.0.1 --ChassisId CHASSIS1 --SlotId SLOT1 --InstanceNa
me INSTANCE1
Name: Test Case 1
Expected Result: Success
Address: 192.168.1.1
Port: 8080
Peripheral Address: 10.0.0.1
Chassis ID: CHASSIS1
Slot ID: SLOT1
Instance Name: INSTANCE1

'''