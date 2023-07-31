mydict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
a=list(mydict)
a.sort()
sorted_dict= {i: mydict[i]for i in a}
print(sorted_dict)