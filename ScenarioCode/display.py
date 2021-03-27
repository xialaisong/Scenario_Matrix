'''
a = [[0 for i in range(3)]for j in range(5)]
for i in range(5):             #row
    for j in range(3):         #column
        a[i][j] = int(input())
        print(a)
'''


def input_dis(N):     #num of row
    print('N=', N)
    print('input :')
    a = [[int(x) for x in input().split()] for y in range(N)]
    for i in range(N-1):
        if len(a[i]) != len(a[i+1]):
            print('different number of column')
            return -1
    return a
    print(a)

#input_dis(3)


def output_dis(output):
    if type(output) == int:
        print(output)
        return -1
    if type(output) == list:
        #r = self.row_num
        #c = self.col_num
        n = 0
        for r in range(len(output)):
            for c in range(len(output[0])):
                #n = len(str(output[r][c]))
                if n < len(str(output[r][c])):
                    n = len(str(output[r][c]))

        for r in range(len(output)):
            for c in range(len(output[0])):
                item = str(output[r][c])
                print(item + ' '*(n+4-len(item)), end='')
            print('\n')

output_dis([[1, 2, 3], [1, 3, 4], [1, 1000, 3]])
