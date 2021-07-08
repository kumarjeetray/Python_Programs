'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''

if __name__ == '__main__':
    records = []
    num = int(input())
    for _ in range(num):
        name = input()
        score = float(input())
        records.append([name, score])
    sorted_scores = sorted(list(set([x[1] for x in records])))
    second_lowest = sorted_scores[1]
    final_list = []
    for student in records:
        if second_lowest == student[1]:
            final_list.append(student[0])

    for student in sorted(final_list):
        print(student)
