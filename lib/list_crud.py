
def create_an_empty_list():
    return list ()

def create_a_list():
    new_list = [1, 2, 3, 4]
    return new_list

def add_element_to_end_of_list(l, element):
    new_list = l.copy()
    new_list.append(element)
    return new_list

def add_element_to_start_of_list(l, element):
    new_list = l.copy()
    new_list.insert(0, element)
    return new_list

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    new_l = l.copy()
    return new_l.pop(0)

def retrieve_element_from_index(l, index):
    return l.pop(index)

def retrieve_last_element_from_list(l):
    return l.pop()
