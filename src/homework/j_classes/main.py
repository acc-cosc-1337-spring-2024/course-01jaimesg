#01jaimesg
from class_a import Die

def main():
    die = Die()
    while True:
        print ("1 - roll die")
        print ("2 - exit program")

        num = input("Enter number:  ")
        if num == "1":
              die.roll()
              print(die)
        
        elif num == "2":
             print("Exiting")
             break
        
        else:
             print("Invalid selection. Please enter 1 or 2: ")
main()
