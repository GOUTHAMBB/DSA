l1=[1,2,3,4,5,6,7,8,9]
matrix_2d=[]
temp=[]*10
for i in range(0,9):
    print(l1[i])
    temp.append(l1[i])
    if i!=0 and  (i+1)%3==0:
        print(temp)
        matrix_2d.append(temp)
        temp=[]
print(matrix_2d)


for i in range(0,len(matrix_2d)):
    for j in range(0,len(matrix_2d)):
         print(f"{matrix_2d[i][j]}", end="\t")
print()
for i in range(0,len(matrix_2d)):
    for j in range(0,len(matrix_2d)):
        print(f"{matrix_2d[j][i]}",end="\t")
print()

# upper triangle
for i in range(0,3):
    for j in range(0,3):
        if j>i:
            print("-",end="\t")
        else:
            print("*",end="\t")
    print()
print()
print()
# lower triangle
for i in range(0,3):
    for j in range(0,3):
        if j<i:
            print("-",end="\t")
        else:
            print("*",end="\t")
    print()
print()
print()
for i in range(0,3):
    for j in range(0,3):
        if j!=i:
            print("-",end="\t")
        else:
            print("*",end="\t")
    print()
arr=[[1,2,3],[4,5,6],[7,8,9]]
print(arr)
for i in range(0,3):
    for j in range(0,3):
        if i>j:
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
print(arr)
        
class two_d_matrix_basics():
    def create_an_empty_matrix(self,rows,columns):
        arr=[[0]*columns for i in range(rows)]
        return arr
    def transponse_the_matrix(self,arr):
        col=len(arr[0])
        rows=len(arr)
        temp_arr= self.create_an_empty_matrix(rows,col)
        for i in range(0,3):
            for j in range(0,3):
                if i>=j:
                    temp_arr[i][j]=arr[j][i]
                    temp_arr[j][i]=arr[i][j]
        return temp_arr
    def sum_of_all_elemts_of_matrix(self,arr):
        col=len(arr[0])
        rows=len(arr)
        sum=0
        for i in range(0,rows):
            for j in range(0,col):
                sum+=arr[i][j]
        return sum
o1=two_d_matrix_basics()
print(o1.create_an_empty_matrix(3,5))
print(o1.transponse_the_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(o1.sum_of_all_elemts_of_matrix([[1,2,3],[4,5,6],[7,8,9]]))
    
