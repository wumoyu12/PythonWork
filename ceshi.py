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
