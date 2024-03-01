# string masalalar
# 1-masala
def order(is_in_order):
    m = list(is_in_order)
    if m == sorted(is_in_order):
        print(True)
    else:
        print(False)


is_in_order = ("abc")
order(is_in_order)
# 2-masala
def convert(convert_to_decimal):
    natija = []
    for x in convert_to_decimal:
        y = x.replace("%", "")
        if type(y) == str:
            n = int(y)
            m = n / 100
            natija.append(m)
    print(natija)


convert_to_decimal = (["1%", "2%", "3%"])
convert(convert_to_decimal)
# 3-masala
# 4-masala
def greet(greet_people):
    lst = ["Hello " + x for x in greet_people]
    string = " ".join(lst)
    print(string)


greet_people = (["Joe"])
greet(greet_people)
# 5-masala
def remove(remove_vowels):
    natija = ""
    for x in remove_vowels:
        if x.lower() not in unli:
            natija += x
    print(natija)


unli = "i", "e", "a", "o", "u", "oʻ"
remove_vowels = ("I have never seen a thin person drinking Diet Coke.")
remove(remove_vowels)

# object masalalar
# 1-masala
# 2-masala
# 3-masala
def get(get_frequencies):
    set1 = {}
    for x in get_frequencies:
        if x in set1:
            set1[x] += 1
        else:
            set1[x] = 1
    return set1


get_frequencies = (["A", "B", "A", "A", "A"])
print(get(get_frequencies))
# 4-masala
def old(oldest):
    natija = 0
    for keys, values in oldest.items():
        if values > natija:
            natija = values
    print(natija)


oldest = ({
    "Max": 9,
    "Josh": 13,
    "Sam": 48,
    "Anne": 33
})
old(oldest)
old(oldest)
# 5-masala
def top(top_note):
    natija = {}
    for x, y in top_note.items():
        replac = x.replace("notes", "top_note")
        if type(y) == list:
            n = max(y)
            m = set(n)
        if x not in natija:
            natija[x] = m
    print(natija)


top_note = ({"name": "John", "notes": [3, 5, 4]})
top(top_note)