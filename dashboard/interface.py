"""
Web Interface Automation - Code Bros
Simple Flask dashboard to monitor and control your bot in style.
"""
from flask import Flask, render_template_string, request, redirect, url_for
import threading
from config import log

app = Flask(__name__)

STATUS = {"running": False, "last_action": "Idle"}

DASHBOARD_HTML = """
<!doctype html>
<title>Code Bros DuneWars Bot Dashboard</title>
<h2>Code Bros DuneWars Bot</h2>
<p>Status: <b>{{ status }}</b></p>
<p>Last action: {{ last_action }}</p>
<form method="post" action="/toggle">
    <button type="submit">{{ 'Stop' if running else 'Start' }}</button>
</form>
"""

def start_bot():
    STATUS["running"] = True
    STATUS["last_action"] = "Bot started"
    log("Bot started from dashboard.")

def stop_bot():
    STATUS["running"] = False
    STATUS["last_action"] = "Bot stopped"
    log("Bot stopped from dashboard.")

@app.route("/")
def index():
    return render_template_string(DASHBOARD_HTML, 
        status="Running" if STATUS["running"] else "Stopped",
        last_action=STATUS["last_action"],
        running=STATUS["running"]
    )

@app.route("/toggle", methods=["POST"])
def toggle():
    if STATUS["running"]:
        stop_bot()
    else:
        start_bot()
    return redirect(url_for('index'))

def run_dashboard():
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False), daemon=True).start()
    log("Dashboard available at http://localhost:5000")

# Example usage: import and call run_dashboard() in main.py