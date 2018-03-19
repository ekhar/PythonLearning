#Quadratic Solver

def quadratic_solver():
    print("Hello I am the simple quadratic solver. I solve equations that go by Ax^2 + Bx + C")

    #A Value
    while True:
        try:
            quadratic_a = int(input('Enter in the value of A: '))
            break
        except:
            print("That is not an integer. Do not include the 'x', and please try again.")
    #B Value
    while True:
        try:
            quadratic_b = int(input('Enter in the value of B: '))
            break
        except:
            print("That is not an integer. Do not include the 'x', and please try again.")
    #C Value
    while True:
        try:
            quadratic_c = int(input('Enter in the value of C: '))
            break
        except:
            print("That is not an integer. Do not include the 'x', and please try again.")

    def zero(A, B, C):
        mults = []
        for i in range(-abs(A*C),abs(A*C)):
            for x in range(-abs(A*C),abs(A*C)):
                if i*x == A*C:
                    mults.append(i) and mults.append(x)
            for y in mults:
                for z in mults:
                    if int(y) + int(z) == B and int(y) * int(z) == A*C:
                        try:
                            global factor2
                            global factor1
                            factor1 = -(y/A)
                            factor2 = -(z/A)
                            break
                        except:
                            break
        try:
            print('x = {:.3f} x = {:.3f}'.format(factor1, factor2))
        except:
            print("Sorry this problem is too advanced for my tiny little brain!")

    zero(quadratic_a, quadratic_b, quadratic_c)
    again = input("\nWould you like me to try to solve another one? (Yes/No) ")
    if again == "Yes" or "yes" or "y":
        quadratic_solver()

quadratic_solver()