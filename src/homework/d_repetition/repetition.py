#jaimesg


def get_factorial(num):
    sum = 0

    for num in[1, 2, 6, 24, 120, 720]:
    #for i in range(num):        
            print(num)

def sum_odd_numbers(num):
      for i in range(1, 20, 2):
            print(i)


def homework_menu():
    for word in ["Homework 3 Menu", "1 - Factoral", "2 - Sum odd numbers", "3 - Exit"]:
        print(word)

def while_validate_user_input():
    lot_number = -1
    
    while(lot_number != 0):
        lot_number = input("Enter number from 1-10")

    