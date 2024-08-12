my_dict = {'Mom': 890543402404,'Job': 87457845196, 'home': 87451288754}
print(my_dict)
print(my_dict['Mom'])
my_dict['Den'] = 7986453879465
print(my_dict['Den'])
my_dict.update({'Max': 46468527446, 'Nikita': 78925245})
print(my_dict)
del my_dict['Max']
print(my_dict)

my_set = {1,2,3,4,5,2,4,6,3,1,'live', 'drive'}
print(my_set)
my_set.update ({7,8,9})
print(my_set)
print(my_set.discard(2))
print(my_set)