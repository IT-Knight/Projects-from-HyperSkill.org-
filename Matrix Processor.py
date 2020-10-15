matrix1, matrix2, matrix3 = [], [], []
 
def call_error():
    print('The operation cannot be performed.')
    return True
 
def add_matrices():
    global matrix1, matrix2, matrix3
    R,C = input('Enter size of first matrix:').split() 
    R,C = int(R), int(C)
    print('Enter first matrix:')
    for i in range(int(R)):
        temp = input().split()           
        for el in temp:
            el = float(el)
        matrix1.append(temp)
    R2,C2 = input('Enter size of second matrix:').split()
    if int(R2) != R and int(C2) != C:
        call_error()
        return True
 
    print('Enter second matrix:')
    for i in range(int(R2)):
        temp = input().split()           
        for el in temp:
            el = float(el)
        matrix2.append(temp)
    for i in range(R):
        for j in range(C):
            matrix3.append(float(matrix1[i][j]) + float(matrix2[i][j]))
    a,b = 0, C
    print('The result is:')
    if C == 1:
        for i in matrix3:
            print(i)
    else:
        for i in range(C): 
            print(*matrix3[a:b])
            a += C
            b += C
    matrix1, matrix2, matrix3 = [], [], []
    return True
    
    
def matrix_by_constant():
    global matrix1
    R, C = [int(x) for x in input('Enter size of matrix:').split()]
    print('Enter matrix:')
    for i in range(R):
        temp = [int(x) for x in input().split()]
        matrix1.append(temp)
    const = int(input('Enter constant:'))
    for i in range(R):
        for j in range(C):
            matrix1[i][j] *= const
    print('The result is:')        
    [print(*x) for x in matrix1]
    matrix1 = []
 
 
def the_matrix_fucked_you():
    print("Enter size of first matrix: ")  # work
    row_x, col_x = [int(x) for x in input().split()]
    print("Enter first matrix: ")
    matrix_x = [input().split() for _ in range(row_x)]
    print("Enter size of second matrix: ")
    row_y, col_y = [int(x) for x in input().split()]
    print("Enter second matrix: ")
    matrix_y = [input().split() for _ in range(row_y)]
    result = [[round(sum(float(a) * float(b) for a, b in zip(X_row, Y_col)), 3) for Y_col in zip(*matrix_y)] for X_row in matrix_x]
    print("The result is: ")
    for row in result:
        print(*row)
    return True
 
def matrix_transpose():
    global matrix1, matrix2, matrix3
    print('\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
    while True:
        option = input('Your choice:')
        if option not in ['1', '2', '3', '4']:
            call_error()
            continue # предвариательно так должно происходить
        else:
            break
    R,C = [int(x) for x in input('Enter matrix size:').split() ]
    print('Enter matrix:')
    for i in range(R):
        temp = [float(x) for x in input().split()] # int/float? при выводе можно подправить
        matrix1.append(temp)
    print('The result is:')
 
    if option == '1': # обычная транспортировка
        result = list(zip(*matrix1)) # [list(x) for x in zip(*matrix)]
    if option == '2': # стороняя диагональная
        temp2 = [line[::-1] for line in matrix1]
        temp2_1 = list(zip(*temp2))
        result = [line[::-1] for line in temp2_1]
    if option == '3': # по вертикальной линии, просто развернуть
        result = [line[::-1] for line in matrix1]
    if option == '4':
        result = matrix1[::-1]
    [print(*line) for line in result]
    matrix1 = []
    return True
    
def determinant(matrix, mul): 
    width = len(matrix) 
    if width == 1: 
        return mul * matrix[0][0] 
    else: 
        sign = -1 
        sum = 0 
        for i in range(width): 
         m = [] 
         for j in range(1, width): 
          buff = [] 
          for k in range(width): 
           if k != i: 
            buff.append(matrix[j][k]) 
          m.append(buff) 
         sign *= -1 
         sum += mul * determinant(m, sign * matrix[0][i]) 
        return sum 
 
def transposeMatrix(m):
    return [list(x) for x in zip(*m)]
 
def getMatrixMinor(m,i,j): # а это непонятно.
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
 
def getMatrixDeternminant(m): # и так готово.
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
 
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
 
def getMatrixInverse(m): # готово
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
 
    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
       
while True:
    print("""\
    1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit""")
    
    choice = input('Your choice:')
    if choice not in [str(x) for x in range(6+1)]:  
        call_error()
        continue
    
    if choice == '0':
        break
    if choice == '1':
        if add_matrices(): continue
    if choice == '2':
        if matrix_by_constant(): continue
    if choice == '3':
        if the_matrix_fucked_you(): continue
    if choice == '4':
        if matrix_transpose(): continue
    if choice == '5':
        R,C = [int(x) for x in input('Enter matrix size:').split() ]
        print('Enter matrix:')
        for i in range(R):
            temp = [float(x) for x in input().split()] # 
            matrix1.append(temp)
        print('The result is:')
        print(determinant(matrix1, 1))
        matrix1 = []
        continue
    if choice == '6':
        R,C = [int(x) for x in input('Enter matrix size:').split() ]
        print('Enter matrix:')
        for i in range(R):
            temp = [float(x) for x in input().split()] # 
            matrix1.append(temp)
        print('The result is:')
        if determinant(matrix1, 1) == 0:
            print("This matrix doesn't have an inverse.")
            continue
        else:
            result = getMatrixInverse(matrix1)
            [print(*line) for line in result]
            continue
