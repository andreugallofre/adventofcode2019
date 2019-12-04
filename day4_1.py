def is_valid_password(number):
    if has_duplicated(number) and always_increase(number):
        return True
    return False


def has_duplicated(number):
    str_num = str(number)

    ocurrences = {}
    for i in str_num:
        try:
            ocurrences[i] = ocurrences[i] + 1
            return True
        except:
            ocurrences[i] = 1

    return False


def always_increase(number):
    str_num = str(number)

    old = str_num[0]
    for i in str_num[1:]:
        if i < old:
            return False
        old = i

    return True


initial_puzzle = 172930
end_puzzle = 683082

valid_passwords = 0
for i in range(initial_puzzle, end_puzzle):
    if is_valid_password(i):
        valid_passwords += 1

print(valid_passwords)
