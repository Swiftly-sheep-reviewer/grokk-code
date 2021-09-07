def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  left, right = 0, len(arr)-1
  while left <= right:
    if arr[left] + arr[right] == target_sum:
      return [left, right]
    elif arr[left] + arr[right] > target_sum:
      right -= 1
    else:
      left += 1
  return [-1, -1]