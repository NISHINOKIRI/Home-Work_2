# 1. Пользователь подаёт на ввод список из чисел, необходимо вывести список, состоящий только из чётных чисел (append)

nums = [1, 2, 3, 4, 5, 6]


def get_even_nums_list(nums: list) -> list:
    return [num for num in nums if not num % 2]


# 2. Пользователь вводит слово, необходимо проверить, является ли слово палиндромом шалаш | шалаш



def is_palindrome(check_word: str) -> bool:
    return check_word == check_word[::-1]

# 3. Необходимо написать функцию, принимающую на вход список чисел. Она обрабатывает его и возвращает суммы пар чисел:
# << [1,2,3,4,5,6]
# >> [3,7,11]
# Если передано не чётное количество чисел для составления пар, последнее число не учитывается


def sum_nums(nums: list) -> list:
    nums_complete = []
    for i in range(0, len(nums) - 1, 2):
        print(nums[i:i + 2])
        nums_complete.append(sum(nums[i:i + 2]))
    print(nums_complete)
    # return [sum(nums[i:i + 2]) for i in range(0, len(nums) - 1, 2)]

sum_nums(nums)