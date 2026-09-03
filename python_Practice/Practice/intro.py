#Fetures Of String
# massage="""Booby's World
# cartoon in 1900 in childhood in past"""
# print(massage[0:7])
# print(massage.count("in"))
# print(massage.find("in"))
#
# greeting = 'hello'
# name = 'Ayon'
# wc ='Welcome To the World'
# pri='{}, {}, {}'.format(greeting,name.upper(),wc)
# print(len(pri))
# print(pri)
# print (dir(name))
# from os import name
# from turtledemo.penrose import start

#List
# course=['Math','English','History','French']
# course2=['Graphics','Physics']
# course.insert(0,course2)
# print(course)

# course.extend(course2)
# print(course)
#
# for index, item in enumerate(course,start=1):
#     print(index, item)
#
# course_join = (' -- '.join(course))
#
# print(course_join)
#
#
# new_split = course_join.split(' -- ')
# print(new_split)


# list1=['Math','English','History','French']
# list2=list1
#
# print(list1)
# print(list2)
#
# list1[0]='Science'
# print(list1)
# print(list2)

#Tuples

# tuples1=('Math','English','History','French','Math') # tuples are immutable
# tuples2=tuples1

# print(tuples1)
# print(tuples2)

# tuples1[0]='Science' # that's why it is invalid
# print(tuples1)
# print(tuples2)

#Set Practice

# arts_course = {'Bangla', 'English', 'History', 'French', 'English', 'History', 'French','Math'}
# science_course = {'Bangla', 'English', 'Geography', 'Science', 'Math', 'English'}
# new_courses= sorted(arts_course)
# print(new_courses)
# print(science_course)
# common_courses=science_course.intersection(arts_course)
# different_courses=science_course.difference(arts_course)
# all_courses=science_course.union(arts_course)
# print(common_courses)
# print(different_courses)
# print(all_courses)
#
# # Empty List,Tuples,set creation
#
# empty_list=[]
# empty_list= list()
#
# empty_tuple=()
# empty_tuple = tuple()
#
# empty_set ={} # not valid it is for dictionary
# empty_set = set()

# Dictionary

# student ={
#     'name':'Jhon','age':23,'course':['Bangla','English','Math']
# }
#
# student.update({'name':'Booby','age':25,'course':['Geography','Philosophy','History']}) # for update dictionary
#
# student['course'].remove('Philosophy') # remove any value from list
#
#
# student['marks']=87.34
# student['marks']=94.8 # for update dictionary
#
# del student['marks'] # for deleting value
#
# print(student['name'])
# print(student.get('age', None))
# print(student.get('marks', None))
# print(student.get('phone', None))
#
# for key,value in student.items():
#     print(key,':',value)

# print(student.keys())
# print(student.values())
# print(student.items())

#Conditions

# def function(greeting,name='Jhon'):
#     return (f"{greeting}, {name} Welcome to  new world")
#
# print(function('Hello'))

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# course=['Math','Art']
# info={'name':'Shakib','age':25,'marks':89}
# student_info(*course,**info) # one * for tuples and ** for DictionaryNatural


# month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

# def is_leap_year(year):
#     return  year%4==0 and (year%400==0 or year%100!=0)

# def days_in_month(month,year):

#     if not 1 <= month <= 12:
#         return 'Invalid month'
#     if month==2 and is_leap_year(year):
#         return 29
#     return month_days[month]

# print(is_leap_year(2024))
# print(days_in_month(1,2023))


# import my_moduls as m
#
# vari= m.test
#
# print(vari)
#
# course= ['Math','English', 'Art','Bangla']
#
# search= m.find_index(course,'Bangla')
#
# print(search)

# import random
# course= ['Math','English', 'Art','Bangla']
#
# random_course=random.choice(course)
# print(random_course)

# import datetime
#
# today = datetime.date.today()
# time = datetime.datetime.now().time()
# print(time)
# print(today)
#
# import calendar
# leap_year=calendar.isleap(2020)
# print(leap_year)

# import antigravity


# import os
# print(dir(os.getcwd()))

# i=100
# while i<=200:
#     print(i)
#     i+=20

# s1={1,2,3,4,5,6}
# s2={6,7,8,9}
# print(s1&s2)