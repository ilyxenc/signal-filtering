# для Yk = S( Bn * Xk-n ) - S ( Am * Yk-m ):

B = [-0.5,1] # коэффициент B
A = [1,3,1] # коэффициенты A

X = [0,0,1,1,2,3,2,1,0,1,0,0] # задание входного сигнала
# X = [0,0,1,1,1,3,2,1,0,1,0,0]
Y = []

# функция получения одного значения отфильтрованного сигнала
def formula (X, Y, A, B):

    firstSum = 0
    for i in range(len(B)):
        firstSum += B[i] * X[len(B) - i - 1]

    secondSum = 0
    for i in range(len(A)):
        secondSum += A[i] * Y[len(A) - i - 1]

    return firstSum - secondSum

YY = []
XX = []
for i in range(len(A)):
    YY.append(0)
for i in range(len(B)):
    if i - len(B) + 1 < 0:
        XX.insert(0,0)
    else:
        XX.append(X[i])

# формирование отфильтрованного сигнала
for i in range(1,len(X)):
    result = formula( XX, YY, A, B )
    Y.append( result )
    YY = YY[1:]
    YY.append( result )
    XX = XX[1:]
    XX.append( X[i] )

Y.append ( formula( XX, YY, A, B ) )
print(Y)

# при X = [0,0,1,1,2,3,2,1,0,1,0,0]:
# [0.0, 0.0, -0.5, 1.0, 0.5, -2.5, 2.0, 6.5, -9.0, -13.0, 34.5, 13.5]
