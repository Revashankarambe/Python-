s1 = {1, 2, 4, 6}
s2 = {3, 5, 7}
print(s1.union(s2))
s1.update(s2)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2= {"seoul","kabul","Delhi"}
cities3= cities.difference(cities2)
print(cities3)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2= {"seoul","kabul","Delhi"} 
print(cities.issuperset(cities2))
cities3= {"Tokyo","Madrid","Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))