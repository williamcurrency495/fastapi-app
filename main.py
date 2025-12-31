from fastapi import FastAPI, Request, Response

app = FastAPI()

# This must match EXACTLY what you type in the Meta "Verify token" box
VERIFY_TOKEN = "wmiller53814875514099"


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}


@app.get("/webhook/instagram")
async def verify_webhook(request: Request):
    """
    Meta calls this with a GET request one time when you set up the webhook.
    We must send back the 'hub.challenge' value as plain text
    IF the verify token matches.
    """
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
        # Return the challenge as plain text
        return Response(content=challenge, media_type="text/plain")

    # If something is wrong, return 403
    return Response(content="Verification failed", status_code=403)


@app.post("/webhook/instagram")
async def receive_instagram_message(request: Request):
    """
    This will be used later for real messages.
    For now we just log the body and say 'ok'.
    """
    data = await request.json()
    print("Incoming IG webhook:", data)
    return {"status": "received"}
