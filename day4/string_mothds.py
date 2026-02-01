
# length
name1 = "Prashant"
print(len(name1))

name2 = "  Prashant  "
print(len(name2))

# name3 = input("enter your name: ")
# print(len(name3))

# upper case

city = "Pune"
print(city.upper())

country = "India"
print(country.upper())

# lower case

city = "Pune"
print(city.lower())

country = "India"
print(country.lower())

# title case

city = "new york"
print(city.title())

country = "united states of america"
print(country.title())

# strip

raw_name = "   Prashant   "
print(raw_name.strip())

raw_name2 = "###Prashant###"
print(raw_name2)
print(raw_name2.strip("#"))

print(type(raw_name))

multi_line_string ="this planet has—or rather had—a problem. which was\n\
this: most of the people living on it were unhappy for\n\
pretty much of the time. Many solutions were suggested\n\
for this problem, but most of these were largely con-\n\
cerned with the movements of small green pieces of\n\
paper, which is odd because on the whole it wasn’t the\n\
small green pieces of paper that were unhappy."

print(multi_line_string.capitalize())

poem_string ="""
    He worked by day and toiled by night,
        He gave up play and some delight.
    Dry books he read, new things to learn,
        And forged ahead, success to earn.
    He plodded on with faith and pluck,
        And when he won, men called it LUCK
"""

print(poem_string)