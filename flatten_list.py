def flatten_iterative(nested_list):
    stack = list(nested_list[::-1])  # reverse so we pop in order
    print("stack = ", stack)
    result = []
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result

lst=[10,7,6,[11,13,5],88]
print(flatten_iterative(lst))
