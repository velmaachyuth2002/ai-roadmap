dataset = [
    {"text": "great film", "label": 1, "tokens": ["great", "film"]},
    {"text": "awful pacing", "label": 0, "tokens": ["awful", "pacing"]},
    {"text": "great great pacing", "label": 1, "tokens": ["great", "great", "pacing"]},
]
newdic={}
for items in dataset:
    newset=set(items["tokens"])
    for i in newset:
        if i in newdic:
            newdic[i]+=1
        else:
            newdic[i]=1
print(newdic)