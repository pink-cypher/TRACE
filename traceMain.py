from Analyst.analyst import Analyst
from projectManager.projectManager import ProjectManager


analyst = Analyst()
analystResult = analyst.checkAnalyst()

if analystResult:
    print("going to dashboard")
    analyst = Analyst(**analystResult)

    print(analyst.getInitials())
else:

    print("No analysts found. Please create one.")
    initials = input("Enter your initials: ")
    role = input("Enter your role (Lead/Member): ")
    isLead = input("Are you a Lead? (yes/no): ").strip().lower() == "yes"

    analystResult = analyst.createAnalyst(initials=initials, role=role, islead=isLead)

    if analystResult:
        print("Analyst created.")



project_manager = ProjectManager(analyst=analyst)



projectID = input("Enter Project ID: ").strip()

loadedProject = project_manager.loadProject(projectID=int(projectID) if projectID.isdigit() else None)

if loadedProject:
    print(vars(loadedProject))
else:
    print("Project not found or access denied.")


if project_manager.deleteOrArchiveProject(loadedProject.getID(), False):
    print("Archived")
# loadedProject.setDescription("Updated project description.")
# loadedProject.setStatus("Archived")
# loadedProject.setLockStatus(True)

# isSaved = project_manager.saveProject(loadedProject)




# while True:
#     print("\n Project Menu")
#     print("1 Create a Project")
#     print("2 Load a Project")
#     print("3 Exit")

    # choice = input("Enter your choice: ").strip()

    # if choice == "1":  # Create a project
    #     if analyst.getIslead():
    #         project_name = input("Enter Project Name: ").strip()
    #         description = input("Enter Project Description: ").strip()

    #         isCreated = project_manager.createProject(
    #             projectName=project_name,
    #             description=description
    #         )
    #         if isCreated:
    #             print("Project Created Successfully!")
    #         else:
    #             print("Failed to create project.")
    #     else:
    #         print("Only Leads can create a project.")

    # elif choice == "2":  # Load a project
    #     projectID = input("Enter Project ID: ").strip()

    #     loadedProject = project_manager.loadProject(projectID=int(projectID) if projectID.isdigit() else None)

    #     if loadedProject:
    #         print(vars(loadedProject))
    #     else:
    #         print("Project not found or access denied.")

    # elif choice == "3":  # Exit
    #     print("Exiting Project Menu...")
    #     break

    # else:
    #     print("Invalid choice! Please enter 1, 2, 3, or 4.")
