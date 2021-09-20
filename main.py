wordlist = []

def close():

#	number = int(input("[/*] number limit:"))
#	for i in wordlist:
#		if(i == None):
#			continue
#		for j in range(number):
#			j = str(j)
#			wordlist.append(i+j)
#			wordlist.append(i+"."+j)

        file = open("user_wordlist.txt","a")
        for i in wordlist:
                if(i is not None):
                        if(len(i) != 0):
                                file.write(i+"\n")
	file.close()
	print("Good luck! (user_wordlist.txt)")
	exit()
while(1):
	name = input("[/*]  Name and Surname?\r\n")
	if(name == "q"):
		close()
	name_lower=name.lower()
	name_lower_array=name_lower.split(" ")
	for i in name_lower_array:
		wordlist.append(i)
	fullname = ""
	if(len(name_lower_array) > 1):
		fullname = ".".join(name_lower_array)
		wordlist.append(fullname)
		nameDotSurname = wordlist.append(name_lower_array[0]+"."+"".join(name_lower_array[1:]))
		nDotSurname = wordlist.append(name_lower_array[0][0]+"."+"".join(name_lower_array[1:]))
		nSurname = wordlist.append(name_lower_array[0][0]+"".join(name_lower_array[1:]))
		wordlist.append(nameDotSurname)
		wordlist.append(nDotSurname)

#	print(wordlist)
