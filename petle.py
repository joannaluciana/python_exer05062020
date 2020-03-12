


# n=int(input('Podaj numer ciągu fibonaciego - pamietaj indeks liczy się od  zera '))    
# e1=0
# e2=1
# if n == 0:
#     print(0)
# elif n == 1:
#     print(1) 
# else :
#     for element in range (2,n+1):
#         e3=e1+e2
#         e1=e2
#         e2=e3
# print(e2)


# n=int(input('Podaj numer ciągu fibonaciego - pamietaj indeks liczy się od  zera '))  
# listafib = [0,1]
# if n == 0:
# print(0)
# elif n == 1:
# print(1)

# for element in range(2,n+1):
# listafib[element]=listafib[element-1]+listafib[element-2]
# listafib.append(listafib[element])
        
#         print (listafib[element])



# n=int(input('Podaj numer ciągu fibonaciego - pamietaj indeks liczy się od  zera '))

# def fibonaci(n):
#     if  n<1:
#         return 0
#     if n==1:
#         return 1
#     return (fibonaci(n-1)+fibonaci(n-2))
#     print(fibonaci(n))   



# n=int(input("podaj z czego silnie"))
# def silnia(n):
#     if n==0:
#         return 1
#     if n==1:
#         return 1
#     return silnia(n-1) * n

#     print (silnia(n))



# for i in range (1,101):
    
#     if i%15==0 :
#         print (f"Fizz buzz {i}")
#     elif i%5==0 :
#         print (f"Buzz {i}")
#     if i%3==0:
#         print (f"Fizz {i}")
#     else:
#         print(i)


slowo=input('wpisz slowo:')

for i in range (int(len(slowo)/2)):
    if slowo[i]!=slowo[-i-1]:
       print("to nie jest palindrom")
    else:
        print("to jest palindrom")


slowo=input('wpisz slowo:')


if(slowo == slowo[:: - 1]):
   print("Palindrome")
else:
   print("Nie palindrome")




        
    
       


