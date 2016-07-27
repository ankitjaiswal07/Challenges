"""Solution of Maximum subarray problem.
Maximum subarray problem is the task of finding the contiguous
subarray within a one-dimensional array of numbers which has the largest
sum.
For example, for the sequence of values -2, 1, -3, 4, -1, 2, 1, -5, 4
the contiguous subarray with the largest sum is 4, -1, 2, 1, with sum 6.
"""


def find_max_sub_array(ls):
  """Finds a subarray with maximum sum.
  Args:
    ls: List for which maximum sub array is to be found.
  Returns:
    starting index of sub array.
    ending index of sub array.
    sum of the sub array.
  Raises:
    ValueError: if list is empty.
  """

  if not ls:
    raise ValueError("Empty Array")
  if len(ls) == 1:
    return 0, 0, ls[0]

  i = start = finish = temp_sum = max_sum = 0
  for j in range(len(ls)):
    temp_sum += ls[j]
    if temp_sum < 0:
      temp_sum = 0
      i = j+1

    if temp_sum > max_sum:
      max_sum = temp_sum
      start = i
      finish = j
  return start, finish, max_sum
