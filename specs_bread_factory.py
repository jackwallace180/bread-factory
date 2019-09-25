from bread_functions import *

print('Testing make dough, with wheat and water --> dough to come out')
print(make_dough('wheat', 'water') =='dough')

print('Testing make dough, with sand and cement --> not dough')
print(make_dough('sand', 'cement') =='not dough')

print('Testing wood_oven, with dough --> Bread to come out')
print(wood_oven('dough') == 'bread')

print('Testing wood_oven, with not dough --> not bread to come out')
print(wood_oven('not dough') == 'not bread')

print('Testing wood_oven, with not dough --> not bread to come out')
print(wood_oven('dough') == 'not bread')