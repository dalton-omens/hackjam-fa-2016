from get_genre_list import get_genre_list
from interest_suggestions import common_interests, suggestions

test = [['metal','pop'],['pop'],['pop'],['rap']]

num_users = input('How many of you are there?\n')
genre_list = get_genre_list()
shared_interest = common_interests(genre_list, test) #replace test with list of each user's preferences
suggestions(genre_list, shared_interest)