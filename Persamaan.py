from trapezoid import*

def Integral(f):
    a = float(input('batas bawah = '))
    b = float(input('batas atas = '))
    n = 100

    integral = trapezoid(f,a,b,n)

    print(a,',',b,',', integral)

    
Integral(lambda x: 4*x**2)
Integral(lambda x: 5*x**4)
Integral(lambda x: 6*x**6)
Integral(lambda x: 7*x**9)
Integral(lambda x: 8*x**11)
Integral(lambda x: 9*x**13)
Integral(lambda x: 10*x**15)
Integral(lambda x: 11*x**17)
Integral(lambda x: 12*x**19)
Integral(lambda x: 13*x**21)
