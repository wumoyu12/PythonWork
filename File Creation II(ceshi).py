import os.path
from os import path

msg=["New File Name:", "Existing File Name:"];

def main():
    AskInfo();

def AskInfo():
    checkpoint = "askinfo";
    whichoption=str(input("1-Create a new file\n"
                          "2-Search for an existing file\n"
                          "Select an option by typing 1 or 2: "))
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich, pointcheck):
    global whichfilename;
    match(pointcheck):
        case "askinfo":
            lengthopt=len(optionwhich);
            if( lengthopt != 1):
                print("Incorrect response. Type 1 or 2");
                AskInfo();
            else:
                optwhich = ord(optionwhich);
                if(int(optwhich) < 49 or int(optwhich) > 50):
                    print("Incorrect response. Type 1 or 2");
                    AskInfo();
                else:
                    if(optwhich == 49):
                        Create();
                    else:
                        Search();
        case default:
            print("Houston...we have a problem");
            sys.exit();

def FileType():
    whichtype=str(input("1-Word Document\n"
                        "2-Text File\n"
                        "Select an option by typing 1 or 2"))
    Checkfiletype(whichtype);
    
def Checkfiletype(file):
    global filetype;
    match(file):
        case "1":
            filetype=".doc";
        case "2":
            filetype=".txt";
        case default:
            print("It's an invaild select, please try again");
            FileType();
    
def Create():
    global filename;
    FileType();
    filename=str(input("Please Enter " + msg[0]));
    FileConnectivity();
    if (exist=="n"):
        pythfile = open(filename, "x");
        print("File created successfully!");
        pythfile.close();
        NewFileAdd();
    else:
        print("This file is already exist.");

def NewFileAdd():
    ask=str(input("Do you want write anything in this file(type 1:Yes/type 2:No)."))
    match (ask):
        case "1":
            Addtext();
        case "2":
            AskInfo();
        case default:
            print("Your input is invalid, please type 1 or 2.");
            NewfileAdd();

def Addtext():
    text=str(input("Type something add to your file"));
    if (text==""):
        print("please enter something");
    else:
        pythfile=open(filename, "a");
        pythfile.write(text);
        print("Add Successfully!");
        pythfile.close();
        Readfile();
        
def Readfile():
    print("You have flowing in " + filename + ":");
    pythfile=open(filename, "r");
    print(pythfile.readline());
    pythfile.close();

def Search():
    global filename;
    FileType();
    filename=str(input("Please Enter " + msg[1]));
    FileConnectivity();
    if (exist=="y"):
        Readfile();
        AskSearch();
    else:
        print("This file is not exist.");
        AskInfo();
    
def AskSearch():
    what=str(input("1-Add something to this file\n"
                   "2-Overwrite the file"
                   "3-Go Back"
                   "Select an option by typing 1 or 2"))
    match (what):
        case "1":
            Addtext();
        case "2":
            Overwrite();
        case "3":
            AskInfo();
        case default:
            print("Your input is invalid, please try again")
            AskSearch();
            
def Overwrite():
    text=str(input("Type something to write in your file"));
    if (text==""):
        print("please enter something");
    else:
        pythfile=open(filename, "w");
        pythfile.write(text);
        print("Add Successfully!");
        pythfile.close();
        Readfile();

def FileConnectivity():
    global exist;
    print(filename + filetype);
    fileDir=os.path.dirname(os.path.realpath("__file__"));
    fileexist=bool(path.exists(filename + filetype));
    if(fileexist == True):
        exist="y";
    else:
        exist="n";
    
if __name__ == "__main__":
    main();
