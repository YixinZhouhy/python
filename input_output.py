# 输入与输出
def reverse(text):
    return text[ : : -1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Enter text:')
if is_palindrome(something):
    print('Yes, it\'s a palindrome')
else:
    print('No, it\'s not a palindrome')


# 文件
# 打开模式可以为:阅读模式'r' 写入模式 'w' 追加模式'a'
# 文本模式't' 二进制模式'b'

poem = '''\
Progaramming is fun
when the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt', 'w') # w会将文件里的删除，再重新写入
f.write(poem)  # 向文件中编写文件
f.close()  # 关闭文件

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:  # 零长度只是EOF
        break
    print(line, end = '-')  # 每行的末尾都已经有换行符，因为从文件中读取得

f.close()


# pickle
st = 'ff'
import pickle
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile,'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)


# unicode
import io

f = io.open('abc.txt', 'wt', encoding = 'utf-8')
f.write(u'Imagine non-English language here')
f.close()

text = io.open('abc.txt', encoding = 'utf-8').read()
print(text)



# write a tabel of squares and cubes
# rjust() 右对齐
for x in range(1,11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end = ' ')
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d}  {2:4d}'.format(x,  x * x,  x * x * x ))






















    
































