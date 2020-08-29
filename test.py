def occurrences(arr, int):
  result = 0
  for i in range(len(arr)):
    if int == arr[i]:
      result += 1
  return result

arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]  
int = 2
print (occurrences(arr, int))

[i for in in ifilter(lambda x: x % 5, islice(count(5), 10)]