import webbrowser

def common_interests(genre_list, preferences):
	preferences_list = []
	for person in preferences:
		preferences_list += person
	shared_interest = max(set(preferences_list), key=preferences_list.count)
	print('Your group enjoys' + ' ' + shared_interest + ' ' + genre_list[-1].lower())
	return shared_interest

def suggestions(genre_list, shared_interest):
	suggested_site = []
	if genre_list[-1] == 'Music':
		suggested_site = 'https://play.spotify.com/search/' + shared_interest
	elif genre_list[-1] == 'Movies':
		suggested_site = 'http://www.metacritic.com/browse/movies/genre/metascore/' + shared_interest
	elif genre_list[-1] == 'Games':
		suggested_site = 'http://www.metacritic.com/browse/games/genre/metascore/' + shared_interest
	elif genre_list[-1] == 'Restaurants':
		city = input('What city are you in?\n')
		state = input('What state are you in? Use state abbreviations only: (Ex.CA)\n')
		suggested_site = 'https://www.yelp.com/search?find_desc=' + shared_interest + '&find_loc=' + city + ',' + state + shared_interest

	print(shared_interest, suggested_site)
	suggested_print = ('For ' + shared_interest + ' suggestions, Go to ' + suggested_site)
	print(suggested_print)
	webbrowser.open(suggested_site)

