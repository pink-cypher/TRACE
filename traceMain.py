from Analyst.analyst import Analyst
from projectManager.projectManager import ProjectManager

analyst = Analyst()

analystResult = analyst.checkAnalyst()

if analystResult:
    print("going to dashboard")
    analyst = Analyst(analystId=analystResult["ID"], initials=analystResult["initials"],
                    role=analystResult["role"], isLead=analystResult["isLead"], mac=analystResult["mac"])
    
    # print(analyst.initials)
    # print(analyst.mac)
    # print(analyst.islead)
    # print(analyst.role)

else:


    print("No analysts found. Please create one.")
    initials = input("Enter your initials: ")
    role = input("Enter your role (Lead/Member): ")
    isLead = input("Are you a Lead? (yes/no): ").strip().lower() == "yes"
    isLead = False

    analystResult = analyst.createAnalyst(initials=initials, role=role, isLead=isLead)
    analyst = Analyst(analystId=analystResult["ID"], initials=analystResult["initials"],
                    role=analystResult["role"], isLead=analystResult["isLead"], mac=analystResult["mac"])
    
    # print(analyst.initials)
    # print(analyst.mac)
    # print(analyst.islead)
    # print(analyst.role)
    print("Analyst created.")


project_manager = ProjectManager(analyst=analyst)

if analyst.islead:
    project_name = input("Enter Project Name: ").strip()
    description = input("Enter Project Description: ").strip()

    project_manager.createProject(
        projectName=project_name,
        description=description
    )

else:
    print("Only Leads can create a project.")


