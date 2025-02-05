import os
from os import path

msg = ["New File Name:", "Existing File Name:"]

def main():
    AskInfo();

def AskInfo():
    checkpoint = "askinfo";
    whichoption = str(input("\n1-Create a new file\n"
                            "2-Search for an existing file\n"
                            "Select an option by typing 1 or 2: "))
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich, pointcheck):
    global whichfilename
    match(pointcheck):
        case "askinfo":
            lengthopt = len(optionwhich)
            if(lengthopt != 1):
                print("Incorrect response. Type 1 or 2")
                AskInfo()
            else:
                optwhich = ord(optionwhich)
                if(int(optwhich) < 49 or int(optwhich) > 50):
                    print("Incorrect response. Type 1 or 2")
                    AskInfo()
                else:
                    if(optwhich == 49):
                        Create()
                    else:
                        Search()
        case default:
            print("Houston...we have a problem")
            sys.exit()

def FileType():
    whichtype = str(input("\n1-Word Document\n"
                          "2-Text File\n"
                          "3-Excel\n"
                          "Select an option by typing 1 or 2: "))
    Checkfiletype(whichtype)

def Checkfiletype(file):
    global filetype
    match(file):
        case "1":
            filetype = ".doc"
        case "2":
            filetype = ".txt"
        case "3":
            filetype = ".xlsx"
        case default:
            print("It's an invalid selection, please type 1 or 2")
            FileType()

def Create():
    global filename
    FileType()
    filename = str(input("Please Enter " + msg[0]))
    FileConnectivity()
    if (exist == "n"):
        pythfile = open(filename + filetype, "x")
        print("File created successfully!")
        pythfile.close()
    else:
        print("This file already exists, please try again")
        Create()
    AskInfo()

def Search():
    global filename
    FileType()
    filename = str(input("Please Enter " + msg[1]))
    FileConnectivity()
    if (exist == "y"):
        print("The file is exisist")
    else:
        print("This file does not exist");
    AskInfo()

def FileConnectivity():
    global exist
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(filename + filetype))
    if (fileexist == True):
        exist = "y"
    else:
        exist = "n"

if __name__ == "__main__":
    main()
