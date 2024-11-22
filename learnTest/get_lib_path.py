import os
import sys

path = 'F:\hao.zhen\oakgate_testdev-feature-OGT-0320-Exerciser\src\magic_cases\library\generic\lib_loader.py'

print('test:',os.path.abspath(path).split(os.sep))

print('@'*50)
print('__file__:',os.path.abspath(__file__).split(os.sep)) # ['D:', 'PythonProject', 'learnTest', 'get_lib_path.py']

path_l = os.path.abspath(__file__).split(os.sep)

root = os.sep.join(path_l[:path_l.index('learnTest')])
print('root:',root) # D:\PythonProject

dirr = os.sep.join([root,'learnTest','index'])
print(dirr)
if os.path.exists(dirr):
    print('exists!')
else:
    print('not exists!')

# for root,dirs,files in os.walk(root):
#     print(root,dirs,files)
#     print('#'*30)

print(os.listdir('D:\PythonProject\Dynamic'))

print('sys.modules :',sys.modules,sep='\n')