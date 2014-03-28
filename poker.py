import random

def pair(cards):
	cardpair=""
	for a in cards:
		if (cards.count(a)>1):
			cardpair=a #TODO put a condition to find the bigger pair
	if cardpair=="":
		cardpair=0
		return cardpair
	else:
		return cardpair

def twopair(cards):
	check = pair(cards)
	pairs=[]
	if check==0:
		pairs=0
		return pairs
	else:
		pairs.append(check)
		#print cards
		for a in range(0, 2):
			index1 = cards.index(check)
			del cards[index1]
		check = pair(cards)
		if check==0:
			pairs = 0
			return pairs
		else:
			pairs.append(check)
			return pairs
	
def three(cards):
	check = 0
	card = ""
	for a in cards:
		if (cards.count(a)==3):
			check = 1
			card = a
	if check==0:
		return check
	else:
		return card

def checker(cards):
	winning={'pair':pair(cards), 'twopair':twopair(cards), 'three':three(cards)}
	print winning

def generatecard():
	shades={'s':'Spades', 'c':'Clubs', 'h':'Hearts', 'd':'Diamonds'}
	card = shades[random.choice(shades.keys())]+" "+str(random.randrange(1, 13))
	return card

def playing():
	cards=[]
	while(True):
		temp=generatecard()
		if not temp in cards:
			cards.append(temp)
		else:
			True
		if len(cards)==2:
			break
	print ("Your cards are "+ cards[0]+ ", "+cards[1])
	for i in range(0, 5): #generating other cards
		cards.append(generatecard())
		if i>=2:
			print ("The cards are : "+str(cards[2:i+3]))
			while(True):
				cont = raw_input("Enter 'c' to continue playing or enter 'f' to fold: ")
				if cont=='c':
					break
				elif cont=='f':
					return
				else:
					True
	print("")
	checker(cards)

playing()
print ("Thank you for playing.")	
