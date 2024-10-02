Score = 105

# if Score >= 101:
#   print("Wrong Grading!")
# elif Score >= 90 :
#   print("A Grade")
# elif Score >= 80:
#   print("B Grade")
# elif Score >= 70:
#   print("C Grade")
# elif Score >= 60:
#   print("D Grade")
# else:
#   print("F Grade")

if Score >= 101:
  print("Please verify your grade again")
  exit()

if Score >= 90 :
  grade = "A"
elif Score >= 80:
  grade = "B"
elif Score >= 70:
  grade = "C"
elif Score >= 60:
  grade = "D"
else:
  grade = "F"  

print("Grade ", grade)  