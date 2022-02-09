# -------------------------------
# 早稲田理工のロト6に変換するやつ
# 初版
#
# shobon 2022/02/09
# -------------------------------


def cton(c):
	t=ord(c)
	for u,v in ([96,c],[103,"1"],[109,"2"],[115,"3"],[122,"4"]):
		if t<=u:return v
	return c

def waseda(s):
	m=1;r=[]
	for i in s:
		if i==" ":
			r.append(i)
			m=1
		elif m==1:
			r.append(i)
			m=0
		else:
			r.append(cton(i))
	return "".join(r)

print(waseda("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."))

"""
file = open("words.txt","r") #早稲田の
d = dict()
for word in file.readlines():
	targ = waseda(word.lower()[:-1])
	if targ not in d:
		d[targ] = []
	d[targ].append(word.lower()[:-1])

probdata = [
	["f4314233","f23413123","f133412","f332"],
	["t213243","t22131","t1122433","t1331"],
	["e321311","e33212","e31343111","e223134"],
	["a312134","a31134123","a13434","a1132231141"],
	["e2143123","e21311311","e233413","e2344"],
	["p1313321311","p3412112","p32422111","p13113411"],
	["c334214233","c11131","c33312343","c133114"],
	["c4331314","c332231324","c2133323","c1312331"],
	["m42132322","m232124321","m4312321","m13412"],
	["p221","p3221","p3243331","p222112"],
	["d434333121","d22232","d2333312","d1112131"],
	["a44321441","a3343231","a21331","a34333131"],
	["c213312","c333231342","c12113","c4342322121"],
	["i3334121112","i23212","i322124","i1231123241"],
	["p3344311","p23321","p1144","p331"]
]
for probnum, choices in enumerate(probdata):
	print(f"[{probnum+1}]")
	u = max([len(i) for i in choices])
	for cnum, t in enumerate(choices):
		if t not in d:
			print(f"{cnum + 1} {t.ljust(u)} (X) No data")
		else:
			print(f"{cnum + 1} {t.ljust(u)}  -> {' '.join([i for i in d[t]])}")
"""