from fastapi import APIRouter, Request, Form
from services.scanningManager.scan_service import ScanService

scan_service = ScanService()
router = APIRouter()

@router.post("/projects/{project_id}/http-request")
async def execute_http_request(
    project_id: str,
    target_url: str = Form(...),
    http_method: str = Form(...),
    headers: str = Form(None),
    cookies: str = Form(None),
    hide_status_codes: str = Form(None),
    show_only_status_codes: str = Form(None),
    proxy: str = Form(None),
    request_body: str = Form(None),
    additional_params: str = Form(None)
):

    # Execute the HTTP request using the provided parameters
    response = scan_service.execute_http_request(
        target_url,
        http_method,
        headers,
        cookies,
        hide_status_codes,
        show_only_status_codes,
        proxy,
        request_body,
        additional_params
    )
    return response