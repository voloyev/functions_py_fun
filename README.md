# Code as narrative #
Every code should do the following:

1. Collecting input
2. Performing work
3. Delivering output
4. Handling failures

Let's have an example:

```python
def location(item: str, value: str):
    sub_table = get_sub_table(item, value)
    if(len(sub_table) == 0):
        raise Exception
    else:
        first_row = sub_table[0]
    match item:
        case 'class':
            return get_location(first_row.file_path, first_row.class_name, None)
        case 'method':
            return get_location(first_row.file_path, first_row.class_name, first_row.method_name)
        case 'file':
            return get_location(first_row.file_path, None, None)
        case _:
            raise Exception("Item must be :class, :method, or :file")
```

Fix it:


# Decorators #

# Functools #
