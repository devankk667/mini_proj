from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.app.schemas.base import ErrorResponse, ErrorDetail
from backend.app.exceptions import AppException
from backend.app.routers import auth, inventory, business, finance_and_mgmt, analytics_and_reports

app = FastAPI(
    title="MSME360 Backend API",
    description="Logical Backend & API layer for MSME360 Business Management System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            success=False,
            message=exc.message,
            errors=[ErrorDetail(code=exc.code, message=exc.message, field=exc.field)]
        ).model_dump()
    )

app.include_router(auth.router)
app.include_router(inventory.router)
app.include_router(business.router)
app.include_router(finance_and_mgmt.router)
app.include_router(analytics_and_reports.router)

@app.get("/api/health")
def health_check():
    return {"status": "ok", "system": "MSME360 API"}
