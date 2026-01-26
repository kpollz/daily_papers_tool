import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import secrets

from daily_papers_tool import run_daily_digest

app = FastAPI(
    title="Daily Papers Tool API",
    description="API để tạo tóm tắt các bài báo nghiên cứu hàng ngày từ Hugging Face",
    version="1.0.0"
)

# Basic Authentication
security = HTTPBasic()

# Lấy mật khẩu từ biến môi trường
API_PASSWORD = os.getenv("API_PASSWORD")

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    """Xác thực người dùng với mật khẩu từ .env"""
    if not API_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API password chưa được cấu hình trong file .env"
        )
    
    # So sánh mật khẩu một cách an toàn
    is_correct_password = secrets.compare_digest(credentials.password, API_PASSWORD)
    
    if not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Mật khẩu không đúng",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    return credentials.username

class DateRequest(BaseModel):
    """Model cho request với ngày, tháng, năm"""
    day: int = Field(..., ge=1, le=31, description="Ngày (1-31)")
    month: int = Field(..., ge=1, le=12, description="Tháng (1-12)")
    year: int = Field(..., ge=2000, le=2100, description="Năm (2000-2100)")
    model: Optional[str] = Field(default="gemini-2.5-flash", description="Mô hình LLM để sử dụng")

@app.get("/")
async def root():
    """Endpoint kiểm tra API hoạt động"""
    return {
        "message": "Daily Papers Tool API",
        "status": "running",
        "version": "1.0.0"
    }

@app.post("/generate-digest")
async def generate_daily_digest(
    date_request: DateRequest,
    username: str = Depends(verify_password)
):
    """
    Tạo tóm tắt các bài báo nghiên cứu cho một ngày cụ thể.
    
    Yêu cầu xác thực Basic Auth với mật khẩu từ file .env.
    
    Args:
        date_request: Đối tượng chứa day, month, year và model (optional)
        username: Tên người dùng từ xác thực (tự động lấy từ Depends)
    
    Returns:
        Thông tin về quá trình xử lý và đường dẫn file kết quả
    """
    try:
        # Tạo chuỗi ngày từ day, month, year
        date_str = f"{date_request.year}-{date_request.month:02d}-{date_request.day:02d}"
        
        # Validate ngày hợp lệ
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ngày không hợp lệ: {date_str}"
            )
        
        # Gọi hàm xử lý chính
        result_file = run_daily_digest(date_str, model=date_request.model)
        
        return {
            "success": True,
            "message": f"Đã tạo tóm tắt thành công cho ngày {date_str}",
            "date": date_str,
            "model": date_request.model,
            "output_file": result_file,
            "username": username
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lỗi khi xử lý: {str(e)}"
        )

@app.get("/generate-digest")
async def generate_daily_digest_get(
    day: int,
    month: int,
    year: int,
    model: Optional[str] = "gemini-2.5-flash",
    username: str = Depends(verify_password)
):
    """
    Tạo tóm tắt các bài báo nghiên cứu cho một ngày cụ thể (GET method).
    
    Yêu cầu xác thực Basic Auth với mật khẩu từ file .env.
    
    Args:
        day: Ngày (1-31)
        month: Tháng (1-12)
        year: Năm (2000-2100)
        model: Mô hình LLM để sử dụng (mặc định: gemini-2.5-flash)
        username: Tên người dùng từ xác thực (tự động lấy từ Depends)
    
    Returns:
        Thông tin về quá trình xử lý và đường dẫn file kết quả
    """
    try:
        # Validate input
        if not (1 <= day <= 31):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ngày phải trong khoảng 1-31"
            )
        if not (1 <= month <= 12):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tháng phải trong khoảng 1-12"
            )
        if not (2000 <= year <= 2100):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Năm phải trong khoảng 2000-2100"
            )
        
        # Tạo chuỗi ngày từ day, month, year
        date_str = f"{year}-{month:02d}-{day:02d}"
        
        # Validate ngày hợp lệ
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ngày không hợp lệ: {date_str}"
            )
        
        # Gọi hàm xử lý chính
        result_file = run_daily_digest(date_str, model=model)
        
        return {
            "success": True,
            "message": f"Đã tạo tóm tắt thành công cho ngày {date_str}",
            "date": date_str,
            "model": model,
            "output_file": result_file,
            "username": username
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lỗi khi xử lý: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

