#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner
check_prime = __import__('0-prime_game').check_prime

# print('0', check_prime(0))
# print('1', check_prime(1))
# print('2', check_prime(2))
# print('3', check_prime(3))
# print('4', check_prime(4))
# print('27', check_prime(27))
# print('19', check_prime(19))

print("isWinner(0, [0]): {}".format(isWinner(0, [0])))
print("isWinner(-1, [10]): {}".format(isWinner(-1, [10])))
print("isWinner(3, [4, 5, 1]): {}".format(isWinner(3, [4, 5, 1])))
print("isWinner(5, [2, 5, 1, 4, 3]): {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]): {}"
        .format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
