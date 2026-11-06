# FastAPI Tutorial

A beginner-friendly tutorial for building and running REST APIs with [FastAPI](https://fastapi.tiangolo.com/) and Python.

## What you will learn

- Create a FastAPI application
- Define GET and POST routes
- Validate request data with Pydantic
- Read path and query parameters
- Access automatic API documentation
- Test an API locally

## Prerequisites

- Python 3.9 or newer
- `pip`
- A terminal

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install "fastapi[standard]"
```

## Create your first API

Create a file named `main.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Tutorial")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI tutorial!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, search: str | None = None):
    return {"item_id": item_id, "search": search}


@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

`{item_id}` is a path parameter, while `search` is a query parameter. Pydantic validates the JSON body used by `POST /items/`.

## Run the server

Start the development server from the directory containing `main.py`:

```bash
fastapi dev main.py
```

The API will be available at:

- Application: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

You can also start it with Uvicorn:

```bash
uvicorn main:app --reload
```

## Try the endpoints

### Welcome endpoint

```bash
curl http://127.0.0.1:8000/
```

### Path and query parameters

```bash
curl "http://127.0.0.1:8000/items/42?search=keyboard"
```

### Create an item

```bash
curl -X POST http://127.0.0.1:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Keyboard","price":49.99,"in_stock":true}'
```

Interactive documentation is generated automatically at `/docs`. Use it to view request schemas and test every endpoint from your browser.

## Suggested next steps

1. Add status codes and HTTP exceptions with `HTTPException`.
2. Organize routes using `APIRouter`.
3. Connect a database with SQLAlchemy or SQLModel.
4. Add authentication and authorization.
5. Write endpoint tests with `TestClient` and `pytest`.
6. Configure environment variables and application settings.

## Useful project structure

```text
.
├── .venv/
├── main.py
├── requirements.txt
└── README.md
```

As the application grows, consider moving routers, models, database configuration, and tests into separate packages.

## Production command

For a production-style run:

```bash
pip install "uvicorn[standard]"
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Resources

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Pydantic documentation](https://docs.pydantic.dev/)
- [Uvicorn documentation](https://www.uvicorn.org/)

## License

Add your preferred license before publishing or sharing this tutorial project.
