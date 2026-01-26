import os
import time
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()


# -------------- Envs -------------
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")


app = App(token=SLACK_BOT_TOKEN)


@app.command("/ping-44")
def ping_pong(ack, respond):
    import time
    start = time.time()
    ack()
    latency = (time.time() - start) * 1000
    respond(f"pong! latency: {latency}ms")




















if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    