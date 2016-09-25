from get_genre_list import get_genre_list
from interest_suggestions import common_interests, suggestions
from make_preferences import make_preferences

num_users = input('\nHow many of you are there? Please enter a number.\n')
correct = False
while not correct:
  try:
    int(num_users)
    correct = True
  except NameError:
    num_users = input('Please input a number. (Ex.4)')
genre_list = get_genre_list()
preferences = make_preferences(genre_list, num_users)
shared_interest = common_interests(genre_list, preferences) #replace test with list of each user's preferences
suggestions(genre_list, shared_interest)
