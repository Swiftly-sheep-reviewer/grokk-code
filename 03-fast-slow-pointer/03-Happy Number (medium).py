def find_happy_number(num):
    # TODO: Write your code here
    slow = fast = num
    while True:
        slow = find_square_num(slow)
        fast = find_square_num(find_square_num(fast))
        if slow == fast:
            break
    return slow == 1


def find_square_num(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num = num // 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
