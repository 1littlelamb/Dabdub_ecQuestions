#Roatation 13 Encode/Decode

with open('text_files/encoded_message.txt', 'r') as myfile:
  message = myfile.read()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

special_characters = {' ':' ', '.':'.', ',':',', '\n':'\n', '\t':'\t', ':':':', '-':'-', '/':'/', '!':'!', '#':'#', '1':'1', '2':'2', '3':'3', '4':'4'}
 
while True: 
	try:
		rot = int(input('Enter the Rotation Amount: '))
		break
	except:
		continue

def createRotationDict(rot, alphabet):

	alphabet_rotated = []

	for i in range(len(alphabet)):

		if (i+rot) > len(alphabet)-1:
			i = i-len(alphabet)
		alphabet_rotated.append(alphabet[i+rot])

	rotationDictionary = {alphabet[i]:alphabet_rotated[i] for i in range(len(alphabet))}
	rotationDictionary.update(special_characters)

	return rotationDictionary

def encodeDecode(rotationDictionary, encodedMessage):

	decodedText = ''

	for i in encodedMessage.lower():
		decodedText += rotationDictionary[i]

	return decodedText


rotationDictionary = createRotationDict(rot, alphabet)

newText = encodeDecode(rotationDictionary, message)

fileName = input('Enter the filename you would like to save the resultant text too: ')

with open(fileName + '.txt', 'w') as myfile:
	myfile.write(newText)
