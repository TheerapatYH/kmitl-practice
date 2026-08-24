from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "KMITL Practice API"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "name": "Test Student"
    }