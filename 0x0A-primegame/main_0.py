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

print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
