#consecctive  duplicate detector
"""accept N number,display only those number that appear consecatively. more than one 
example:12234445 and 
output:-2 
        4  give this expleneson for easy way in pythone programing"""

n=[1,2,2,3,4,4,4,5]
dup = []
for i in n:
    if n.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)               