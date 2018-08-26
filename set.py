# sets in python are a collection of unique elements
my_set = set()
my_set.update([1,2,3,4])
my_set.add(0)
print('my_set', my_set)

your_set = {5,6,3,4}
your_set.add(7)
print('your_set', your_set)

our_intersected_set = my_set.intersection(your_set)
print('our_intersected_set', our_intersected_set)
