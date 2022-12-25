if __name__ == '__main__':
    n = int(input())
    
    if(n<=0):
        print('STDIN')
    else:
        for i in range(n):
            print(i**2)