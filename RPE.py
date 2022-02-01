import time
def rpn(s):
	lex=parse(s)
	s2=[]
	r= ""
	operations=["+","-","*","/","(",")"]
	for a in lex:
		if a=="(":
			s2=[a]+s2
		elif a in operations:
			if s2==[]:
				s2=[a]
			elif a==")":
				while(True):
					q=s2[0]
					s2=s2[1:]
					if q=="(":
						break
					r+=q + " "
			elif check(s2[0]) < check(a):
				s2=[a]+s2
			else:
				while(True):
					if s2==[]:
						break
					q=s2[0]
					r+=q + " "
					s2=s2[1:]
					if check(q)==check(a):
						break
				s2=[a]+s2
		else:
			r+=a + " "
	while(s2 != []):
		q=s2[0]
		r+=q + " "
		s2=s2[1:]
	return r

def check(o):
	if o=="+" or o=="-":
		return 1
	elif o=="*" or o=="/":
		return 2
	elif o=="(":
		return 0

def parse(s):
	delims=["+","-","*","/","(",")"]
	lex=[]
	tmp=""
	for a in s:
		if a != " ":
			if a in delims:
				if tmp != "":
					lex+=[tmp]
				lex+=[a]
				tmp=""
			else:
				tmp+=a
	if tmp != "":
		lex+=[tmp]
	return lex


formula = input()

rpnstck = rpn(formula)
print(rpnstck)
sum = eval(formula)
print(sum)
time.sleep(10)
