
def calculate_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 55:
        return 'C'
    else:
        return 'D'

def main():
    print("Enter marks of 5 students")
    stud1_marks = list(map(int, input("Enter marks of student 1: ").split(",")))
    stud2_marks = list(map(int, input("Enter marks of student 2: ").split(",")))
    stud3_marks = list(map(int, input("Enter marks of student 3: ").split(",")))
    stud4_marks = list(map(int, input("Enter marks of student 4: ").split(",")))
    stud5_marks = list(map(int, input("Enter marks of student 5: ").split(",")))

    stud1_avg = sum(stud1_marks)/len(stud1_marks)
    stud2_avg = sum(stud2_marks)/len(stud2_marks)
    stud3_avg = sum(stud3_marks)/len(stud3_marks)
    stud4_avg = sum(stud4_marks)/len(stud4_marks)
    stud5_avg = sum(stud5_marks)/len(stud5_marks)

    stud_dict ={
        "stud1":stud1_avg,
        "stud2":stud2_avg,
        "stud3":stud3_avg,
        "stud4":stud4_avg,
        "stud5":stud5_avg
    }

    for stud in stud_dict.items():
        print(f"{stud[0]}: Average Marks = {stud[1]} Grade = {calculate_grade(stud[1])}")

    topper = max(stud_dict, key=stud_dict.get)
    print(f"Topper: {topper} with Average Marks = {stud_dict[topper]}")

main()