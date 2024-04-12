def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

print(middle('oi'))
print(middle('ovo'))

def is_palindrome(string):
    if len(string) <= 1: 
        return True
   
    if first(string) != last(string):
        return False
    
    return is_palindrome(middle(string))

# 6.4 - gpt
def is_power(a, b):
    if a == b:
        return True
    if a < b:
        return False
    if a%b == 0 and is_power(a/b, b):
        return True

        
print(f'''
{is_power(5,6)}
{is_power(6,6)}
{is_power(9,2)}
{is_power(10,2)}
''')

