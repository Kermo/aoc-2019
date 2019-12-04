password_range = "273025-767253".split("-")


def decreasing(password):
    for x in range(1, len(password)):
        if int(password[x] < password[x -1]):
            return True

    return False

def has_single_duplicate_numbers(password):
    return sorted([str(password).count(c) for c in set(str(password))])[-1] > 1

def has_double_duplicate_numbers(password):
    return 2 in [str(password).count(c) for c in set(str(password))]


def count_different_password(password_range, part):
    possible_password = 0

    for i in range(int(password_range[0]), int(password_range[1])):

        if part == 1:
            if not decreasing(str(i)) and has_single_duplicate_numbers(i):
                possible_password += 1
        else:
            if not decreasing(str(i)) and has_double_duplicate_numbers(i):
                possible_password += 1

    return possible_password


print("Part 1: " + str(count_different_password(password_range, 1)))
print("Part 2: " + str(count_different_password(password_range, 2)))