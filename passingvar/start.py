def f():
    print ('Inside f() : '), a

# Variable 'a' is redefined as a local
def g():
    a = 2
    print ('Inside g() : '),a

# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print ('Inside h() : '),a

# Global scope
if __name__ == '__main__':
    a = 1
    print ('global :',a)
    f()
    print ('global : ',a)
    g()
    print ('global : ',a)
    h()
    print ('global : ',a)
