def linear_search_dictionary(dictionary, target):
    for key, value in dictionary.items():
        if value == target:
            print(f'{target} found at key {key}')
            return key
    else:
        print(f'Target ({target}) not found in the dictionary.')
        return None

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)


    
