import sets

prog1 = set(['Student1', 'Student2', 'Student3'])
prog2 = set(['Student3', 'Student4', 'Student5'])


#sets.get_students_who_look_program_and_prog2(prog1, prog2)

#sets.get_students_who_took_prog1_or_prog2(prog1, prog2)

#sets.get_students_who_took_prog1_not_prog2(prog1, prog2)

#sets.get_students_who_took_prog2_not_prog1(prog1, prog2)

import sets

while True:

    print("1 - Students who took prog1 and prog2")
    print("2 - Students who took prog2 only")
    print("3 - Students who took prog1 not prog2")
    print("4 - Students who took prog2 not prog1")
    print("5 - Exit")

    num = input("Enter number between 1-3: ")

    if num == "1":
        sets.get_students_who_look_program_and_prog2(prog1, prog2)

    elif num == "2":
        sets.get_students_who_took_prog1_or_prog2(prog1, prog2)

    elif num == "3":
        sets.get_students_who_took_prog1_not_prog2(prog1, prog2)
    
    elif num == "4":
        sets.get_students_who_took_prog2_not_prog1(prog1, prog2)
    
    elif num == "5":
        print("Exiting the program. ")
        break

    else:
        print("Invalid selection. Please enter 1-5: ")