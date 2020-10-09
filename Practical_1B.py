
#Performing Matrix Operations
M1 = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]

M2 = [ [9, 8, 7],
      [6, 5, 4],
      [3, 2, 1] ]

M3 = [ [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0] ]

print("\nMatrix 1: \n")
for i in M1:
    print(i)
    
print("\nMatrix 2: \n")
for i in M2:
    print(i)

#Matrix multiplication
for i in range(len(M1)):
    for j in range(len(M2[0])):
        for k in range(len(M2)):
            M3[i][j] += M1[i][k] * M2[k][j]
       
print("\nMatrix Multiplication: \n")       
for i in M3:
    print(i)
        
#Matrix addition
for i in range(len(M3)):
    for j in range(len(M3[0])):
        M3[i][j] = M1[i][j] + M2[i][j]

print("\nMatrix Addition: \n")
for i in M3:
    print(i)

#Transpose of matrix
#Matrix 1
for i in range(len(M3)):
    for j in range(len(M3[0])):
        M3[i][j] = M1[j][i]

print("\nTranspose of matrix 1: \n")
for i in M3:
    print(i)

#Matrix 2
for i in range(len(M3)):
    for j in range(len(M3[0])):
        M3[i][j] = M2[j][i]

print("\nTranspose of matrix 2: \n")
for i in M3:
    print(i)

    
