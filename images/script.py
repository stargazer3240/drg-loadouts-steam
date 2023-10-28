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
        oc_type = "clean"
    elif "Balanced" in frame:
        subfolder = "02-Balanced/"
        oc_type = "balanced"
    elif "Unstable" in frame:
        subfolder = "03-Unstable/"
        oc_type = "unstable"

    frame = frames_path + frame
    dest_path = base_dir + "overclocks/png/" + subfolder

    for upgrade in upgrades:
        upgrade = upgrades_path + upgrade
        dest = dest_path + "0" + str(i) + "." + oc_type + ".png"
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
