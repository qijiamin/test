#_*_coding:utf-8-*-
import math
a=input('������a:')
b=input('������b:')
c=input('������c:')
D=b*b-4*a*c
print 'D=',D
if D<0:
    print '�޷����'
else:
    x1=(-1.0*b+math.sqrt(D))/(2*a)
    x2=(-1.0*b-math.sqrt(D))/(2*a)
    print x1,x2