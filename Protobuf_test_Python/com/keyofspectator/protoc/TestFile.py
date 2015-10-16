#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月16日

@author: KeyOfSpectator
'''
import sys
import Person_pb2

person = Person_pb2.Person()
person.id = 1
person.name = 'fsc'
person.sex = 'male'
person.tel = '12345678'

print person

file_path = '/Users/KeyOfSpectator/tmp_file'

# Write the new person to disk.
f = open(file_path, "wb")
f.write(person.SerializeToString())
f.close()
print 'person1 write done'
print

# Read from the disk
person2 = Person_pb2.Person()

try:
  f = open(file_path, "rb")
  person2.ParseFromString(f.read())
  f.close()
except IOError:
  print file_path + ": Could not open file.  Creating a new one."

print 'read person2'
print person2