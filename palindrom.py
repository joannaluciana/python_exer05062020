


slowo=input('wpisz slowo:')

for i in range (len slowo//2)):
    if slowo[i]!=slowo[-i-1]:
       print("to nie jest palindrom")
    else:
        print("to jest palindrom")
dlaczego zawsze mi drukuje to jest palindrom

slowo=input('wpisz slowo:')


#    nie wolno :/ tez ładne :(
if(slowo == slowo[:: - 1]):
   print("Palindrom")
else:
   print("Nie palindrom")


#    mnie się to najbardziej podoba rozwiązanie ponizej
# simple beautiful


my_str = 'alla'

rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")




        
    
       


