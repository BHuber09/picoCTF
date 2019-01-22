# Crpyto can often be done by hand, here's a message you got from a friend, llkjmlmpadkkc with the key of thisisalilkey.

msg = "llkjmlmpadkkc"
key = "thisisalilkey"
out = ""
main = []

arr = [0]*27
count = 0

with open("table.txt", "r") as file:
	# dont care for the first couple of lines as its just headers
	line = file.readline().lstrip()
	data = line.split(" ")
	main = data
	line = file.readline().rstrip()

	line = file.readline().rstrip()[4:].lower()

	while line:
		data = line.split(" ")

		arr[count] = data
		count += 1

		line = file.readline().rstrip()[4:].lower()

for i in range(len(key)):
	k_val = ord(key[i]) - 97

	for j in range(len(arr[k_val])):
		if(msg[i] == arr[k_val][j]):
			out += main[j]



print "picoCTF{" + out + "}"