#-*-coding:utf-8-*-
a0=5
a1=7
a2=45
a3=23
a4=25
a5=12
a6=33
a7=4
x=input('������x:')
#����f(1,x)
f1=a0+a1*x
print 'n=1','x=',x,'f1=',f1
#����f(2,x)
f2=a0+a1*x+a2*x**2
print 'n=2','x=',x,'f2=',f2
#����f(5,x)
f5=a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5
print 'n=5','x=',x,'f5=',f5
#����f(7,x)
f7=a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5+a6*x**6+a7*x**7
print 'n=7','x=',x,'f7=',f7