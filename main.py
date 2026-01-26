import os
import requests
import time
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()


# -------------- Envs -------------
# SLACK :3
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
# Coolify
COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_API_KEY = os.getenv("COOLIFY_API_KEY")


app = App(token=SLACK_BOT_TOKEN)


@app.command("/ping-44")
def ping_pong(ack, respond):
    import time
    start = time.time()
    ack()
    latency = (time.time() - start) * 1000
    respond(f"pong! latency: {latency}ms")


@app.command("/coolify-version")
def coolify_ver(ack, respond):
        ack()
        response = requests.get(
            f"{COOLIFY_API_URL}/version",
            headers={"Authorization" : f"Bearer {COOLIFY_API_KEY}"}
            )
        if response.status_code == 200:
            respond(f"Coolify Ver: {response.text}")
        else:
            respond(f"Error! {response.status_code}")



@app.command("/coolify-health-status")
def coolify_status(ack, respond):
     ack()
     response = requests.get(
          f"{COOLIFY_API_URL}/health",
          headers={"Authorization" : f"Bearer {COOLIFY_API_KEY}"}
        )
     if response.status_code == 200:
          respond(f"Coolify returned health status: {response.text}")
     else:
          respond(f"Error! {response.status_code}")
 

















if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    