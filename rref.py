__author__ = 'LobaAjisafe'


x = [[1, 2, 3]]
ogx = x


def find_zero_maker(a, b):
    return b/a


def find_non_zero_index(a):
    """
    Finds non zero index
    :param a: list
    :return: int
    """
    for j in range(len(a)):
        if a[j] != 0:
            return j


def reduce_row(a, b):
    """
    :param a: list
    :param b: list
    :return: list
    """
    z = find_non_zero_index(a)
    c = find_zero_maker(a[z], b[z])
    new_list = []
    for i in range(len(a)):
        new_list.append(-c * a[i] + b[i])

    return new_list


def reduce_all_rows(a, b, c):
    """
    takes in reference row and all subsequent rows
    :param a: list
    :param b: list of lists
    :return: list of lists
    """
    new_list_of_lists = a
    for lis in c:
        new_list_of_lists.append(reduce_row(b, lis))

    return new_list_of_lists


def simplify_row(a):
    """
    :param a: list
    :return: list
    """
    z = find_non_zero_index(a)

    b = []
    for j in a:
        b.append(j/a[z])

    return b


def rref(a):
    for l in range(len(a)-1, -1, -1):
        z = find_non_zero_index(a[l])
        for k in range(l):
            b = find_zero_maker(a[l][z], a[k][z])
            new_list = []
            for j in range(len(a[l])):
                new_list.append(-b * a[l][j] + a[k][j])
            a[k] = new_list


for i in range(1, len(x)):
    x = reduce_all_rows(x[:i], x[i - 1], x[i:])

red_form = []
for i in x:
    red_form.append(simplify_row(i))


rref(red_form)

print(red_form)
print(ogx)



