#Пз4.2 Дано целое число N (> 0). Найти сумму 11 + 22 + ... + NN

while True:
    n = int( input('n = ') )
    try:
        print( sum( [ float(i)**float(i) for i in range(1, n+1) ] ) )
    except Exception as e:
        print(e)
    print()
    res = sum( [ i ** i for i in range(1, n + 1) ] )
    print( f'Длина числа = { len( str(res) ) }' )
    print(res)
    print()