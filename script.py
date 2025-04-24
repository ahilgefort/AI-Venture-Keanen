
def sort_decreasing(numbers):
  """Sorts a list of numbers in decreasing order.

  Args:
    numbers: A list of numbers to be sorted.

  Returns:
    A new list containing the numbers sorted in decreasing order.
  """
  return sorted(numbers, reverse=True)

if __name__ == '__main__':
  numbers = [5, 2, 8, 1, 9, 4]
  sorted_numbers = sort_decreasing(numbers)
  print(sorted_numbers)

