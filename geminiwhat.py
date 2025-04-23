
def sort_numbers(numbers):
  """Sorts a list of numbers in ascending order.

  Args:
    numbers: A list of numbers to be sorted.

  Returns:
    A new list containing the numbers from the input list, sorted in
    ascending order.
  """
  return sorted(numbers)

if __name__ == '__main__':
  # Example usage:
  numbers = [5, 2, 8, 1, 9, 4]
  sorted_numbers = sort_numbers(numbers)
  print(f"Original numbers: {numbers}")
  print(f"Sorted numbers: {sorted_numbers}")

  numbers2 = [3.14, 1.618, 2.718]
  sorted_numbers2 = sort_numbers(numbers2)
  print(f"Original numbers: {numbers2}")
  print(f"Sorted numbers: {sorted_numbers2}")

  numbers3 = []
  sorted_numbers3 = sort_numbers(numbers3)
  print(f"Original numbers: {numbers3}")
  print(f"Sorted numbers: {sorted_numbers3}")
