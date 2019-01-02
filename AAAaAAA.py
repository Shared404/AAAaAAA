#! /usr/bin/env python2


def threeCapFinder(instring):
	instring = list(instring)
	for i in range(len(instring)):
		instring[i] = ord(instring[i])
	i = 0
	for i in range(len(instring)):
		if instring[i] >= 65 and instring[i] <= 90:
			if instring[i+1] >= 65 and instring[i+1] <= 90:
				if instring[i+2] >= 65 and instring[i+2] <= 90:
					if instring[i+3] >= 97 and instring[i+3] <= 122:
						if instring[i+4] >= 65 and instring[i+4] <= 90:
							if instring[i+5] >= 65 and instring[i+5] <= 90:
								if instring[i+6] >= 65 and instring[i+6] <= 90:
									if instring[i-1] < 65 or instring[i-1] > 90:
										if instring[i+7] < 65 or instring[i+7] > 90:
											print(chr(instring[i]) + chr(instring[i+1]) + chr(instring[i+2]) + chr(instring[i+3]) + chr(instring[i+4]) + chr(instring[i+5]) + chr(instring[i+6]))
						
wantedfile = raw_input("File> ") 
f = open(wantedfile)
threeCapFinder(f.read())
f.close()
