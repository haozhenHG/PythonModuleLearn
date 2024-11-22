import argparse

class MyClass:
    def __init__(self):
        print('__init__')
        self.parser = argparse.ArgumentParser(description="这是一个示例程序。")
        self.parser.add_argument('--at4_filename', type=str, help='AT4文件的名称')
        self.args = self.parser.parse_args()

    def run(self):
        print(f"AT4文件名: {self.args.at4_filename}")

# 创建类的实例并运行
if __name__ == "__main__":
    my_class = MyClass()
    my_class.run()