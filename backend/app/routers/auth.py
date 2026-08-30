from fastapi import APIRouter, Depends, HTTPException, status
from backend.app.schemas.auth import LoginRequest, TokenResponse, UserResponse
from backend.app.services.auth_service import verify_password, create_access_token, get_current_user_from_token
from backend.app.repositories.in_memory import db

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
def login(login_data: LoginRequest):
    user = next((u for u in db.users if u["username"] == login_data.username or u["email"] == login_data.username), None)
    if not user or not verify_password(login_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    token = create_access_token({"sub": user["username"], "role": user["role"]})
    user_resp = UserResponse(
        id=user["id"],
        username=user["username"],
        email=user["email"],
        name=user["name"],
        role=user["role"],
        is_active=user["is_active"]
    )
    return TokenResponse(access_token=token, token_type="bearer", user=user_resp)

@router.get("/me", response_model=UserResponse)
def get_me(current_user: dict = Depends(get_current_user_from_token)):
    return UserResponse(
        id=current_user["id"],
        username=current_user["username"],
        email=current_user["email"],
        name=current_user["name"],
        role=current_user["role"],
        is_active=current_user["is_active"]
    )
