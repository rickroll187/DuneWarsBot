"""
Utility Functions - Code Bros
Because DRY is the spice of life.
"""
import random

def random_chance(probability):
    """Returns True with the given probability [0,1]."""
    return random.random() < probability

def safe_int(val, default=0):
    try:
        return int(val)
    except Exception:
        return default

def clamp(val, minval, maxval):
    return max(min(val, maxval), minval)