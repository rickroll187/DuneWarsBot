"""
API/Webhook Endpoint - Code Bros
Trigger bot actions from your phone, scripts, or other tools!
"""
from flask import Flask, request, jsonify
import threading
from config import log

api_app = Flask(__name__)

@api_app.route("/trigger", methods=["POST"])
def trigger_action():
    data = request.json or {}
    action = data.get("action", "")
    log(f"API trigger received: {action}")
    # TODO: Call your main bot logic here, e.g. train.run() or combat.run()
    return jsonify({"status": "ok", "action": action})

def run_api():
    threading.Thread(target=lambda: api_app.run(host="0.0.0.0", port=5050, debug=False, use_reloader=False), daemon=True).start()
    log("API endpoint running at http://localhost:5050/trigger")