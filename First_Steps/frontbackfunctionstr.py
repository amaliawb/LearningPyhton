def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]
  return str[len(str)-1] + mid + str[0]

str = input()
print(front_back(str))

#last char is len -1 because length is from 1 but index is from 0
