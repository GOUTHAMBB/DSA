class Solution:
    def setZeroes(self, arr):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_update_zeros=[]
        columns_to_update_zeros=[]
        rows=len(arr)
        columns=len(arr[0])
        for i in range(rows):
            for j in range(columns):
                if arr[i][j]==0:
                    rows_to_update_zeros.append(i)
                    columns_to_update_zeros.append(j)
        if  rows_to_update_zeros:
            for i in rows_to_update_zeros:
                for j in range(0,columns):
                    arr[i][j]=0
        if  columns_to_update_zeros:
            for j in columns_to_update_zeros:
                for i in range(rows):
                    arr[i][j]=0
        return arr
    def setZeroes_optimal(self, arr):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(arr)
        columns=len(arr[0])
        rows_to_update_zeros=[0]*rows
        columns_to_update_zeros=[0]*columns
        for i in range(rows):
            for j in range(columns):
                if arr[i][j]==0:
                    rows_to_update_zeros[i]=1
                    columns_to_update_zeros[j]=1
        print(rows_to_update_zeros,columns_to_update_zeros)
        for i in range(len(rows_to_update_zeros)):
            for j in range(len(columns_to_update_zeros)):
                if rows_to_update_zeros[i]==1 or columns_to_update_zeros[j]==1:
                    arr[i][j]=0
        return arr
o1=Solution()
print(o1.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(o1.setZeroes_optimal([[1,1,1],[1,0,1],[1,1,1]]))
        

        