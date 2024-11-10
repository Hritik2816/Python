
#Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

original_string = "Using Recursion"
reversed_string = reverse_string(original_string)
print(reversed_string)

#Using a Loop
original_string = "Using a Loop"
reversed_string = ''
for char in original_string:
    reversed_string = char + reversed_string
print(reversed_string)  # Output: !dlroW ,olleH

#slice method
def revSlice(s):
  k = s[::-1]
  return k
result = revSlice('Hritik')
print(result)