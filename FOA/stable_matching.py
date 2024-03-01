# # Initialization
# men = ['Mike', 'Harvey', 'Louis', 'Jeff']
# women = ['Rachel', 'Donna', 'Sheila', 'Jessica']

# # Preferences
# men_pref = {  # indicates the preferences of the men
#   'Mike': ['Rachel', 'Jessica', 'Donna', 'Sheila'],
#   'Harvey': ['Donna', 'Jessica', 'Rachel', 'Sheila'],
#   'Louis': ['Sheila', 'Donna', 'Jessica', 'Rachel'],
#   'Jeff': ['Rachel', 'Jessica', 'Donna', 'Sheila']
# }

# women_pref = {  # indicates the preferences of the women
#   'Rachel': ['Mike', 'Jeff', 'Harvey', 'Louis'],
#   'Donna': ['Harvey', 'Louis', 'Mike', 'Jeff'],
#   'Jessica': ['Mike', 'Harvey', 'Louis', 'Jeff'],
#   'Sheila': ['Louis', 'Jeff', 'Harvey', 'Mike']
# }

# men = ['X', 'Y', 'Z']
# women = ['A', 'B', 'C']

# men_pref = {'X': ['A', 'B', 'C'], 'Y': ['B', 'A', 'C'], 'Z': ['A', 'B', 'C']}

# women_pref = {'A': ['Y', 'X', 'Z'], 'B': ['X', 'Y', 'Z'], 'C': ['X', 'Y', 'Z']}

men = ['ryan', 'josh', 'blake', 'connor']
women = ['lizzy', 'sarah', 'zoey', 'daniella']
men_pref = {
  'ryan': ['lizzy', 'sarah', 'zoey', 'daniella'],
  'josh': ['sarah', 'lizzy', 'daniella', 'zoey'],
  'blake': ['sarah', 'daniella', 'zoey', 'lizzy'],
  'connor': ['lizzy', 'sarah', 'zoey', 'daniella']
}

women_pref = {
  'lizzy': ['ryan', 'blake', 'josh', 'connor'],
  'sarah': ['ryan', 'blake', 'connor', 'josh'],
  'zoey': ['connor', 'josh', 'ryan', 'blake'],
  'daniella': ['ryan', 'josh', 'connor', 'blake']
}

temp_men_pref = men_pref.copy()

free_men = list(men)
free_women = list(women)

match = {'ryan': '', 'josh': '', 'blake': '', 'connor': ''}

# match = {'Mike': '', 'Harvey': '', 'Louis': '', 'Jeff': ''}
# match = {'X': '', 'Y': '', 'Z': ''}

while free_men:
  man = free_men[0]
  woman = temp_men_pref[man][0]
  print("Current Man", man)
  print("Current Woman", woman)
  if woman in free_women:
    match[man] = woman
    free_men.remove(man)
    free_women.remove(woman)
    temp_men_pref[man].remove(woman)
    print("Both man and women are free so matched")
  else:
    current_husband = [k for k, v in match.items() if v == woman][0]
    if women_pref[woman].index(man) < women_pref[woman].index(current_husband):
      free_men.remove(man)
      match[man] = woman
      free_men.append(current_husband)
      match[current_husband] = ''
      print("Women prefers man to her current husband")
    else:
      temp_men_pref[man].remove(woman)
      print("Woman rejects man")

print(match)
