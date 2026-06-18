alphabet= input("enter any alphabet")
match alphabet:
     case "a"|"e"|"i"|"o"|"u":
         print("letter")
     case _:
         print("constants")


alphabet= input("enter any alphabet")
match alphabet:
    case "a"|"s"|"d"|"f"|"g"|"p"|"h"|"j"|"k"|"l"|"m":
        print("special character")
    case _:
        print("not a special character")
