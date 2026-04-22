#Q:3/
with open('samp.txt','w') as file:
    file.write("Hello, Shrey here for assignment-2.\n")
    file.write("Do Accept this time ;).")

#Q:4/
with open("samp.txt", "r") as file:
    content = file.read()
    print(content)