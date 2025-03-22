from Analyst.analyst import Analyst
from projectManager.projectManager import ProjectManager

# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Optional: allow all origins if not proxying (for dev only)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/api/initials")
# async def receive_initials(request: Request):
#     data = await request.json()
#     return {"capitalized_initials": True}


analyst = Analyst()
initals = 'RP'
analystResult = analyst.checkAnalyst(initals)

print(analystResult)



# if analystResult:
#     print("going to dashboard")
#     analyst = Analyst(**analystResult)

#     print(analyst.getInitials())
# else:

#     print("No analysts found. Please create one.")
#     initials = input("Enter your initials: ")
#     role = input("Enter your role (Lead/Member): ")
#     isLead = input("Are you a Lead? (yes/no): ").strip().lower() == "yes"

#     analystResult = analyst.createAnalyst(initials=initials, role=role, islead=isLead)

#     if analystResult:
#         print("Analyst created.")



# project_manager = ProjectManager(analyst=analyst)



# projectID = input("Enter Project ID: ").strip()

# loadedProject = project_manager.loadProject(projectID=int(projectID) if projectID.isdigit() else None)

# if loadedProject:
#     print(vars(loadedProject))
# else:
#     print("Project not found or access denied.")


# if project_manager.deleteOrArchiveProject(loadedProject.getID(), True):
#     print("Deleted")
