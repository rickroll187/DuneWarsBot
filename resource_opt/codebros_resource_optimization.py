def smart_spice_spending(driver, config, shared_state):
    """
    Optimize resource (spice) usage:
    - Keeps enough spice in hand (spice_buffer)
    - Prioritizes upgrades (bank/mothership/tech) if thresholds are met
    - Never spends all spice at once (randomizes amounts)
    - Logs every decision with a bro joke
    """
    spice = get_current_spice(driver)
    buffer = config["spice_buffer"]
    upgrades = [
        ("bank", can_upgrade_bank, upgrade_bank),
        ("mothership", can_upgrade_mothership, upgrade_mothership),
        ("tech", can_upgrade_tech, upgrade_tech),
    ]
    # If we have enough for an upgrade and are above the buffer, prioritize upgrades
    for name, can_fn, upgrade_fn in upgrades:
        if can_fn(driver) and spice > buffer * 1.2:
            code_bros_log(f"Resource Optimizer: Upgrading {name}—spice to grow, not to show!")
            with_retries(upgrade_fn, driver)
            spice = get_current_spice(driver)  # Refresh after upgrade

    # If too much spice on hand, bank some, but not all!
    if spice > buffer * 2:
        to_bank = spice - buffer - random.randint(int(buffer*0.2), int(buffer*0.7))
        code_bros_log(f"Resource Optimizer: Banking {to_bank:,} spice. Gotta keep some for Fremen pizza night.")
        with_retries(bank_spice, driver, amount=to_bank)

    # If below buffer and not in a defense panic, skip spending
    if spice < buffer:
        code_bros_log("Resource Optimizer: Spice is tight, time to hoard like a sandworm.")
        return

    # Otherwise, spend small random amounts on units/repairs
    spend = min(spice - buffer, random.randint(int(buffer*0.1), int(buffer*0.4)))
    if spend > 0:
        code_bros_log(f"Resource Optimizer: Spending {spend:,} spice for upgrades and gear. Spice must flow!")
        with_retries(auto_buy_weapons, driver, amount=spend)

# Example: Call this from your bank_task, mothership_task, or a new optimization_task (threaded)