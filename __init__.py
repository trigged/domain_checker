#coding=utf-8

x = {'123': "我"}
print x['123']
print x['123'].decode("utf-8")
name = str(x).split("'")[3]
print  str(x).split("'")

print name
print name.decode("ascii").encode("gb2312")
import chardet

print chardet.detect(name)
print "======"
value = name.decode("ascii")
print isinstance(name,unicode)
print isinstance(value,unicode)

