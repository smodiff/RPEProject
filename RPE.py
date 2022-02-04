import time
class ReversePolishNotation(object):
	
	def checkPriority(self, o):
		if o=="+" or o=="-":
			return 1
		elif o=="*" or o=="/":
			return 2
		elif o=="(":
			return 0

	def calculate(self, s):
		s = s.replace(" ", "")
		s2=[]
		r= ""
		operations=["+","-","*","/","(",")"]
		for a in s:
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
				elif self.checkPriority(s2[0]) < self.checkPriority(a):
					s2=[a]+s2
				else:
					while s2 != []:
						q=s2[0]
						r+=q + " "
						s2=s2[1:]
						if self.checkPriority(q) == self.checkPriority(a):
							break
					s2=[a]+s2
			else:
				r+=a + " "
	
		for i in range(0, len(s2)): r+=s2[i] + " "
		summ = eval(s)
		return r,summ


formula = input()

rpn = ReversePolishNotation()
rpnstck, summ = rpn.calculate(formula)

print(rpnstck)
print(summ)

time.sleep(20)
