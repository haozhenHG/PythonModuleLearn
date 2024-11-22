import inspect
import importlib
def get_attrs_of_module(module_name='temp'):
    module=__import__(module_name)#动态引入模块(temp.py文件)
    print('__import__ module:',module)  # module: <module 'temp' from 'D:\\PythonProject\\Dynamic\\temp.py'>

    module  = importlib.import_module(module_name)

    print('importlib.import_module module:',module)  # module: <module 'temp' from 'D:\\PythonProject\\Dynamic\\temp.py'>

    for name,cls in inspect.getmembers(module,inspect.isclass):
        print('name:',name)
        print('cls:',cls)

    print('*' * 80)
    #用inspect.getmembers获取模块中的类
    # classes=[(clsname,fullname) for (clsname,fullname) in inspect.getmembers(module,inspect.isclass)]
    classes = [clsname for (clsname,fullname) in inspect.getmembers(module,inspect.isclass)]

    print('classes:',classes) #classes: ['A', 'B']
    print('*' * 80)
    fun  = [clsname for (clsname,fullname) in inspect.getmembers(module,inspect.isfunction)]

    print('fun:',fun) #classes: ['A', 'B']


    dic_cls_methods={}
    for clsname in classes:
        #用python内置的getattr()方法获取模块的类，inspect.isfunction()方法过滤出该类的方法

        print('getattr :',getattr(module,clsname)) # getattr : <class 'temp.A'>
        print('*'*40)
        print('inspect+getattr',inspect.getmembers(getattr(module,clsname))) # inspect.isfunction会限制输出
        '''
        inspect+getattr [
        ('A', 1),
        ('__class__', <class 'type'>),
        ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>),
        ('__dict__', mappingproxy(
            {
                '__module__': 'temp',
                'A': 1,
                '__init__': <function A.__init__ at 0x000001CD7C980700>,
                '_say': <function A._say at 0x000001CD7C980790>,
                'sayhello': <function A.sayhello at 0x000001CD7C980820>,
                '__dict__': <attribute '__dict__' of 'A' objects>,
                '__weakref__': <attribute '__weakref__' of 'A' objects>,
                '__doc__': None
            })
        ),
        ('__dir__', <method '__dir__' of 'object' objects>),
        ('__doc__', None),
        ...]
        '''
        print('*'*40)
        print('inspect+getattr+isfunction',inspect.getmembers(getattr(module,clsname),inspect.isfunction)) # inspect.isfunction会限制输出  获取类clsname中的所有函数成员
        print('*'*40)

        modules = [method_name for (method_name, method) in inspect.getmembers(getattr(module, clsname), inspect.isfunction)]

        dic_cls_methods[clsname]=modules

    print(dic_cls_methods)

get_attrs_of_module()