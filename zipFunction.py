roll=[101,102,103,104,105,106,107,108,109,110]
name=["John","Jane","Mike","Alice","Bob","Charlie","David","Eva","Frank","Grace"]
height=[5.9, 5.7, 6.0, 5.5, 5.8, 6.1, 5.6, 5.4, 6.2, 5.3]
weight=[160, 150, 180, 140, 170, 200, 155, 145, 190, 135]
# The zip() function takes two or more iterables (in this case, the roll and name lists) and returns an iterator of tuples, where the first item in each passed iterator is paired together, the second item in each passed iterator is paired together, and so on. The result is an iterator of tuples, where each tuple contains one element from each of the input iterables.
#
# The zip() function is useful when you want to combine multiple lists or iterables into a single iterable, allowing you to iterate over them in parallel. In this example, we are using the zip() function to combine the roll numbers and names into a single iterable of tuples, which we then convert to a list and print.
zipped_list = list(zip(roll, name, height, weight,"ABCDABCDAB")) #section "ABCDABCDAB" is added to show that zip function will only take the minimum length of the iterable and ignore the rest of the elements in the longer iterable.
print("Zipped list: ", zipped_list)