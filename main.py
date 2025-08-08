from modules.ai_strategy import predict_ai
from modules.data_logger import log_gameplay
import random

def get_features_and_mode():
    # Simulate all features including toggles and resource scenario
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
    current_resources = random.randint(0, 200)
    under_attack_count = random.randint(0, 5)

    # Simulate costs
    training_cost = 30
    weapon_cost = 40
    repair_cost = 20

    # Self-defense logic
    if under_attack_count > 1 and my_defense < enemy_strength:
        print("Bro, we're under multiple attacks! Prioritizing self-defense and repairs.")
        mode = 0  # Set to DEFEND
        auto_repair = 1

    # Auto actions if enough resources
    if auto_train and current_resources >= training_cost:
        print("Auto-training enabled and resources available. Training, bro!")
        current_resources -= training_cost
    if auto_buy_weapons and current_resources >= weapon_cost:
        print("Auto-buying weapons, bro!")
        current_resources -= weapon_cost
    if auto_repair and current_resources >= repair_cost:
        print("Auto-repairing, bro!")
        current_resources -= repair_cost

    return [
        mode, current_spice, enemy_strength, my_defense,
        farm_mode, war_mode, auto_train, auto_buy_weapons, auto_repair, mothership,
        current_resources, under_attack_count
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