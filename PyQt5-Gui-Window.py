#Cheerleader 1.0

en_letters = "abcdefABCDEF"
ord = input("Vad är ditt favoritord?")
enthusiasm = int(input("Bryr du dig verkligen? 1-10"))

for char in ord:
    if char in en_letters:
        print("Ge mig en  " + char)
    else:
        print("Ge mig ett "+ char)

for i in range(enthusiasm):
    print(ord)
