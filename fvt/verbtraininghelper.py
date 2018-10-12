# 
# the verbtraininghelper.py module implements features like:
# - loading all verbforms of all verbs in a dictionary as follows: 
#           d = { "some verbform": 0, "another verbform": 2, ..., "yet another verbform": 1 }
#   every value of every key value pair is initially set to zero
#    
# - checking if user has typed a given verbform correctly three consecutive times. If not 
#   then the value in the dict above is set to zero. When value reaches 3 (the user has 
#   typed in the correct given verbform three consecutive times) the key value pair of that
#   verbform should be removed from the dictionary.
#