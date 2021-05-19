def main():
    #write your code below this line
    peoples_names = []

    while True:
      user_input = (str(input("")))
      peoples_names.append(user_input)      
      if(user_input == ""):
        break

    request = (str(input("Search for?")))
    if request in peoples_names:
      print(str(request + " was found!"))
    else:
      print(str(request + " was not found!"))

if __name__ == '__main__':
    main()
