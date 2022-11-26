contact = {
    "sai teja" : "8500811144",
    "arshaq" : "9048786526",
    "nilesh" : "7052783592",
    "bandi rohit": "7396773878",
    "rakesh":  "9381532097",
    "chandravadhan": "9553224039",
    "amruth": "7780655038",
    "devaraj": "8304846343",
    "harish": "8639283960",
    "likitha": "7013289500",
    "vignesh": "9398001217",
    "madhav": "9001634266",
    "sinan": "9061349363",
    "lihan": "7356669185",
    "harman": "8730817758",
    "dhanush": "9392484866",
    "anirudh": "9569348021",
    "ashish" : "8742831171",
    "aayush" : "9510155815",
    "kashim bhasha": "8688710292",
    "manju": "9346656393",
    "mokshit": "7000209021",
    "prasad": "8639483213",
    "raghu": "9515421196",
    "ram chandra": "8808221880",
    "ranjeet": "6307256902",
    "revanth": "8897477922",
    "satyam": "8651833265"  
}
print("1: Search a Contact, 2: Display all Contacts, 3: Extract multiple numbers")
input1 = int(input("Enter your choice: "))

if input1==1:
    contact1 = input("Enter the name of the contact: ").lower()
    name = contact.get(contact1)
    if name==None:
        print("Check the name you have entered!!!")
    else:
        print(contact1,":",name)

elif input1==2:
    print(contact)
    
elif input1==3:
    extract_contact = int(input("Enter the number of contact to extract: "))
    l = []
    for i in range(extract_contact):
        name = input("Enter the name of the contact: ").lower()
        a = name+ ": " + contact.get(name)
        l.append(a)
    print(l)
else:
    print("Wrong input")