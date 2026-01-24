print ("Hi")
# Second line
text = 'mY lOng loNg STRinG'
string_index = text.lower().index('string')
print(text[:string_index].lower() + text[string_index:].upper())