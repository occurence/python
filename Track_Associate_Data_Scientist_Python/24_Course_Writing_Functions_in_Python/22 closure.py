def parent(arg_1, arg_2):
    value = 22
    my_dict = {'chocolate': 'yummy'}
    def child():
        print(2 * value)
        print(my_dict['chocolate'])
        print(arg_1 + arg_2)
    return child
new_function = parent(3, 4)
print([cell.cell_contents for cell in new_function.__closure__])

print(list(map(lambda cell: cell.cell_contents, new_function.__closure__)))
