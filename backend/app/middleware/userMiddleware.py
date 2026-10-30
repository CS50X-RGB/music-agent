from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.security import decode_access_token
import jwt
from fastapi.responses import JSONResponse

class UserMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request : Request, call_next):
        public_paths = {
            "/api/web/v1/auth/login",
            "/api/web/v1/auth/register"
        }

        if request.url.path in public_paths:
            return await call_next(request)
        
        auth = request.headers.get("Authorization")

        if auth and auth.startswith("Bearer "):
            token = auth.split(" ",1)[1]
            try:
                value = decode_access_token(token=token)

                request.state.user = {
                    "id" : value['sub'],
                    "email" : value['email'],
                    "name" : value['name']
                }
            except jwt.InvalidTokenError:
                return JSONResponse(
                    status_code=401,
                    content={
                        "detail" : "Invalid or expired token"
                    },
                )
        else:
            request.state.user = None
        
        response = await call_next(request)
        return response