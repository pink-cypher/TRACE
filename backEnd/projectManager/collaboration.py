from databasemanager.databasemanager import db

class CollaborationManager:
    def __init__(self):
        pass

    def invite_to_project(self, lead_initials, analyst_initials, projectID):
        return db.addCollaborator(lead_initials, analyst_initials, projectID)

    def list_collaborators(self, projectID):
        return db.getCollaborators(projectID)

    def remove_collaborator(self, lead_initials, analyst_initials, projectID):
        return db.removeCollaborator(lead_initials, analyst_initials, projectID)