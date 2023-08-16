#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [x if x != search else replace for x in my_list]
    return new_list

# Example usage
if __name__ == "__main__":
    initial_list = [1, 2, 3, 4, 3, 5, 3]
    search_element = 3
    replace_element = 0
    
    modified_list = search_replace(initial_list, search_element, replace_element)
    print(modified_list)

