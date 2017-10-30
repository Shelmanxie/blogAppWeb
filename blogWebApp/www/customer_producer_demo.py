
# 其实，子程序就是协程的一种特例
def consumer():
    r = ''
    while True:
        # yield这里 python会将consumer函数识别为生成器，这时c = consumer()并不会真正调用函数体，而是以函数体生成了一个生成器对象实例。
        n = yield r
        if not n:
            print('not n return')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__ == '__main__':
    c = consumer()
    produce(c)