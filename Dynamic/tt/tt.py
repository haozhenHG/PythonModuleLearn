import sys,os,inspect
import importlib
# print(sys.modules,sep='\n')


if 'os' in sys.modules:
    print("os 模块已加载。")
else:
    print("os 模块未加载。")



# 直接从 sys.modules 访问 os 模块的 path 属性
if 'os' in sys.modules:
    print(sys.modules['os'].path)

print('os.sep:',os.sep)

mode = importlib.import_module('Dynamic.dycreatclass')
print(mode)
for name,cls in inspect.getmembers(mode,inspect.isclass):
    print(name)
    print(cls)
    print('*' * 100)

    if name == 'People':
        cls_type = type("Bridge_" + name, (cls,), dict(test_demo=name))
        print(cls_type.name)
        print(cls_type.get_name)
        print(cls_type.breathe)
        print(cls_type.test_demo)
        print(dir(cls_type))
    else:
        continue
