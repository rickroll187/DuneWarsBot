"""
Code Bros Spy Import Debugger 🕵️‍♂️
Quick script to Sherlock your spy.py import woes — tells you if spy.py is missing, broken, or circular.
"""

import os
import importlib.util
import sys

MODULE_DIR = os.path.join(os.path.dirname(__file__), "modules")
SPY_PATH = os.path.join(MODULE_DIR, "spy.py")

def check_file_exists():
    if os.path.isfile(SPY_PATH):
        print("✅ spy.py exists at:", SPY_PATH)
        return True
    else:
        print("❌ spy.py NOT FOUND at:", SPY_PATH)
        return False

def check_for_syntax_error():
    try:
        with open(SPY_PATH, "r") as f:
            compile(f.read(), SPY_PATH, 'exec')
        print("✅ spy.py has valid syntax (no obvious errors)")
        return True
    except Exception as e:
        print("💥 Syntax error in spy.py:", e)
        return False

def try_import_spy():
    sys.path.append(MODULE_DIR)
    try:
        spec = importlib.util.spec_from_file_location("spy", SPY_PATH)
        spy = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(spy)
        print("✅ spy.py imported successfully!")
        return True
    except Exception as e:
        print("💥 Import failed for spy.py:", e)
        return False

def main():
    print("🕵️‍♂️ Code Bros Spy Import Debugger\n------------------------")
    if not check_file_exists():
        print("👉 Create a modules/spy.py file or comment it out in your imports, bro!")
        return
    if not check_for_syntax_error():
        print("👉 Fix the syntax error in modules/spy.py, bro!")
        return
    if not try_import_spy():
        print("👉 Check for circular imports in spy.py (don't import custom_actions if it imports spy!)")
        print("👉 Or drop the code here and Code Bros will roast it!")
        return
    print("🎉 Spy module is good! Add it back to your imports and keep flexing!")
    print("🦾 Code Bros Joke: Why did the spy file disappear? Because even Python spies know how to stay undercover, bro!")

if __name__ == "__main__":
    main()