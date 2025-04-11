s1 = {5,8,1,9}
s2 = set((8,4,1,90))

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1.difference(s2))
print(s2.difference(s1))