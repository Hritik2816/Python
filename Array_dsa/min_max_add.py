def minMaxAdd(A,N):
  if N == 1:
    return A[0]
  
  if A[0] > A[1]:
    maxi = A[0]
    mini = A[1]
  else:
    mini = A[0]
    maxi = A[1]

  for i in range(2,N):
    if A[i] > maxi:
      maxi = A[i]
    elif A[i] < mini:
      A[i] < mini

  return maxi+mini

result = minMaxAdd(145679,6)
print(result)
    