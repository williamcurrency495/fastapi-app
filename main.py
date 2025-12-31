from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Create a simple route at the homepage
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}
