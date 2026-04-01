# dung higher order function 
# wrapper ( hàm bao) và wrapped function ( hàm được bao)

# dung hof
def decorator(func):
    def wrapper():
        print("This is wrapper function")
        func()
        print("This is wrapper function after calling wrapped function")
    
    return wrapper


@decorator   # chi ap dung khi ap dung decorator
def say_hello():
    print("helllo")

# Sử dụng higher order function để tạo một hàm mới bằng cách truyền say_hello vào decorator
# wrapped = decorator(say_hello)
# wrapped()

# su dung decorator
say_hello()