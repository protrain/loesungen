def isStrong (password):
    #check length
    length = len(password) >= 8

    #check lowercase letters
    lower = password.upper() != password

    #check uppercase letters
    upper = password.lower() != password

    #check for numbers
    number = False
    for i in range(1,11):
        if password.find(str(i)) != -1:
            number = True
            break

    #check for special characters
    special = False
    for char in ['!', '*']:
        if password.find(char) != -1:
            special = True
            break

    return length and lower and upper and number and special


print (isStrong("eVJo2!8IrRo"))
print (isStrong("aH6*LauTp21u"))
print (isStrong("o1hKeaZG*!o"))
print (isStrong("S3cr3ts!"))
print (isStrong("Passwort123"))
print (isStrong("passwort!23"))
print (isStrong("PASSWORT!23"))
print (isStrong("!2Bcv"))
print (isStrong("123456789!"))
