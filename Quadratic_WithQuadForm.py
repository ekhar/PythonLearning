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

#x = (-b+(b**2-4ac)**(1/2))/(2a) | x = (-b-(b**2-4ac)**(1/2))/(2a)

def quadsolver(a,b,c):
    xval_1 = (-b+((b**2)-4*a*c)**(1/2))/(2*a)
    xval_2 = (-b-((b**2)-4*a*c)**(1/2))/(2*a)
    print("x = {:.2f} and x = {:.2f}".format(xval_1,xval_2))

quadsolver(quadratic_a,quadratic_b,quadratic_c)
