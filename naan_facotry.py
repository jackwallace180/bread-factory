# functions
def make_dough(arg1, arg2):
    if (arg1 == 'water' and arg2 == 'wheat') or (arg1 == 'wheat' and arg2 == 'water'):
        return 'dough'
    else:
        return 'not dough'
def wood_oven(arg3):
    if arg3 == 'dough':
        return 'bread'
    else:
        return 'not bread'
# calling of functions

# tests TDD
print('Testing make dough, with wheat and water --> dough to come out')
print(make_dough('wheat', 'water') =='dough')

print('Testing make dough, with sand and cement --> not dough')
print(make_dough('sand', 'cement') =='not dough')

print('Testing wood_oven, with dough --> Bread to come out')
print(wood_oven('dough') == 'bread')

print('Testing wood_oven, with not dough --> not bread to come out')
print(wood_oven('not dough') == 'not bread')