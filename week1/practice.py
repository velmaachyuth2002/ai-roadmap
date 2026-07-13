x=[1,2,3,4,5,6,0,0]
'''result=[i for i in x if i%2==0]
print(result)'''
'''words=["Hi","Bye","HELLO","HELLO"]
dict={w : len(words) for w in words }
set1={w.lower() for w in words}
print(dict)
print(set1)'''
'''for i,item in enumerate(x,start=2):
    print(i,item,end=" ")'''
y=[1,2,3,5,6,7,8]
'''for item1,item2 in zip(x,y):
    print(item1,item2)'''
'''dict2=dict(zip(x,y))
print(dict2)'''
'''scores = {
    ("aditya", "math"):    91,
    ("aditya", "physics"): 78,
    ("aditya", "chem"):    85,
    ("meera",  "math"):    88,
    ("meera",  "physics"): 94,
}
scoresa=scoresb=0
count1=0
count2=0
for (student, subject), score in scores.items():
    if student=="aditya":
        scoresa+=score
        count1+=1
    else:
        scoresb+=score
        count2+=1
print(scoresa/count1)
print(scoresb/count2)'''
def f(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
print(f(1))
print(f(2))
print(f(3,[4,5]))