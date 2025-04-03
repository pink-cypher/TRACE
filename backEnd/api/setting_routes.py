from fastapi import APIRouter, Request, HTTPException
from databasemanager.databasemanager import db

router = APIRouter()

@router.post("/setting")
async def updateSetting(request: Request):
    data = await request.json()
    initials = data.get("initials", "").upper()
    export = data.get("export, """)
    darkMode = data.get('darkMode',"")

    settingsResult = db.updateSetting(initials=initials, export=export, darkMode=darkMode)

    if not settingsResult:
        raise HTTPException(status_code=401, detail="Invalid settings")
    
    return {
        "export": settingsResult.get("export"),
        "darkMode": settingsResult.get("darkMode")
    }

