def square_sum(no):
    sum=0
    while(no!=0):
        r=no%10
        square=r*r
        sum=sum+square
        no=no//10
    print(sum)
no=int(input())
square_sum(no)