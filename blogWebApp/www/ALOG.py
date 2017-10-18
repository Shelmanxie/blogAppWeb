#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Creat on 20171016 

__author__ = 'shelman'


from contextlib import contextmanager
import logging; logging.basicConfig(level=logging.INFO)


# 此方法仅仅用于调试 用于跟踪方法的调用 
@contextmanager
def loggerInfo(msg,tag=None):
    '''logging封装，使用contentmanager，可用于方法调用的追踪'''
    if tag==None:
        tag='WebApp'
    logging.info('Loging begin with  {tag}:{msg}'.format(tag=tag, msg=msg))
    yield 
    logging.info('Loging end with  {tag}:{msg}'.format(tag=tag, msg=msg))

# 以下为调用方法
if __name__ == '__main__':
    with loggerInfo('test', 'some message') as l:
        logging.info('do something')