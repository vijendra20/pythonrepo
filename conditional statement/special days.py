day=int(input("enter any day"))
match day:
     case 1|2|3|4|5:
         print("special days")
     case 6|7:
         print("bad days")
     case _:
         print("not a good day")



