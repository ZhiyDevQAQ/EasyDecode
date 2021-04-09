#!/usr/bin/env python
# coding:utf-8
# @Author:ZhiyDevQAQ
# @Name:ThunderDecode.py
# @Date:2021/4/9 9:03
import binascii
import re
import base64


class thunderdecode(object):

    def __init__(self) -> None:
        self.THUNDER_HEADER = 'thunder://'
        self.THUNDER_PREFIX = 'AA'
        self.THUNDER_SUFFIX = 'ZZ'

    def __str__(self) -> str:
        msg = '''

        本类用于实现迅雷链接的解析，首先你要实例化对象，然后定义一个变量接收调用thunder2reallink方法传回的解析结果
        例如:
            th = thunderdecode()
            result = th.thunder2reallink('thunder://QUFodHRwOi8vZGwxNC54NTcwLmNvbS8zRE1HQU1FX05FS09QQVJBX1ZvbC4wLkNIVC5HcmVlbi5yYXJaWg==')
            print(result)

        '''
        return msg

    def check_url(func):
        '''
        本装饰器用于实现对迅雷链接的检查
        :return wapper的内存地址:
        '''

        def wapper(self, url):
            #  匹配模式:http | https | ftp | ed2k | thunder
            if re.search(r'^[thunder://]', url):
                return func(self, url)
            else:
                return '灵能信号有误，请检查'

        return wapper

    @check_url
    def thunder2reallink(self, url):
        '''
        本方法实现对迅雷链接的解析
        :param url: 迅雷链接
        :return url:经过解析的真实链接
        '''
        url = url[len(self.THUNDER_HEADER):]
        url = url.encode('utf-8')
        try:
            url = base64.b64decode(url)
        except binascii.Error as e:
            print('灵能信号有误，具体信息如下:%s' % e)
        url = url.decode('utf-8')
        url = url[len(self.THUNDER_PREFIX):-len(self.THUNDER_SUFFIX)]
        return url


if __name__ == '__main__':
    th = thunderdecode()
    print(th)
    tk = th.thunder2reallink('thunder://QUFodHRwOi8vZGwxNC54NTcwLmNvbS8zRE1HQU1FX05FS09QQVJBX1ZvbC4wLkNIVC5HcmVlbi5yYXJaWg==')
    print(tk)
