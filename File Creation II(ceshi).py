import os.path
from os import path

#msg=["New File Name:", "Existing File Name:"];

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
                        FileType();
                        #whichfilename = str(input(msg[0]));
                    else:
                        FileType();
                        #whichfilename = str(input(msg[1]));

                    #whichfilename = whichfilename + ".doc";
                    #FileConnectivity();
        case default:
            print("Houston...we have a problem");
            sys.exit();

def FileType():
    whichtype=str(input("1-Word Document\n"
                          "2-Text File\n"
                          "Select an option by typing 1 or 2: "))
    match(whichtype):
        case
    
    AskInfo();
    


if __name__ == "__main__":
    main();
