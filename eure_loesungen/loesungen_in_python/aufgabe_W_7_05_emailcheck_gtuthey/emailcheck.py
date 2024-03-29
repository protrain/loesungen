def isEmail (email_address):
    # finde das @ und den ersten . nach dem @
    at = email_address.find("@")
    dot = email_address.find(".",at)

    # identifiziere die drei relevanten Teile der Adresse
    prefix = email_address[0:at]
    domain_name = email_address[at+1:dot]
    suffix = email_address[dot+1:]
    
    # Prüfe die Email-Teile
    return len(prefix) > 1 and len(domain_name) >1 and domain_name.find("@") == -1 and (0 < len(suffix) <4)

# Hauptprogramm
print(isEmail("john@doe.de"))
print(isEmail("john@.net"))
print(isEmail("john@doe.net"))
print(isEmail("@.net"))
print(isEmail("john@doe.shop"))

# akzeptiert auch Emails, mit einem '.' vor dem '@'
print(isEmail("john.doe@email.com"))
