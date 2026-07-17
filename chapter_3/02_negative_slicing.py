name="tanya"

print(name[0:3])

print(name[-3: -1])

print(name[2: 4])

print(name[:4])  #is same as print(name[0:4])

print(name[2:]) #is same as print(name[2:5])
print(name[2:5]) #is same as print(name[2:])


#slicing with skip value
word="amazing"
print(word[1:4:2])

word="abdjdgsjss"
print(word[1:6:2])

#advanced slicing
word="tanya"
print(word[:7])
print(word[0:])