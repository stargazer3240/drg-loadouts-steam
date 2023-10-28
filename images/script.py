import os
import subprocess

base_dir = "./icons/"
frames_path = base_dir + "overclocks/webp/frames/"
frames = os.listdir(frames_path)
upgrades_path = base_dir + "upgrades/webp/"
upgrades = os.listdir(upgrades_path)
subfolder = ""
oc_type = ""

for frame in frames:
    i = 1

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
        upgrade = upgrades_path + upgrade
        if i < 10:
            number = "00" + str(i) + "."
        else:
            number = "0" + str(i) + "."
        dest = dest_path + number + oc_type + ".png"
        if "48px" in upgrade:
            subprocess.run(
                [
                    "composite",
                    "-gravity",
                    "center",
                    upgrade,
                    frame,
                    dest,
                ]
            )
            i += 1
