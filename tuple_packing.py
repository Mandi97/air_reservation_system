# tuple packing
x = 1, 2, 3, 4, 5
# print(x, type(x))


# tuple unpacking
a, b, c = (1, 2, 3)
# print(a, b, c, type(a))



def magic():
    # tuple packing
    return 1, 2, 3, 4


# tuple unpacking
z, x, c, v = magic()
print(z, x, c ,v)




x = 1
y = 2

x, y = y, x

# def asd():
#     return 2, 1
#
# x, y = asd()
# print(x, y)


# a, b, c = (1, 2, 3, 4)
a, b, *r = (1, 2, 3, 4, 5)
*a, b, r = (1, 2, 3, 4, 5)
a, *b, r = (1, 2, 3, 4, 5)