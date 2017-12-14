import sys

university_final_vote = int(sys.argv[1])


def hire_or_not(vote):
  we_can_hire_him = False
  if university_final_vote > 110:
    we_can_hire_him = True
  return we_can_hire_him
  
university_final_vote = int(sys.argv[1])

print hire_or_not(university_final_vote)
