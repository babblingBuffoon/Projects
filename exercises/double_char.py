"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
Examples (Input -> Output):

* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "

"""


def double_char(s):
    l = []
    for element in s:
        l.append(element+element)
    st = ''.join(l)    
    return (st)


def double_char2(s):
    return "".join(c+c for c in s)

print(double_char2('some text'))
print(double_char('some text'))