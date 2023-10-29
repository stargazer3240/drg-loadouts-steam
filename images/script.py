import os
import subprocess

base_dir = "./icons/"
frames_path = base_dir + "overclocks/webp/frames/"
frames = os.listdir(frames_path)
upgrades_path = base_dir + "upgrades/webp/"
upgrades = os.listdir(upgrades_path)
subfolder = ""
oc_type = ""
name = ""
icon = "_icon.png"

for frame in frames:
    if "Clean" in frame:
        subfolder = "01-Clean/"
        oc_type = "Clean"
    elif "Balanced" in frame:
        subfolder = "02-Balanced/"
        oc_type = "Balanced"
    elif "Unstable" in frame:
        subfolder = "03-Unstable/"
        oc_type = "Unstable"

    frame = frames_path + frame
    dest_path = base_dir + "overclocks/png/" + subfolder

    for upgrade in upgrades:
        if "48px" in upgrade:
            if "Overclock" in upgrade:
                name = upgrade[20:-5]
            elif "Upgrade" in upgrade:
                name = upgrade[18:-5]
            upgrade = upgrades_path + upgrade
            dest = dest_path + name + "_" + oc_type + icon
            subprocess.run(
                [
                    "composite",
                    "-gravity",
                    "center",
                    "-define",
                    "png:exclude-chunks=date,tIME",
                    upgrade,
                    frame,
                    dest,
                ]
            )
