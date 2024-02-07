import decisions

ratio = float(input("Total grade: "))
result = decisions.get_faculty_rating(ratio)

print(ratio, "is", result)
