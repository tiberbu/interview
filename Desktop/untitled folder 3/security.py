def maskname (name):
    name = name.split()

    firstName = name[0]
    secondName = name[1]
   
  

    firstName = name[0][:2] + "*" * len(firstName)
    secondName = name[1][:2] + "*" * len(secondName)

    return firstName, secondName



print(maskname("mark ngunyangi"))

