"""
1. Add up and print the sum of the all of the minimum elements of each inner array. 
Each array may contain additional arrays nested arbitrarily deep, 
in which case the minimum value for the nested array should be added to the total.
[
  [8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18],
]
The expected output for the above input is:
8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""
"""
2. Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, 
each on a separate line. If the word has an even number of letters, choose the later letter, 
i.e. the one closer to the end of the string.
['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
The expected output is:
'Cha Cha'
'Paso Doble'
'Viennese Waltz'
'Waltz'
'Samba'
'Rumba'
'Tango'
'Foxtrot'
'Jive'
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""
"""
3. Given an object/dictionary with keys and values that consist of both strings and integers, 
design an algorithm to calculate and return the sum of all of the numeric values.
For example, given the following object/dictionary as input:
{
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
Your algorithm should return 41, the sum of the values 23 and 18.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

def foot(object):
    # get a list of values
    values = object.values()
    # holds our total
    total = 0
    # iterate through our list of values
    for value in values:
        # if it's some sort of number
        if type(value) == int or type(value) == float:
            total = total + value

    return total

d = {
        "cat": "bob",
        "dog": 23,
        19: 18,
        90: "fish"
    }   

print(foot(d))

"""
4. Given a hashmap where the keys are integers, print out all of the values of the hashmap in reverse order, 
ordered by the keys.
For example, given the following hashmap:
{
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}
The expected output is:
widescreen
views
tissue
coffee
inbox
vs code
alloc
bottle
window
since "widescreen" has the largest integer key, "views" has the second largest, etc.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""
