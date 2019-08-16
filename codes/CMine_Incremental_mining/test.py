old_list = ['3', '8', '35', '9', '1', '30', '33', '42', '10', '34', '63', '37', '36', '65', '23', '81', '62', '11', '92', '53', '70', '172', '60', '139', '74', '98', '61', '109', '86', '229', '96', '83', '17', '157', '16']
new_list = ['3', '8', '35', '9', '1', '30', '33', '42', '10', '34', '37', '36', '65', '63', '81', '23', '62', '92', '53', '11', '70', '172', '60', '139', '61', '98', '74', '109', '229', '83', '86', '157', '17', '96', '16']
print "old",old_list
print "new",new_list
ans = 0
for i in range(len(new_list)):
    item = new_list[i]
    l_set = set(new_list[:i])
    r_set = []
    for j in old_list:
        if item==j:
        	break
        else:
        	r_set.append(j)
    r_set = set(r_set)
    if item not in old_list:
        r_set = set([])
    commset = l_set.intersection(r_set)
    ans += (2**(len(l_set))) - (2**(len(commset)))
    print item
    print l_set
    print r_set
    print commset
    print ans
