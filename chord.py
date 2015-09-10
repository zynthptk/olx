pitch = {
	'c':0,
	'c#':1,
	'd':2,
	'd#':3,
	'e':4,
	'f':5,
	'f#':6,
	'g':7,
	'g#':8,
	'a':9,
	'a#':10,
	'b':11,
}
steps = {
	'maj':[4,7],
	'min':[3,7],
	'dim':[4,6],
	'aug':[4,8]
	}	
def get_root(prompt):
	for x in pitch:
		if prompt[1] == "#":
			root = str(prompt[0]+prompt[1])
			if root == x:
				root = pitch[x]
				return root
		else:
			root = str(prompt[0])
			if root == x:
				root = pitch[x]
				return root
def chord_int(prompt,root):
	chord=[root]
	for y in steps:
		if prompt[1] == "#":
			sym = prompt[2]+prompt[3]+prompt[4]
			if sym == y:
				for z in steps[y]:
					chord.append(root+int(z)) 
				return chord
		if prompt[1] != "#":
			sym = prompt[1]+prompt[2]+prompt[3]
			if sym == y:
				for z in steps[y]:
					chord.append(root+int(z)) 
				return chord
def to_notes(chord):
	c_notes = []
	for x in chord:
		x=x%12
		for n in pitch:
			if  x == pitch[n]:
				x = n
				c_notes.append(x)
	return c_notes
		
def go():
	prompt = raw_input("chord? ").lower()
	while prompt != '':
		root = get_root(prompt)
		chord1 = chord_int(prompt,root)
		chord2 = to_notes(chord1)
		print chord2
		prompt = raw_input("chord? ").lower()

go()
