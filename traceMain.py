from Analyst.analyst import Analyst


analyst = Analyst()

analystResult = analyst.checkAnalyst()

if analystResult:
    print("going to dashboard")
    analyst = Analyst(analystId=analystResult["ID"], initials=analystResult["initials"],
                    role=analystResult["role"], isLead=analystResult["isLead"], mac=analystResult["mac"])
    
    print(analyst.initials)
    print(analyst.mac)
    print(analyst.islead)
    print(analyst.role)

else:
    isLead = False
    print("Landing page. input initials and input lect role")
    initials = input("Enter initials: ")
    role = input("1:lead\n2:member\n: ")
    if role == "1":
        role = "Lead"
        isLead = True
    else:
        role = "Member"
    analystResult = analyst.createAnalyst(initials=initials, role=role, isLead=isLead)
    analyst = Analyst(analystId=analystResult["ID"], initials=analystResult["initials"],
                    role=analystResult["role"], isLead=analystResult["isLead"], mac=analystResult["mac"])
    
    print(analyst.initials)
    print("Analyst created.")