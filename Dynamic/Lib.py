import importlib.util
import os
import sys

class DynamicLoader:
    def __init__(self, load_cfg=False):
        self._obj_cache = {}
        self._load_cfg = load_cfg

    def __getattr__(self, cls_name):
        if cls_name in self._obj_cache:
            return self._obj_cache[cls_name]

        # 假设模块文件位于当前目录
        module_name = cls_name.lower()
        module_path = f"{module_name}.py"

        # 检查模块文件是否存在
        if not os.path.exists(module_path):
            raise FileNotFoundError(f"Module file '{module_path}' not found.")

        # 动态加载模块
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # 获取类
        if hasattr(module, cls_name):
            cls = getattr(module, cls_name)
            instance = cls()
            self._obj_cache[cls_name] = instance
            return instance
        else:
            raise AttributeError(f"Class '{cls_name}' not found in module '{module_name}'.")

# 使用示例
loader = DynamicLoader(load_cfg=False)
try:
    my_class_instance = loader.MyClass  # 动态加载 MyClass
    print(my_class_instance.greet())  # 调用 MyClass 的方法
except Exception as e:
    print(e)