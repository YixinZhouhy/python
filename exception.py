# 异常 exception
# 使用try .. except 处理异常
# the statements between the try and excep is executed
# if no exception occurs  , the except clause is skipped
# and execuation of the try statment is finished
try:
    text = input('Enter something-->')
# Press ctrl + d
except EOFError:
    print('Why did you do an EOF on me ?')
# Press ctrl + c
except KeyboardInterrupt:
    print('You cancelled the opreation.')
else:
    print('You entered {}'.format(text))


# 抛出异常 raise
# the raise statement allows the programmer to force
# a specified exception to ocurr
# 引发的错误或异常直接或间接属于Exception类的派生类subclass
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print( 'ShortInputException: The input was' +
           '{0} long, excepted at least {1}'
           .format(ex.length, ex.atleast))
else:
    print('No exception was raised')


# try ... finally
# 程序在退出之前，finally子句总会运行

import sys
import time

f = none

try:
    f = open(poem.text)
    while True:
        line = f.readline()
        if(len(line) == 0):
            break
        print(line, end = ' ')
        sys.stdout.flush()
        print('Press ctrl + c now')
        time.sleep(2)  # 2秒休眠
except IOError:
    print('Could not find file poem.text')
except KeyboardInterrupt:
    print('You cancellded the reading from the file.')
finally:
    if f:
        f.close()
    print('Cleaning up: Closed the file')


# with 语句
with open('poem.text') as f:
    for line in f:
        print(line, end = ' ')









































            






