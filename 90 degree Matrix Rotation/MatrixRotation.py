  
def RotateMatrix(mat):
    m = len(mat)
    n = m-1
    if len(mat)==0 or len(mat)!=len(mat[0]):
        return False
    for i in range(m//2):
        k = n-i
        for j in range(i,k):
            temp1 = mat[i][j]
            mat[i][j] = mat[n-j][i]
            mat[n-j][i]=mat[n-i][n-j]
            mat[n-i][n-j] = mat[j][n-i]
            mat[j][n-i]=temp1
    return True
