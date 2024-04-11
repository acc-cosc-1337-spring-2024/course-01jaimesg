#for value in value:
 #   print(value)


def get_students_who_look_program_and_prog2(prog1, prog2):
    print('Students with both programs')
    print(prog1.intersection(prog2))


def get_students_who_took_prog1_or_prog2(prog1, prog2):
    print('All Students')
    print(prog1.union(prog2))

def get_students_who_took_prog1_not_prog2(prog1, prog2):
    print('Students with only prog1')
    print(prog1.difference(prog2))

def get_students_who_took_prog2_not_prog1(prog1, prog2):
    print('Students with only prog2')
    print(prog2.difference(prog1))