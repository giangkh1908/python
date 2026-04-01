
# def my_sum(x, y):
#     return x + y

# a =6
# b = 5
# print(my_sum(a, b))

# hàm ko trả về giá trị nào

# def my_func(a, b):
#     tong = a + b
    
# a = my_func(3, 4)
# print(a)  # None vì hàm ko trả về giá trị nào cả

# co su dung return nhung ko kem gia tri

# def my_func(a, b):
#     tong = a + b
#     return

# a = my_func(3, 4)


# ham tra ve 1 gia tri
# def my_func(a, b):
#     tong = a + b
#     return tong

# a = my_func(3, 4)
# print(a)  # 7 vì hàm trả về giá trị tong

# ham tra ve nhieu gia tri

# def tinh_hinh_chu_nhat(dai, rong):
#     chu_vi = (dai + rong) * 2
#     dien_tich = dai * rong
#     return chu_vi, dien_tich
# cv, dt = tinh_hinh_chu_nhat(5, 3)
# my_var = tinh_hinh_chu_nhat(5, 3)
# print("Chu vi:", cv)
# print("Dien tich:", dt)
# print("My var:", my_var)  # my_var là một tuple chứa cả chu vi và diện tích
# print(my_var[0])

# ham so chi co cac tham so bat buoc

# def tinh_dien_tich_hinh_chu_nhat(dai, rong):
#     dien_tich = dai * rong
#     return dien_tich
# # call function
# # dt = tinh_dien_tich_hinh_chu_nhat(5, 3)
# # print("Dien tich hinh chu nhat:", dt)


# dt = tinh_dien_tich_hinh_chu_nhat(5, rong=6)
# print("Dien tich hinh chu nhat:", dt)

# ham so co tham so mac dinh

def tinh_dien_tich_hinh_chu_nhat(dai, rong=4):
    dien_tich = dai * rong
    return dien_tich
# call function
dt1 = tinh_dien_tich_hinh_chu_nhat(5)
print("Dien tich hinh chu nhat 1:", dt1)