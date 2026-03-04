# print(bin(-6))
w="add s1,s2,s3"
w=w.split()
def corr(string:str) -> str:
        while(string[-1] == ","):
                string  = string[:-1]
        return string
print(w)
print(w[0])
print(w[1])
wt=w[1].split(",")
print((wt))
p="sw s1,32(sp)"
p=p.split()
print(p)
pt=p[1].split(",")
print(pt)
pt2=pt[1].split("(")
print(pt2)
pt3=pt2[1].strip(")")
print(type(pt3))
