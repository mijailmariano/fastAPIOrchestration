## FastAPI Orchestration 

A FastAPI application to orchestrate multiple endpoints. Incorporating Swagger UI and ReDoc for API documentation and testing.


### Setup

1. Clone the repository
2. Create and activate a Conda environment:
   ```
   conda create -n fastapienv "python>=3.12 -y"
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

**Endpoint Access:**
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

*Refer to Swagger UI or ReDoc for detailed API specifications.*

### Program Orchestration Diagram


```mermaid
graph LR
    A[Client] -->|HTTP Request| B[FastAPI App]
    B -->|Route| C{Routers}
    C -->|/products| D[Products Router]
    C -->|/categories| E[Categories Router]
    C -->|/reviews| F[Reviews Router]
    D -->|Calls| G[Product Service]
    E -->|Calls| H[Category Service]
    F -->|Calls| I[Review Service]
    G -->|Uses| J[Pydantic Models]
    H -->|Uses| J
    I -->|Uses| J
    G -->|Accesses| K[Sample Data]
    H -->|Accesses| K
    I -->|Accesses| K
    B -->|Generate| L[Swagger UI]
    B -->|Generate| M[ReDoc]