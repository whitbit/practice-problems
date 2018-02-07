# this solution uses extra memory
# to keep all characters present in string.

# Null terminating strings are not used in Java.
# For this question, assume that you are passed a
# null terminated string (array of characters).
def remove_duplicates_1(s):
  
  hashset = set([])

  write_index = 0
  read_index = 0

  while s[read_index] != '\0':
    if s[read_index] not in hashset:
      hashset.add(s[read_index])
      s[write_index] = s[read_index]
      write_index += 1

    read_index += 1

  s[write_index] = '\0'

s = "abbabcddbabcdeedebc"
remove_duplicates_1(s)
print s