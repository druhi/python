a = input("week: ")
match a:
    case("monday"):
        print("sports  maths  science  hindi  lunch  english  SST  robotics  ART")
    case("tuesday"):
        print("sports  maths  science  hindi  lunch  english  space  french  ART")
    case("wednesday"):
        print("sports  maths  science  hindi  lunch  english  SST  library  computers(in class)")
    case("thursday"):
        print("sports  maths  science  hindi  lunch  english  SST  music  GK")
    case("friday"):
        print("sports  maths  dance  hindi  lunch  english  SST  Aeromodeling  computer(lab)")
    case(unknown):
        print("not a week or a day of working")
