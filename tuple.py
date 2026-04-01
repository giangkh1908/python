tuple_1 = ("a", 3)
# print(tuple_1)
# print(type(tuple_1))

# print(f"chieu dai cua tuple: {len(tuple_1)}")
# # duyet qua cac phan tu cua tuple
# for item in tuple_1:
#     print(item)
    
# cong cac tuple
tuple_2 = (4, 5, 6)
tuple_3 = tuple_1 + tuple_2
# print(tuple_3)

#conver tuple sang list
list_1 = list(tuple_3)
# print(list_1)
list_1.append("new item")
# print(list_1)
list_1.remove(3)
# conver list sang tuple
new_tuple = tuple(list_1)
print(new_tuple)
print(f"new tuple: {new_tuple}")

# dem so lan xuat hien
print(tuple_3.count(4))

# trich xuat index 1 phan tu trong tuple
print(tuple_3.index(4))

