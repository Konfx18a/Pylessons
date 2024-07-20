import randUnivers as rU
def get_matrix():
    matrix=[]
    for i in range(1,10):
        matrix += [rU.rInt(100,10)]
    print (matrix)
get_matrix()