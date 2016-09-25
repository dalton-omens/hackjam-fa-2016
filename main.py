from get_genre_list import get_genre_list
from interest_suggestions import common_interests, suggestions
from make_preferences import make_preferences

num_users = input('\nHow many of you are there?\n')
genre_list = get_genre_list()
preferences = make_preferences(genre_list, num_users)
shared_interest = common_interests(genre_list, preferences) #replace test with list of each user's preferences
suggestions(genre_list, shared_interest)