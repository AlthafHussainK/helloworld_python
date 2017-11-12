def purify(numbers):
  even_list = []
  for i in numbers:
    if i % 2 == 0:
      even_list.append(i)
  return even_list