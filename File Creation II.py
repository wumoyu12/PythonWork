import sys
import os
from os import path

msg = ["New File Name:", "Existing File Name:"]

def main():
    AskInfo();

def AskInfo():
    checkpoint = "askinfo";
    whichoption = str(input("\n1-Create a new file\n"
                            "2-Search for an existing file\n"
                            "3-Exit the Program"
                            "Select an option by typing 1 2 or 3: "))
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich, pointcheck):
    global whichfilename
    match(pointcheck):
        case "askinfo":
            lengthopt = len(optionwhich)
            if(lengthopt != 1):
                print("Incorrect response. Type 1 2 or 3")
                AskInfo()
            else:
                optwhich = ord(optionwhich)
                if(int(optwhich) < 49 or int(optwhich) > 51):
                    print("Incorrect response. Type 1 2 or 3")
                    AskInfo()
                else:
                    if(optwhich == 49):
                        Create()
                    if(optwhich == 50):
                        Search()
                    else:
                        Exit()
        case default:
            print("Houston...we have a problem")
            sys.exit()

def FileType():
    whichtype = str(input("\n1-Word Document\n"
                          "2-Text File\n"
                          "3-Excel\n"
                          "4-Power Point\n"
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
        case "4":
            filetype = ".ppt"
        case default:
            print("It's an invalid selection, please type 1 2 3 or 4")
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

def Exit():
    sys.exit();

if __name__ == "__main__":
    main()
