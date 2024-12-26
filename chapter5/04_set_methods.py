s1 = {1, 5, 32, 45, "liza"}
s2 = {"liza", 3, 5, 6}
print(s1, type(s1))
print(len(s1))
s1.add("kapopara")

print(s1)
print(s1, type(s1))

s1.remove("liza")
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)

# print(s1.difference(s2))

set1 = {1, 5, 32, 45, "liza"}
set2 = {"liza", 3, 5, 6}
print(set1.difference(set2))
print(set1.union(set2))
print(set1.intersection(set2))