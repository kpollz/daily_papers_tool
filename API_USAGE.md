# Hướng dẫn sử dụng API

## Cài đặt

1. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

2. Tạo file `.env` và thêm mật khẩu:
```env
API_PASSWORD=your_secure_password_here
```

## Khởi động Server

```bash
# Cách 1: Sử dụng uvicorn
uvicorn api:app --host 0.0.0.0 --port 8000

# Cách 2: Chạy trực tiếp
python api.py
```

## Sử dụng API

### 1. Kiểm tra API hoạt động

```bash
curl http://localhost:8000/
```

### 2. Tạo tóm tắt với POST request

```bash
curl -X POST "http://localhost:8000/generate-digest" \
  -u "any_username:your_secure_password_here" \
  -H "Content-Type: application/json" \
  -d '{
    "day": 15,
    "month": 1,
    "year": 2026,
    "model": "gpt-4.1-mini"
  }'
```

### 3. Tạo tóm tắt với GET request

```bash
curl -X GET "http://localhost:8000/generate-digest?day=15&month=1&year=2026&model=gpt-4.1-mini" \
  -u "any_username:your_secure_password_here"
```

### 4. Sử dụng với Python

```python
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8000/generate-digest"
auth = HTTPBasicAuth("any_username", "your_secure_password_here")

# POST method
response = requests.post(
    url,
    auth=auth,
    json={
        "day": 15,
        "month": 1,
        "year": 2026,
        "model": "gpt-4.1-mini"
    }
)

print(response.json())
```

## Xem API Documentation

Khi server đang chạy, truy cập:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Lưu ý

- Username có thể là bất kỳ giá trị nào (chỉ cần password đúng)
- Password phải khớp với giá trị trong file `.env`
- Model mặc định là `gpt-4.1-mini` nếu không chỉ định
- Ngày phải hợp lệ (ví dụ: không có ngày 31/02)

