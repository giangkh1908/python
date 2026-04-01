# # định nghĩa

# # khởi tạo
# name_age = {"Min": 23, "Big": 23}
# # tao dict rỗng
# # name_age = dict()
# # truy cập
# # print(name_age["Min"])
# # thêm vào dic, update giá trị
# # name_age["Min"] = 24
# # print(name_age)
# name_age["An"] = 22
# # print(name_age)
# # duyệt qua các phần tử

# # duyệt qua key
# for k in name_age.keys():
#     print(k)
    
# # duyệt qua value
# for v in name_age.values():
#     print(v)
    
# # duyệt qua cả key và value
# for k, v in name_age.items():
#     print(f"{k} is {v} years old")


# tính điểm trung bình điểm của từng môn trong lớp

# students = [
#     {"id": 1, "name": "Min", "score": {"math": 8.5, "literature": 7.8, "english": 9}},
#     {"id": 2, "name": "An", "score": {"math": 9.6, "literature": 6.8, "english": 8}},
#     {"id": 3, "name": "Big", "score": {"math": 7.7, "literature": 8.8, "english": 7}},
# ]

# total_math = 0
# total_literature = 0
# total_english = 0

# for student in students:
#     total_math += student["score"]["math"]
#     total_literature += student["score"]["literature"]
#     total_english += student["score"]["english"]
# num_students = len(students)
# avg_math = total_math / num_students
# avg_literature = total_literature / num_students
# avg_english = total_english / num_students
# print(f"AVG Math: {avg_math:.1f}")
# print(f"AVG Literature: {avg_literature:.1f}")
# print(f"AVG English: {avg_english:.1f}")
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}  
print(len(my_dict)) 