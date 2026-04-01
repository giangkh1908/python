# read
# file_obj = open("text.txt")
# content = file_obj.read()
# print(content)
# file_obj.close() # close the file after reading

# context manager
# with open("text.txt") as file_obj:
#     content = file_obj.read()
#     print(content)


# write: tao ra noi dung moi, neu file da ton tai thi se bi ghi de
# with open("text.txt", mode="w") as file_obj:
#     file_obj.write("Hello World!")

# append
# with open("text.txt", mode="a") as file_obj:
#     file_obj.write("\nHello World Again!")
    
# x - create a new file, error if file exists
with open("new_file.txt", mode="x") as file_obj:
    file_obj.write("This is a new file created using mode 'x'.")
