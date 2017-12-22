#list-mutable(updatable)
#tuple-immutable
tuple=()

tup1=("physics","chemistry",192,193)

tup2=(1,2,3,4,5)

tup3=("a","b","c","d","e")

tup4=(50,)

print tup1[0]
print tup2[1:5]

tup1[1]="maths"#non updatable changes in object

tup3=tup1+tup2
print tup3

del tup3
print tup3

#set
bri=set(["india","russia","states"])

"india" in bri
"usa" in bri

bric=bri.copy()
print bric

bric.add("china")
print bric

bric.issuperset(bri)#

bric.remove("china")
print bric
