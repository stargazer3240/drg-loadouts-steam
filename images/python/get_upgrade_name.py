def get_upgrade_name(upgrade):
    name = upgrade[10:]
    if "png" in upgrade:
        name = name.removesuffix(".png")
    elif "webp" in upgrade:
        name = name.removesuffix(".webp")
    if "Overclock" in upgrade:
        name = name.removeprefix("Overclock_")
    elif "Upgrade" in upgrade:
        name = name.removeprefix("Upgrade_")
    return name
