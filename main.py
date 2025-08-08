from modules.ai_strategy import predict_ai
from modules.data_logger import log_gameplay
import random

def get_features_and_mode():
    # Simulate all features including toggles
    mode = random.choice([0, 1])  # 0 = Defend, 1 = Attack
    current_spice = random.randint(0, 100)
    enemy_strength = random.randint(0, 100)
    my_defense = random.randint(0, 100)
    farm_mode = random.choice([0, 1])   # 0 = Farm, 1 = Raid
    war_mode = random.choice([0, 1])
    auto_train = random.choice([0, 1])
    auto_buy_weapons = random.choice([0, 1])
    auto_repair = random.choice([0, 1])
    mothership = random.choice([0, 1])
    return [
        mode, current_spice, enemy_strength, my_defense,
        farm_mode, war_mode, auto_train, auto_buy_weapons, auto_repair, mothership
    ], mode

def get_result():
    # Simulate the outcome
    return random.randint(0, 1)

if __name__ == "__main__":
    features, mode = get_features_and_mode()
    action = "ATTACK" if mode == 1 else "DEFEND"
    decision = predict_ai(features)
    if decision:
        print(f"AI says: Go for {action}!")
    else:
        print(f"AI says: Do NOT {action} right now.")
    # Log the outcome for future training
    result = get_result()
    log_gameplay(features, result)
    print(f"Game outcome logged: {'Win' if result else 'Loss'} (mode: {action})")