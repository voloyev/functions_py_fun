user = "Rob"
print(user)

# ....


def is_user_logged_in():
    def foo():
        # global user
        user = "Im Foo"
        print(user)

    user = "Bob"
    print(user)
    return foo


is_user_logged_in()()
print(user)  # => Bob


# is_user_logged_in() # => None
