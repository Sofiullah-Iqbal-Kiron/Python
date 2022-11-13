# Dictionary is defined with a set of curly brace. "{}"
# defaultdict is a subclass of class "dict".

from collections import defaultdict

print("Is defaultdict subclass of dict? ", issubclass(defaultdict, dict), '.', sep='')

a_dict = dict()
a_dict['Kiron'] = 65
a_dict[65] = 'Kiron'
a_dict.setdefault(65, 'Nirob')
print(a_dict.get(65))
