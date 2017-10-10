import copy

"""basic type"""
my_num = 1
my_string = 'This is strig'


"""sequence type"""
my_tuple = (1,2,3)
my_list = [1,2,3]
my_set = {my_num,my_string,my_tuple}
my_dict = {'number':my_num,'string': my_string,'tuple':my_tuple}


"""Type"""
print('{0:=^60}'.format('Type'))
print("my_num's type({}) is same with int? {}".format(type(my_num),isinstance(my_num,int)))
print("my_str's type({}) is same with str? {}".format(type(my_string),isinstance(my_string,str)))
print("my_tuple's type({}) is same with tuple? {}".format(type(my_tuple),isinstance(my_tuple,tuple)))
print("my_list's type({}) is same with list? {}".format(type(my_list),isinstance(my_list,list)))
print("my_set's type({}) is same with set? {}".format(type(my_set),isinstance(my_set,set)))


"""Mutable or Immutable"""
print('{0:=^60}'.format('Mutable or Immutable'))
print('string is Immutable: {}'.format(my_string[1]))
#my_string[1] = 'a' #Immutable

print('tuple is Immutable: {}'.format(my_tuple[1]))
#my_tuple[1] = 40 #Immutable

befor_change_list = copy.deepcopy(my_list)
my_list[1] = 40
print('list is Mutable: {} to {}'.format(befor_change_list,my_list))

befor_change_set = copy.deepcopy(my_set)
my_set.update(my_list)
print('set is Mutable: {} to {}'.format(befor_change_set,my_set))

print('dictionary is part of set')


"""swap in python"""
print('{0:=^60}'.format('swap in python'))
my_name = 'rabob'; my_age = 25
print ('I\'m {} {} year\'s old'.format(my_name,my_age))
my_name,my_age = my_age,my_name
print ('I\'m {} {} year\'s old'.format(my_name,my_age))


"""list calculate"""
print('{0:=^60}'.format('list calculate'))
print('Sum of list : {}'.format(sum(my_list)))
print('min value of list : {}'.format(min(my_list)))
print('max value of list : {}'.format(max(my_list)))
print('length of list : {}'.format(len(my_list)))


"""property of set"""
print('{0:=^60}'.format('property of set'))
the_set = {1,2,3,4,5,6,1,2,3}
print ('set doesn\'t allow overlap{}'.format(the_set))
#print (the_set[1]) #set doesn't support indexing (set doesn't have order)
add_tuple = ('this','is','tuple')
the_set.add(add_tuple)
print ('This is set.add():{}'.format(the_set))
add_list = ['this','is','tuple']
#the_set.add(add_list) #set's element must Immutable
