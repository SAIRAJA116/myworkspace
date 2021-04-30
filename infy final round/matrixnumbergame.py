r = int(input())
c=r+1
matrix=[]

for i in range(r):
    matrix.append(list(map(int,input().split())))
print(matrix)
res=[]
for i in range(r):
    #if we are travelling across the row
    for j in range(c-2):
        if(matrix[i][j]==matrix[i][j+1]==matrix[i][j+2]):
            res.append(matrix[i][j])

for i in range(c):
    #if we are travelling across the column
    for j in range(r-2):
        if(matrix[j][i]==matrix[j+1][i]==matrix[j+2][i]):
            res.append(matrix[i][j])

for i in range(r-2):
    for j in range(c-2):
        if(matrix[i][j]==matrix[i+1][j+1]==matrix[i+1][j+1]):
            res.append(matrix[i][j])

print(res)
print(min(res))