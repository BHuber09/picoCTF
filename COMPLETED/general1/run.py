#If I told you your grade was 0x41 in hexadecimal, what would it be in ASCII?

str = "0x41"
str = str[2:]

print str.decode("hex")