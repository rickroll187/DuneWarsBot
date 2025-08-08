import datetime

_battle_log = []

def log_battle(player, outcome, details=None):
    """
    Log a battle for a player.
    Args:
        player (str): The name or ID of the player involved.
        outcome (str): The outcome of the battle ("win", "loss", etc.).
        details (str, optional): Extra details about the battle.
    Returns:
        dict: The logged entry.
    """
    entry = {
        "time": datetime.datetime.now().isoformat(),
        "player": player,
        "outcome": outcome,
        "details": details
    }
    _battle_log.append(entry)
    return entry

def get_battle_log():
    """
    Get the full battle log.
    Returns:
        list: All battles logged.
    """
    return list(_battle_log)

def clear_battle_log():
    """
    Clear all battle logs.
    """
    _battle_log.clear()

# 🦾 Code Bros Joke:
# Why did the battle log take a nap? Because it was tired of tracking all those epic wins, bro! 😎
