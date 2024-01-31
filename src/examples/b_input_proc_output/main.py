import input_process_output

val1 = input("enter val 1:")
val2 = input("enter val 2:")
val3 = input("enter val 3: ")

result = input_process_output.operator_precedence_1(int(val1), int(val2), int(val3))

print(result)

