def task_1_1():
    print("\t\t\t\t\tTask 1.1")
    user_input = input()
    result_list = list(user_input.lower())
    print("Created list is:", result_list)

def task_1_2():
    print("\t\t\t\t\tTask 1.2")
    char_count = {}
    user_input = input()
    for char in user_input:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    result = [(char, count) for char, count in char_count.items()]
    print(result)

def task_1_3():
    print("Task 1.3")
    list_vow = []
    list_cons = []
    list_sym = []

    vowels = ['a', 'e', 'i', 'o', 'u']

    user_input = input()

    for char in user_input:
        if char.isalpha():
            if char.lower() in vowels:
                list_vow.append(char)
            else:
                list_cons.append(char)
        else:
            list_sym.append(char)

    print("vowels", list_vow)
    print("cons", list_cons)
    print("symbols", list_sym)

def task_1_4():
    print("\t\t\t\t\tTask 1.4")
    list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]

    n = len(sorted(list_A))

    q1_idx = n // 4
    q2_idx = q1_idx * 2
    q3_idx = q1_idx * 3

    q1 = sorted(list_A)[:q1_idx]
    q2 = sorted(list_A)[q1_idx:q2_idx]
    q3 = sorted(list_A)[q2_idx:q3_idx]
    q4 = sorted(list_A)[q3_idx:]

    if n % 2 != 0:
        q1.append(0)
    print("Q1:", q1)
    print("Q2:", q2)
    print("Q3:", q3)
    print("Q4:", q4)

def task_2_1():
    print("Task 2.1, 2.2, 2.3, 2.4")
    student_name = input("Student name - ")

    assignment_scores = input("Scores for assignments = ").split(',')
    assignment_scores = [int(score.strip()) for score in assignment_scores]

    lab_scores = input("Labs = ").split(',')
    lab_scores = [float(score.strip()) for score in lab_scores]

    test_scores = input("Tests =  ").split(',')
    test_scores = [int(score.strip()) for score in test_scores]

    final_grade = 0.3 * (sum(assignment_scores) / len(assignment_scores)) + 0.5 * (sum(lab_scores) / len(lab_scores)) + 0.2 * (sum(test_scores) / len(test_scores))

    student = {
        'name': student_name,
        'assignment': assignment_scores,
        'test': test_scores,
        'lab': lab_scores,
        'final_grade': final_grade
    }

    print(student)
    submitted_assignments = len(student.get('assignment', []))
    submitted_labs = len(student.get('lab', []))
    submitted_tests = len(student.get('test', []))
    submission_check = {student['name']: submitted_assignments + submitted_labs + submitted_tests}
    print(submission_check)

def task_3_1():
    transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

    stats = {}

    for user_id, transaction_type in transactions:
        if user_id not in stats:
            stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}
        if transaction_type in [1, 2, 3]:
            stats[user_id][transaction_type] += 1

    for user_id, user_data in stats.items():
        transaction_counts = [(t, user_data[t]) for t in [1, 2, 3]]
        transaction_counts.sort(key=lambda x: -x[1])
        most_frequent = transaction_counts[0][0]
        least_frequent = transaction_counts[-1][0]
        stats[user_id]['mft'] = most_frequent
        stats[user_id]['lft'] = least_frequent

    print(stats)

task_1_1()
task_1_2()
task_1_3()
task_1_4()
task_2_1()
task_3_1()
