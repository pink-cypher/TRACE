from fastapi import APIRouter, Request
from Analyst.analyst import Analyst

router = APIRouter()

@router.post("/check")
async def check_analyst(request: Request):
    data = await request.json()
    initials = data.get("initials", "").upper()
    
    analyst = Analyst()
    exists = analyst.checkAnalyst(initials)
    return {"exists": bool(exists)}

@router.post("/create")
async def create_analyst(request: Request):
    data = await request.json()
    initials = data.get("initials").upper()
    role = data.get("role")

    analyst = Analyst()
    created = analyst.createAnalyst(initials, role)
    return {"success": created}