# length
my_str='hello'
# print(len(my_str))
# index 
# print(my_str[-5])

# slicing for string
# print(my_str[1:4])

# dem so luong nguyen am trong 1 cau tieng anh
# nguyên âm trong tiếng anh: ue o a i

# senectence = input("nhap cau tieng anh: ")

# vowels ="ueoai"
# senectence = senectence.lower()

# count = 0

# for char in senectence:
#     if char in vowels:
#         count += 1
        
# print("so luong nguyen am trong cau ", senectence, "la: ", count)

# reverse string : đảo ngược chuỗi
my_str = "hello"
reversed_str = ""
for char in my_str:
    reversed_str = char + reversed_str
print("reversed string: ", reversed_str)