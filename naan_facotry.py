# functions
def make_dough(ingredient1, ingredient2):
    if (ingredient1 == 'water' and ingredient2 == 'wheat') or (ingredient1 == 'wheat' and ingredient2 == 'water'):
        return 'dough'
    else:
        return 'not dough'

def wood_oven(ingredient):
    if ingredient == 'dough':
        return 'bread'
    else:
        return 'not bread'
    
def run_factory(ingredient1, ingredient2):
    dough_r = make_dough(ingredient1, ingredient2)
    result_bread = wood_oven(dough_r)
    return result_bread
print(run_factory('wheat', 'water'))
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

print('Testing wood_oven, with not dough --> not bread to come out')
print(wood_oven('dough') == 'not bread')