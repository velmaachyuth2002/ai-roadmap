user = {"name": "aditya", "tags": ["ml"]}
def add_tag(tags):
    list2=tags.copy()
    list2.append("new")
    return list2
print(user)
lis1=user["tags"]
list3=add_tag(lis1)
print(user)

print(f"id(lis1): {id(list3)}")
print( id(user["tags"]))
