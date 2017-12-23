# Number Spelling - Take an Integer and Spell it Out (1-1,000,000)

# Ones
numdict_1 = {
    '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
    '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': ''
}

# Tens
numdict_2 = {
    '1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
    '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety', '0': ''
}

# Teens
numdict_teen = {
    '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
    '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '0': ''
}


def num2string():
    while True:
        global num
        global nums
        try:
            num = int(input('Enter in any number you want '))
        except:
            print('I only understand numbers.')
            num = int(input('Enter in any number you want '))
            continue
        else:
            break
    nums = str(num)


def num2wordones():  # 1
    print(numdict_1[nums[0]])


def num2wordtens():  # 10
    if num < 20 and num > 10:
        print(numdict_teen[nums])
    else:
        print(numdict_2[nums[0]] + ' ' + numdict_1[nums[1]])


def num2wordhunds():  # 100

    if int(nums[1:]) > 10 and int(nums[1:]) < 20:
        print(
            numdict_1[nums[0]] + " hundred " +
            numdict_teen[nums[1:]]
        )

    else:
        print(
            numdict_1[nums[0]] + " hundred " +
            numdict_2[nums[1]] + '' +
            numdict_1[nums[2]]
        )


def num2wordthous():  # 1,000
    if int(nums[1:]) > 10 and int(nums[1:]) < 20:
        print(
            numdict_1[nums[0]] + " thousand " +
            numdict_1[nums[1]] + " hundred " +
            numdict_teen[nums[2:]]
        )
    else:
        print(
            numdict_1[nums[0]] + " thousand " +
            numdict_1[nums[1]] + " hundred " +
            numdict_2[nums[2]] + '' +
            numdict_1[nums[3]]
        )


def num2wordtenthous():  # 10,000

    if int(nums[0:2]) > 10 and int(nums[0:2]) < 20 and int(nums[3:]) > 10 and int(nums[3:]) < 20:
        # If in the number ab,cde: ab is a teen and de is a teen
        print(
            numdict_teen[nums[0:2]] +
            " thousand " +
            numdict_1[nums[2]] + " hundred " +
            numdict_teen[nums[3:]]
        )

    elif int(nums[0:2]) > 10 and int(nums[0:2]) < 20:
        # If in the number ab,cde: ab is a teen
        print(
            numdict_teen[nums[0:2]] + " thousand " +
            numdict_1[nums[2]] + " hundred " +
            numdict_2[nums[3]] + numdict_1[nums[4]])


    elif int(nums[3:]) > 10 and int(nums[3:]) < 20:
        # If in the number ab,cde: de is a teen
        print(
            numdict_2[nums[0]] + ' ' +
            numdict_1[nums[1]] + ' thousand ' +
            numdict_1[nums[2]] + ' hundred ' +
            numdict_teen[nums[3:]]
        )

    else:
        print(
            numdict_2[nums[0]] + ' ' +
            numdict_1[nums[1]] + " thousand " +
            numdict_1[nums[2]] + " hundred " +
            numdict_2[nums[3]] + ' ' +
            numdict_1[nums[4]]
        )


def num2wordhundthous():  # 100,000

    if int(nums[1:3]) > 10 and int(nums[1:3]) < 20 and int(nums[4:]) > 10 and int(nums[4:]) < 20:
        # If in the number abc,cdef: ab is a teen and de is a teen
        print(
            numdict_1[nums[0]] + " hundred " +
            numdict_teen[nums[1:3]] +
            " thousand " +
            numdict_1[nums[2]] + " hundred " +
            numdict_teen[nums[4:]]
        )

    elif int(nums[1:3]) > 10 and int(nums[1:3]) < 20:
        # If in the number abc,def: ab is a teen
        print(
            numdict_1[nums[0]] + " hundred " +
            numdict_teen[nums[1:3]] + " thousand " +
            numdict_1[nums[3]] + " hundred " +
            numdict_2[nums[4]] + numdict_1[nums[5]])


    elif int(nums[4:]) > 10 and int(nums[4:]) < 20:
        # If in the number abc,def: de is a teen
        print(
            numdict_1[nums[0]] + ' hundred ' +
            numdict_2[nums[1]] + ' ' +
            numdict_1[nums[2]] + ' thousand ' +
            numdict_1[nums[3]] + ' hundred ' +
            numdict_teen[nums[4:]]
        )

    else:
        print(
            numdict_1[nums[0]] + ' hundred ' +
            numdict_2[nums[1]] + ' ' + numdict_1[nums[2]]
            + " thousand " + numdict_1[nums[3]] +
            " hundred " + numdict_2[nums[4]]
            + ' ' + numdict_1[nums[5]]
        )


def order():
    if num < 10:
        num2wordones()
    elif num < 100:
        num2wordtens()
    elif num < 1000:
        num2wordhunds()
    elif num < 10000:
        num2wordthous()
    elif num < 100000:
        num2wordtenthous()
    elif num < 1000000:
        num2wordhundthous()


num2string()
order()


def redo():
    global play
    again = input("Would you like to enter another number? (Yes/No)")

    if again == "Yes":
        play = True
    else:
        play = False


redo()

while play == True:
    num2string()
    order()
    redo()
    if play == False:
        print("Ok I will see you later!")
        break
