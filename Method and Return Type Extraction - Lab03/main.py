import re
methods=[]
returnType=[]
def extractMethods(code):
    for i in code:

        if("(" in i and ")" in i and "." not in i):
            j=i.split(";")
            for k in j:
                if ("(" in k and ")" in k and "." not in i):
                    k=k.replace("}","")
                    k = k.replace("public", "")
                    k = k.replace("static", "")


                    #removing leading spaces
                    k=k.strip()


                    if re.match(r'^int', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("int")


                    if re.match(r'^String', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("String")

                    if re.match(r'^double', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("double")

                    if re.match(r'^float', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("float")

                    if re.match(r'^boolean', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("boolean")

                    if re.match(r'^char', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("char")

                    if re.match(r'^long', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("long")

                    if re.match(r'^void', k):
                        k = k.split(' ', 1)[1]
                        returnType.append("void")

                    #k = k.replace(" ", "")
                    methods.append(k)



def takeInput(address):
    # reading file
    file = open(address, 'r')
    listOfLines = file.readlines()
    file.close()
    code=[]
    string = ""
    for line in listOfLines:
        eachLine = line.strip()
        string = string +eachLine+" "
    code=string.split("{")
    return code

code=takeInput("input.txt")
extractMethods(code)

print("----Methods-----")
for i in methods:
    print(i)
print("-----Return Types-----")
for i in returnType:
    print(i)
