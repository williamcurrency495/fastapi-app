from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Create a simple route at the homepage
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}

from fastapi import Request

VERIFY_TOKEN = "super-secret-token-change-this"  # pick any random string

@app.get("/webhook/instagram")
async def verify_webhook(request: Request):
    """
    Instagram/Facebook call this once when you set up the webhook
    to verify that your server is real.
    """
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)  # Meta expects the raw challenge back
    return "Verification failed"

@app.post("/webhook/instagram")
async def receive_instagram_message(request: Request):
    """
    This runs every time someone sends your IG account a message.
    For now, we'll just print it and reply with a simple JSON.
    Later, we'll plug in AI and sending DMs back.
    """
    data = await request.json()
    print("Incoming IG webhook:", data)
    return {"status": "received"}
