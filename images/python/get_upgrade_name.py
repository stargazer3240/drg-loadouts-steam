def get_upgrade_name(upgrade):
    if "Overclock" in upgrade:
        name = upgrade[20:-5]
    elif "Upgrade" in upgrade:
        name = upgrade[18:-5]
    else:
        name = upgrade[10:-5]
    return name
