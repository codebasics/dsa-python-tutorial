# 2. You have a list of your favourite marvel super heros.
# ```
# heros=['spider man','thor','hulk','iron man','captain america']
# ```
# Using this find out,
#     1. Length of the list
#     2. Add 'black panther' at the end of this list
#     3. You realize that you need to add 'black panther' after 'hulk',
#        so remove it from the list first and then add it after 'hulk'
#     4. Now you don't like thor and hulk because they get angry easily :)
#        So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#        Do that with one line of code.
#     5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# You have a list of your favourite marvel super heros. 
heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out
# 1. Length of the list
print(f'1. length of {heros} is {len(heros)}')

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(f'2. Adding \'black panther\' at the end of the list: {heros}')

# 3. You realize that you need to add 'black panther' after 'hulk',
#  so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(f'3. Adding \'black panther\' after hulk: {heros}')

# 4. remove thor & hulk, add 'captain strange' in their place
heros[1:3]=['doctor strange']
print(f'4. Replace thor & hulk with \'captain strange:\' {heros}')

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(f'5. sorted list: {heros}')

