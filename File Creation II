import os.path
from os import path

msg=["New File Name:", "Existing File Name:"];

def main():
    AskInfo();

def AskInfo():
    checkpoint = "askinfo";
    whichoption=str(input("\n1-Create a new file\n"
                          "2-Search for an existing file\n"
                          "Select an option by typing 1 or 2: "))
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich, pointcheck):
    global whichfilename;
    match(pointcheck):
        case "askinfo":
            optwhich = ord(optionwhich);
            if( int(optwhich) != 49 or int(optwhich) != 50):
                print("Incorrect response. Type 1 or 2");
                AskInfo();
            else:
                if(optwhich == 1):
                    whichfilename = str(input(mfg[0]));
                else:
                    whichfilename = str(input(mfg[1]));

                whichfilename = whichfilename + ".doc";
                FileConnectivity();
        case default:
            print("Houston...we have a problem");
            sys.exit();

def FileConnectivity():
    fileDir=os.path.dirnmae(os.path.realpath("__file__"));
    fileexist=bool(path.exists(whichfilename));
    if(fileexist == True):
        adminfile=open(whichfilename, "r");
    else:
        adminfile=open(whichfilename, "x");
    adminfile.close();

if __name__ == "__main__":
    main();
