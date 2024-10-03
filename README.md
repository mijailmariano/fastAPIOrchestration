## FastAPIOrchestration

A prototype FastAPI application demonstrating multiple endpoints with Swagger UI and ReDoc integration.

### Setup

1. Clone the repository
2. Create and activate a Conda environment:
   ```
   conda create -n fastapienv python>=3.9 -y
   conda activate fastapienv
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### File Structure

```
app/
├── main.py            # FastAPI app initialization
├── models/            # Pydantic models
├── routers/           # API route handlers
└── data/              # Sample data
tests/                 # Pytest files
```


### Deploy

```
uvicorn app.main:app --reload
```

**Access:**
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc


### Deployment Stack

- FastAPI
- Pydantic
- Uvicorn (ASGI server)
- Pytest

### API Endpoints

- `/products/`
- `/categories/`
- `/reviews/`

Refer to Swagger UI or ReDoc for detailed API specifications.
