import importlib
import inspect
import sys,os

class DynamicLoader:
    def __init__(self, load_cfg=False):
        self._obj_cache = {}
        self._load_cfg = load_cfg

    def __getattr__(self, cls_name):
        # 如果类名已在缓存中，直接返回缓存的实例
        if cls_name in self._obj_cache:
            return self._obj_cache[cls_name]

        # 遍历有效的库路径，这里假设库路径是当前目录
        valid_lib_paths = ['./']

        for lib_path in valid_lib_paths:
            for lib_file in os.listdir(lib_path):
                if not lib_file.endswith(".py") or lib_file.startswith('_'):
                    continue

                mod_name = lib_file.split('.')[0]
                if mod_name not in sys.modules:
                    mod_path = os.path.join(lib_path, mod_name).replace(os.sep, '.')
                    imp_mod = importlib.import_module(mod_path)
                else:
                    imp_mod = sys.modules[mod_name]

                for name, cls in inspect.getmembers(imp_mod, inspect.isclass):
                    if not self._load_cfg and name == cls_name:
                        # 创建一个新类并将其实例存储在缓存中
                        cls_type = type("Bridge_" + cls_name, (cls,), dict(test_demo=self))
                        self._obj_cache[cls_name] = cls_type()
                        return self._obj_cache[cls_name]
                    elif self._load_cfg and (name == "Cfg" + cls_name):
                        # 将类实例存储在缓存中
                        self._obj_cache[cls_name] = cls()
                        return self._obj_cache[cls_name]

        # 如果未找到类，抛出 RuntimeError
        raise RuntimeError(f"Failed to find the class '{cls_name}' in all modules under path '{valid_lib_paths}'")

# 使用示例
loader = DynamicLoader(load_cfg=False)
try:
    my_class_instance = loader.MyClass  # 假设 MyClass 是一个在某个 .py 文件中定义的类
except RuntimeError as e:
    print(e)