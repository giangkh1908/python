# xu ly ngoai le

try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Closing the file")