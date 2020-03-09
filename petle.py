


n=int(input('Podaj numer ciągu fibonaciego - pamietaj indeks liczy się od  zera '))    
e1=0
e2=1
if n == 0:
    print(0)
elif n == 1:
    print(1) 
else :
    for element in range (2,n):
        e3=e1+e2
        e1=e2
        e2=e3
print(e2)



# n=int(input('Podaj numer ciągu fibonaciego - pamietaj indeks liczy się od  zera '))  
# listafib=(0,1)
# if n == 0:
#     print(0)
# elif n == 1:
#     print(1)

# for element in range(2,n):
#     listafib[n]=listafib[n-1]+listafib[n-2]
#     listafib.append(listafib[n])
        
# print (listafib[n])



n=int(input('Podaj numer ciągu fibonaciego - pamietaj indeks liczy się od  zera '))

def fibonaci(n):
    if  n<1:
        return 0
    if n==1:
        return 1
    return (fibonaci(n-1)+fibonaci(n+2))
    print(fibonaci(n))   



n=int(input("podaj z czego silnie"))
def silnia(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return silnia(n-1) * n

    print (silnia(n))



