'''def A():
    for i in range(3):
        print(' *',end=' ')
    print()
    n=0
    while n<=2:
        print('* '+'  '*(5-2)+'*')
        n+=1
    for i in range(5):
        print('*',end=' ')
    print()
    e=0
    while e<=2:
        print('* '+'  '*(5-2)+'*')
        e+=1
print(A())'''


'''def B():
    for i in range(3):
        print('* ',end=' ')
    print()
    n=0
    while n<=2:
        print('* '+'  '*(5-2)+'*')
        n+=1
    for i in range(4):
        print('*',end=' ')
    print()
    e=0
    while e<=2:
        print('* '+'  '*(5-2)+'*')
        e+=1
    for i in range(4):
        print('*',end=' ')


def C():
    for i in range(3):
        print(' '+'*',end=' ')
    print()
    for i in range(3):
        print('*')
    for i in range(3):
        print(' '+'*',end=' ')



def D():
    for i in range(3):
        print('* ',end=' ')
    print()
    n=0
    while n<=4:
        print('* '+'  '*(5-2)+'*')
        n+=1
    for i in range(3):
        print('* ',end=' ')



def E():
    for i in range(3):
        print('*',end=' ')
    for i in range(3):
        print('*')
    for i in range(3):
        print('*',end=' ')
    for i in range(3):
        print('*')
    for i in range(4):
        print('*',end=' ')


def F():
    for i in range(5):
        print('*',end=' ')
    print()
    n=0
    for i in range(2):
        print('*')
    n=0
    for i in range(5):
        print('*',end=' ')
    print()
    n=0
    for i in range(5):
        print('*')
    print()
    n=0



def G():
    for i in range(7):
        if i == 0 or i == 6:
            print(" * * * ")
        elif i == 3:
            print("*   * *")
        elif i in [1, 2]:
            print("*      ")
        else:
            print("*     *")



def H():
    n=0
    while n<=2:
        print('* '+'  '*2+'*')
        n+=1
    for i in range(4):
        print('*',end=' ')
    print()
    n=0
    while n<=2:
        print('* '+'  '*2+'*')
        n+=1



def I():
    for i in range(5):
        print('*',end=' ')
    print()
    for i in range(4):
        print(' '*3+' *')
    for i in range(5):
        print('*',end=' ')



def J():
    for i in range(5):
        print('*',end=' ')
    print()
    for i in range(2):
        print('  '*2+'*')
    for i in range(2):
        print(' '+'*',end=' ')
    print()
    for i in range(2):
        print(' '+'*',end=' ')
    print()




def K():
    i=1
    for i in range(2,0,-1):
        print('*'+'  '*i+'*')
        i+=1
    i=1
    for i in range(3):
        print('*'+'  '*i+'*')


def L():
    for i in range(3):
        print('*')
    for i in range(3):
        print('*',end=' ')



def M():
    for i in range(7):
        if i == 0:
            print("*     *")
        elif i == 1:
            print("**   **")
        elif i == 2:
            print("* * * *")
        elif i == 3:
            print("*  *  *")
        else:
            print("*     *")



def N():
    for i in range(7):
        if i == 0 or i == 6:
            print("*      *")
        else:
            print("*" + " " * (i - 1) + "* " + " " * (5 - i) + "*")
 


def O():
    for i in range(3):
        print(' *',end=' ')
    print()
    n=0
    while n<=3:
        print('* '+'  '*(3)+'*')
        n+=1
    for i in range(3):
        print(' *',end=' ')



def P():
    for i in range(2):
        print(' *',end=' ')
    print()
    n=0
    while n<=2:
        print('* '+'  '*(2)+'*')
        n+=1
    for i in range(1):
        print('* ',end=' ')
    for i in range(4):
        print('*')



def Q():
    for i in range(7):
        if i == 0 or i == 6:
            print(" * * * ")
        elif i == 4:
            print("*    **")
        elif i in [1, 2, 3]:
            print("*     *")
        else:
            print("*      *")


def R():
    for i in range(5):
        print('*',end=' ')
    print()
    n=0
    while n<=2:
        print('* '+'  '*(5-2)+'*')
        n+=1
    for i in range(5):
        print('*',end=' ')
    print()
    i=1
    for i in range(7):
        print('*'+' '*i+'*')


def S():
    for i in range(4):
        print('*',end=' ')
    for i in range(3):
        print('*')
    for i in range(5):
        print('*',end=' ')
    print()
    for i in range(2):
        print('  '*3+'  *')
    for i in range(5):
        print('*',end=' ')



def T():
    for i in range(5):
        print('*',end=' ')
    print()
    for i in range(4):
        print('  '*2+'*')



def U():
    n=0
    while n<=3:
        print('*'+'  '*3+'*')
        n+=1
    for i in range(2):
        print(' '+' *',end='')



def V():
    for i in range(5):
        for j in range(2 * 5 - 1):
            if j == i or j == 2 * 5 - 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()



def W():
    for i in range(5):
        if i == 0:
            print("*     *")
        elif i == 1:
            print("*     *")
        elif i == 2:
            print("*  *  *")
        elif i == 3:
            print("* * * *")
        else:
            print("*     *")




def X():
    for i in range(5):
        for j in range(2 * 5 ):
            if j == i or j == 2 * 5 - 1 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    for i in range(5,0,-1):
        for j in range(2 * 6 - 1):
            if j == i or j == 2 * 6 - 1 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()



def Y():
    for i in range(5):
        for j in range(2 * 5 - 1):
            if j == i or j == 2 * 5 - 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    for i in range(3):
        print(' '*3+' *')





def Z():
    for i in range(5):
        print('*',end=' ')
    for i in range(6):
        print('  '*(i-1)+'*')
    for i in range(6):
        print('*',end=' ')


l=[]

n=input('Enter your Name in caps ')
for i in n:
    if i=='A' or i=='a':
        l.append(A())
    elif i=='B' or i=='b':
        B()
        print('\n')
    elif i=='C' or i=='c':
        C()
        print('\n')
    elif i=='D' or i=='d':
        D()
        print('\n')
    elif i=='E' or i=='e':
        E()
        print('\n')
    elif i=='F' or i=='f':
        F()
        print('\n')
    elif i=='G' or i=='g':
        G()
        print('\n')
    elif i=='H' or i=='h':
        H()
        print('\n')
    elif i=='I' or i=='i':
        I()
        print('\n')
    elif i=='J' or i=='j':
        J()
        print('\n')
    elif i=='K' or i=='k':
        K()
        print('\n')
    elif i=='L' or i=='l':
        L()
        print('\n')
    elif i=='M' or i=='m':
        M()
        print('\n')
    elif i=='N' or i=='n':
        N()
        print('\n')
    elif i=='O' or i=='o':
        O()
        print('\n')
    elif i=='P' or i=='p':
        P()
        print('\n')
    elif i=='Q' or i=='q':
        Q()
        print('\n')
    elif i=='R' or i=='r':
        R()
        print('\n')
    elif i=='S' or i=='s':
        S()
        print('\n')
    elif i=='T' or i=='t':
        T()
        print('\n')
    elif i=='U' or i=='u':
        U()
        print('\n')
    elif i=='V' or i=='v':
        V()
        print('\n')
    elif i=='W' or i=='w':
        W()
        print('\n')
    elif i=='X' or i=='x':
        X()
        print('\n')
    elif i=='Y' or i=='y':
        Y()
        print('\n')
    elif i=='Z' or i=='z':
        Z()
print(l)'''


'''n=7
a=-1
for i in range(n):
    a+=1
    print(' '*(n-i)+'*'+' '*(a+i)+'*')
for i in range(n-1):
    print('*',end='  ')'''

'''n=5
for i in range(n+1):
    for k in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end=' ')
        for a in range(n-i):
            print(' ',end='')
    print()'''


n=5

'''for i in range(n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(n-i,0,-1):
        print('*',end='')
    print()
'''
for i in range(n):
    for j in range(n-i):
        print(' '*(j)+'*')



#n=int(input())
'''n=6
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for k in range((i+1)*2):
        print('*',end='')
    print()'''





















