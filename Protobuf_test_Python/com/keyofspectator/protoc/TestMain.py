#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月16日

@author: KeyOfSpectator
'''

import Person_pb2

person = Person_pb2.Person()
person.id = 1
person.name = 'fsc'
#'标题'.decode('gbk').encode('utf-8')
#person.sex = u"男".decode('gb2312').encode('utf8')
#person.sex = "男".decode('utf-8').encode('')
#print type(person.sex)
person.sex = 'male'
person.tel = '12345678'

print person

serializedStr = person.SerializeToString()
print type(serializedStr)
print serializedStr