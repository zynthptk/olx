notes = {
  'e':0,
  'a':5,
  'd':10,
  'g':15,
  'b':19
}

pitch = {
  0:'e',
  1:'f',
  2:'f#',
  3:'g',
  4:'g#',
  5:'a',
  6:'bb',
  7:'b',
  8:'c',
  9:'c#',
  10:'d',
  11:'eb',
  12:'e'
}
tab = raw_input("Note? ")
while tab != '':
	str(tab)
	
	for x in notes:
		if x == tab[0]:
			strng = notes[x]
			
	if len(tab) != 3:
		num = tab[1]
		
	else:
		num = tab[1]+tab[2]	
	val = int(strng) + int(num)
	
	for n in pitch:
		if  val%12 == n:
			print pitch[n]
	tab = raw_input("Note? ")
	
