def my_decorator(func):  # func is ref to function e.g. function_name
    def wrapper(**kwargs):
        print(f"Before exe {func}")
        func(**kwargs)
        print(f"after exe {func}")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


@my_decorator
def greetings(**kwargs):
    name = kwargs["name"]
    print(f"hello {name}")


greetings(name="Bob")

say_hello()
