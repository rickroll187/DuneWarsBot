# Code Bros DuneWars Bot

## Prerequisites
- Python 3.8+
- Chrome or Firefox installed
- [Download ChromeDriver](https://sites.google.com/chromium.org/driver/) for Chrome
- [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox  
  (put the driver you need in your PATH or same folder)
- `pip install selenium`

## File Structure

```
dunewars-bot/
├── main.py
├── config.py
├── bot_logic.py
└── README.md
```

## Usage

1. **Edit `config.py`**  
   Set `BROWSER` to `"chrome"` or `"firefox"`.

2. **Add your bot logic**  
   Put your spicy automation steps in `bot_logic.py` (after login).

3. **Run the bot:**
   ```
   python main.py
   ```

4. **Manual login:**  
   Browser opens to login page. Log in (including captcha, if present).

5. **Back to terminal:**  
   When you’re on your base, press Enter for Code Bros magic.

6. **Bot runs!**  
   It’ll visit your dashboard and do whatever you scripted.

---

**Code Bros: Where bots are spicy, code is nice, and every run’s a little slice of Arrakis.**