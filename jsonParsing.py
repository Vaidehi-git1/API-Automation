import json

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'
dict_courses = json.loads(courses)
# take json code in a variable as string, cause there's a method called 'loads' in
# jason which splits string into lists format.

# dict_courses = {"name": "RahulShetty", "languages": [ "Java", "Python"]}
print(type(dict_courses))
# list_languages = dict_courses["languages"]
# print(list_languages[0])

print(dict_courses["languages"][0])


# open Json file, read it and print 2nd course name.

with open("C:\\Users\\vtadu\\Downloads\\courses.json") as f:
    dict_courses = json.load(f)
    print(dict_courses)
    print(type(dict_courses))
    print(dict_courses['Courses'][1]['title'])
    print(dict_courses['Dashboard']['website'])

# If the items in list appears anywhere in the dict and print 3rd item.

print(dict_courses['Courses'])
list_dictCourses = dict_courses['Courses']
print(type(list_dictCourses))
for course in list_dictCourses:
    print(course)
    if course['title'] == 'ROA':
        print("ROA course price is: ", course['price'])
        assert course['price'] == 45

# Comparing 2 Json files.

with open("C:\\Users\\vtadu\\Downloads\\courses1.json") as fi:
    dict_courses2 = json.load(fi)
    assert dict_courses == dict_courses2


