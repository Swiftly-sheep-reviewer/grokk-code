def make_squares(arr):
    squares = [0] * len(arr)
    # TODO: Write your code here
    n = len(squares) - 1
    left, right = 0, len(arr) - 1
    while left <= right and n >= 0:
        if arr[left] ** 2 > arr[right] ** 2:
            squares[n] = arr[left] ** 2
            left += 1
        else:
            squares[n] = arr[right] ** 2
            right -= 1
        n -= 1
    return squares
