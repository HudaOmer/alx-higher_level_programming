#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
<<<<<<< HEAD
    return my_list.mul(2)
    #return [x * number for x in my_list]
=======
    return list(map(lambda x: x * number, my_list))
>>>>>>> af00a546715740c0343cdad75f9cd7ed1a5fb9eb
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
