def func1():
    print('func1 is called.')
def func2():
    print('func2 is called.')
def func3():
    print('func3 is called.')

class A:
    A=1
    def __init__(self,name='A'):
        self.name=name

    def _say(self,msg):
        print(msg)

    def sayhello(self):
        print('hello,i am {}'.format(self.__class__))

class B:
    B=2
    def __init__(self,name='B'):
        self.name=name
    def _do_work(self):
        print('Do some work.')
    def greet(self):
        print('hello,i am {}'.format(self.name))