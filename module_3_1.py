calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(string):
    count_calls()
    dlina_str = len(string)
    caps = string.upper()
    low_er = string.lower()
    return (dlina_str, caps, low_er)
def is_contains(string, list_to_search):
    count_calls()
    string.upper()
    for i in range(len(list_to_search)):
        string_1 = (list_to_search[i])
        if string.upper() == string_1.upper():
            otvet = True
            break
        else:
            otvet = False
    return otvet
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Happy'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Litle', ['Lit', 'LitLE', 'tle']))
print(calls)