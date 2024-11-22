import os,sys

path = r'D:\PythonProject'
print(os.walk(path))

for root,dirs,files in os.walk(path):
    print(root,' / ',dirs,' /  ',files)
    print('\n')

path = 'D:\PythonProject\learnTest'
print('dir:',os.listdir(path))

import time

print(time.time())