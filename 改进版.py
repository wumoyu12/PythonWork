import os
from os import path
import sys  # Import sys module for sys.exit()

msg = ["New File Name:", "Existing File Name:"]

def main():
    AskInfo()

def AskInfo():
    checkpoint = "askinfo"
    whichoption = str(input("1-Create a new file\n"
                            "2-Search for an existing file\n"
                            "Select an option by typing 1 or 2: "))
    CheckInfo(whichoption, checkpoint)

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
    whichtype = str(input("1-Word Document\n"
                          "2-Text File\n"
                          "Select an option by typing 1 or 2: "))
    Checkfiletype(whichtype)

def Checkfiletype(file):
    global filetype
    match(file):
        case "1":
            filetype = ".doc"
        case "2":
            filetype = ".txt"
        case default:
            print("It's an invalid selection, please try again")
            FileType()

def Create():
    global filename
    FileType()
    filename = str(input("Please Enter " + msg[0]))
    FileConnectivity()
    if (exist == "n"):
        pythfile = open(filename + filetype, "x")  # Use the correct file name with extension
        print("File created successfully!")
        pythfile.close()
        NewFileAdd()
    else:
        print("This file already exists.")

def NewFileAdd():
    ask = str(input("Do you want to write anything in this file (type 1:Yes / type 2:No): "))
    match (ask):
        case "1":
            Addtext()
        case "2":
            AskInfo()
        case default:
            print("Your input is invalid, please type 1 or 2.")
            NewFileAdd()

def Addtext():
    text = str(input("Type something to add to your file: "))
    if (text == ""):
        print("Please enter something.")
    else:
        pythfile = open(filename + filetype, "a")  # Ensure using the correct file name
        pythfile.write(text)
        print("Added successfully!")
        pythfile.close()
        Readfile()

def Readfile():
    print("You have the following content in " + filename + ":")
    pythfile = open(filename + filetype, "r")  # Ensure using the correct file name
    print(pythfile.read())  # To read all content in the file
    pythfile.close()

def Search():
    global filename
    FileType()
    filename = str(input("Please Enter " + msg[1]))
    FileConnectivity()
    if (exist == "y"):
        Readfile()
        AskSearch()
    else:
        print("This file does not exist.")
        AskInfo()

def AskSearch():
    what = str(input("1-Add something to this file\n"
                     "2-Overwrite the file\n"
                     "3-Go Back\n"
                     "Select an option by typing 1, 2, or 3: "))
    match (what):
        case "1":
            Addtext()
        case "2":
            Overwrite()
        case "3":
            AskInfo()
        case default:
            print("Your input is invalid, please try again.")
            AskSearch()

def Overwrite():
    text = str(input("Type something to overwrite in your file: "))
    if (text == ""):
        print("Please enter something.")
    else:
        pythfile = open(filename + filetype, "w")  # Ensure using the correct file name
        pythfile.write(text)
        print("Overwritten successfully!")
        pythfile.close()
        Readfile()

def FileConnectivity():
    global exist
    print(filename + filetype)
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(filename + filetype))
    if (fileexist == True):
        exist = "y"
    else:
        exist = "n"

if __name__ == "__main__":
    main()
