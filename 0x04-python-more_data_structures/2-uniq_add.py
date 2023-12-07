def uniq_add(my_list=[]):
    uniq_integers = set()
    for num in my_list:
        if num not in uniq_integers:
            uniq_integers.add(num)
    return sum(uniq_integers)
