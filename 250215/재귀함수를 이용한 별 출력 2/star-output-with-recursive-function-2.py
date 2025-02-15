n=int(input())
def printstars(n):
    if n==0:
        return
    print('* '*n)
    printstars(n-1)
    print('* '*n)
printstars(5)