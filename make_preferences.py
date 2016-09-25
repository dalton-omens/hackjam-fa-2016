def make_preferences(genre_list, num_users):
    def prompt():
        print('What are you interested in? Here are your options: If you\'re done, type \"Done\".')
        lst = ''
        for i in range(len(genre_list) - 2):
            lst = lst + genre_list[i] + ', '
        lst = lst[:-2] + '\n'
        return input(lst).strip()
    preferences = []
    for user in range(num_users):
        print('User ' + str(user + 1) + ':')
        user_preferences = []
        done = False
        while not done:
            new_preference = prompt()
            if new_preference in genre_list and new_preference not in genre_list[:-3:-1] and new_preference not in user_preferences:
                user_preferences += [new_preference]
            elif new_preference == 'Done' or new_preference == "done":
                done = True
            else:
                print('Please type a valid new word in the list.')
        preferences += [user_preferences]
    return preferences

