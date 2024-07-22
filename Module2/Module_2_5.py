# import randUnivers as rU
#def get_matrix():
#    matrix=[]
#    for i in range(1,10):
#        matrix += [rU.rInt(100,10)]
#    print (matrix)
#get_matrix()
def get_matrix(n, m, value):
    matrix=[]
    while n:
        row= []
        for j in range(0,m):
            row.append(value)
        matrix.append(row)
        n -= 1
    print (matrix)
get_matrix(5,4,10)
