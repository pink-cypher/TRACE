from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from Analyst.analyst import Analyst
from jose import jwt
from databasemanager.config.config_loader import SECRET_KEY, ALGORITHM 

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

@router.post("/login")
async def login(request: Request):
    data = await request.json()
    initials = data.get("initials", "").upper()
    role = data.get("role")

    analyst = Analyst()
    analyst_data = analyst.loadAnalyst(initials)

    if not analyst_data:
        raise HTTPException(status_code=401, detail="Invalid initials")

    # Save role/session if needed
    analyst.saveAnalyst(initials=initials, role=role)

    token_data = {
        "sub": initials,
        "role": role
    }

    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "initials": initials,
        "role": role
    }

@router.post("/logout")
async def logout():
    response = JSONResponse(content={"message": "Logged out"})
    response.delete_cookie("access_token", path="/")
    return response