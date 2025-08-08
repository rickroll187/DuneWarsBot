import datetime

_spy_log = []

def log_spy_action(player, action, details=None):
    """
    Log a spy action for a player.
    Args:
        player (str): The name or ID of the player being spied on.
        action (str): The type of spy action performed.
        details (str, optional): Extra details about the action.
    Returns:
        dict: The logged entry.
    """
    entry = {
        "time": datetime.datetime.now().isoformat(),
        "player": player,
        "action": action,
        "details": details
    }
    _spy_log.append(entry)
    return entry

def get_spy_log():
    """
    Get the full spy log.
    Returns:
        list: All spy actions logged.
    """
    return list(_spy_log)

def clear_spy_log():
    """
    Clear all spy logs.
    """
    _spy_log.clear()

# 🦾 Code Bros Joke:
# Why did the spy go to the desert?
<<<<<<< HEAD
# To keep an eye on the sand... but he lost track after the 10th grain, bro! 😎
=======
# To keep an eye on the sand... but he lost track after the 10th grain, bro! 😎
>>>>>>> 9dbbc3d6b3088efb8f66c20d28f89c621cf8d14c
