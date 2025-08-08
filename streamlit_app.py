import os
import sys

# Code Bros: This file lets you deploy your dashboard as 'streamlit_app.py' (for Streamlit Cloud or your own convenience)!
# It just imports and runs the real dashboard so you stay DRY and spicy.

DASHBOARD_PATH = os.path.join(os.path.dirname(__file__), "dashboard", "codebros_dashboard_controller.py")

if not os.path.exists(DASHBOARD_PATH):
    print("🔥 Code Bros Error: Dashboard file not found! Expected at:", DASHBOARD_PATH)
    sys.exit(1)

# Streamlit expects a script, so let's execute the dashboard controller directly!
with open(DASHBOARD_PATH, encoding='utf-8') as f:
    code = compile(f.read(), DASHBOARD_PATH, 'exec')
    exec(code, globals())
