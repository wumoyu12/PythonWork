import os.path
from os import path

def main():
    AskInfo();

def AskInfo():
    checkpoint = "askinfo";
    whichoption=str(input("\n1-Create a new file\n"
                          "2-Search for an existing file\n"
                          "Select an option by typing 1 or 2: "))
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich, pointcheck):
    match(pointcheck):
        case "askinfo":
            lengthopt=len(optionwhich);
            if( lengthopt != 1):
                print("Incorrect response. Type 1 or 2");
            else:
                optwhich = ord(optionwhich);
                if(int(optwhich) < 49 or int(optwhich) > 50):
                    print("Incorrect response. Type 1 or 2");
                else:
                    print("You have selected wisely");
        case default:
            print("Houston...we have a problem");
    AskInfo();
    
if __name__ == "__main__":
    main();
