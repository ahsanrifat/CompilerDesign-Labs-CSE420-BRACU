keyword = set()
identifiers = set()
a_operator = set()
r_operator = set()
b_operator = set()
l_operator = set()
as_operator = set()
numerical = set()
others = set()
reserved = ["abstract", "assert", "boolean",
            "break", "byte", "case", "catch", "char", "class", "const",
            "continue", "default", "do", "double", "else", "extends", "false",
            "final", "finally", "float", "for", "goto", "if", "implements",
            "import", "instanceof", "int", "interface", "long", "native",
            "new", "null", "package", "private", "protected", "public",
            "return", "short", "static", "strictfp", "super", "switch",
            "synchronized", "this", "throw", "throws", "transient", "true",
            "try", "void", "volatile", "while"]

arithmetic = ["+", "-", "*", "/", "%", "++", "--"]
relational = ["==", "!=", ">", "<", ">=", "<="]
bitwise = ["&", "|", "^", "~", "<<", ">>", ">>>"]
logical = ["&&", "||", "!"]
assignment = ["=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", "&=", "^=", "|="]
other = ["{", "}", "(", ")"]
#especial = ["!", "@", "!", "$", "%", "^", "&", "*", "(", ")", "-", "?", "<", ">", ":", ",", "|"]
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
    code=string.split()
    return code
def checkIsVariable(string):

    if(string[0].isalpha()==True or string[0]=="_" or string[0]=="$"): #starting is correct

        for x in range(string.__len__()):

            if(x!=0): #ignoring first index

                if(string[x].isalnum()==False and string[x]!='_'): #if any special character is present

                    return False
    else:

        return False #fault at the beginning
    return True


def processData(code):
    count = 0;
    for i in code:

        t = True

        if ("," in i):
            others.add(",")
        if (";" in i):
            others.add(";")

        i = i.replace(",", "")
        i = i.replace(";", "")

        # if(i.isdigit()==True):
        # numerical.add(i)

        m = i.replace(".", "")

        if (m.isdigit() == True):
            numerical.add(i)
            t=False
        if (t == True):
            # checking keyword
            for j in reserved:
                if (j == i):
                    keyword.add(i)
                    t = False

        if (t == True):

            # checking arithmetic
            for j in arithmetic:
                if (j == i):
                    a_operator.add(i)
                    t = False

        if (t == True):
            # checking relational
            for j in relational:
                if (j == i):
                    r_operator.add(i)
                    t = False

        if (t == True):
            # checking bitwise
            for j in bitwise:
                if (j == i):
                    b_operator.add(i)
                    t = False

        if (t == True):
            # checking logical
            for j in logical:
                if (j == i):
                    l_operator.add(i)
                    t = False

        if (t == True):
            # checking assignment
            for j in assignment:
                if (j == i):
                    as_operator.add(i)
                    t = False

        if (t == True):
            # checking other
            for j in other:
                if (j == i):
                    others.add(i)
                    t = False

        if(t==True):
          #checking variable
            if(checkIsVariable(i)):
                identifiers.add(i)



        count = count + 1
    if(as_operator.__len__()!=0):
        print("Assignment Operators:")
        print(as_operator)
    if (keyword.__len__()!= 0):
        print("keyword:")
        print(keyword)
    if (a_operator.__len__()!= 0):
        print("Arithmetic Operators:")
        print(a_operator)
    if (r_operator.__len__()!= 0):
        print("Relational Operators:")
        print(r_operator)
    if (others.__len__()!= 0):
        print("Others Operators:")
        print(others)
    if (numerical.__len__()!= 0):
        print("Numerical Operators:")
        print(numerical)
    if (identifiers.__len__()!= 0):
        print("Identifier:")
        print(identifiers)
    if (l_operator.__len__()!= 0):
        print("Logical Operators:")
        print(l_operator)
    if (b_operator.__len__()!= 0):
        print("Bitwise Operators:")
        print(b_operator)

code=takeInput("input.txt")
processData(code)
