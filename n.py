a = input("what would you like to know search like thursday, ct: ")
match a:
    case("who is the class teacher"):
        print("ct - rachna verma")
    case("what is sports"):
            print("1 - lawn tennis 2- (incase of aahwan) basketball")
    case("what is aahwan"):
            print("sport competion")
    case("monday"):
        print("eng - rachna verma sports sst- aanchal batra maths - ritu sood science- seema sharma lunch awkn prog ct dance - kavita hindi - reema tridevi art - samriti")
    case("tuesday"):
        print("gk - ct sports english- rachna verma math- ritu sood science- seema sharma lunch aeromodeling - eric library hindi- reema tridevi art - samritti")
    case("wednesday"):
        print("sst-aanchal batra sports english-rachna verma maths-ritu sood french-shweta shukla space science- seema sharma hindi-reema tridevi stem")
    case("thursday"):
        print("club sports english maths science lunch computer sst-aanchal batra hindi-reema tridevi communication")
    case("friday"):
        print("english sports sst math science computer sst hindi music")
    case("ct"):
        print("ct - rachna verma")
    case("sports"):
            print("1 - lawn tennis 2- (incase of aahwan) basketball")
    case(unknown):
        print("sorry not known")


