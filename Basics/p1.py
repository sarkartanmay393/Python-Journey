# say something is a programme that take user input over and over then compile it to final statement by making first char a sentence upper case,
# joining diff statements via period symbol, if finds a question statement then add a question mark to the end, and the programme ends with '/end' statement.


res = ""

while True:
    statement = input("Say something : ")
    if (statement == "/end"):
        print(res)
        break
    elif (statement.startswith("how" or "wh")):
        statement = statement.title()
        statement = statement + "?"
        res += statement
    else:
        statement = statement.title()
        statement += ". "
        res += statement
