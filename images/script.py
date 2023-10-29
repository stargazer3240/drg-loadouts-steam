import os
import subprocess

base_dir = os.path.join(os.path.relpath("."), "icons")
frames_path = os.path.join(base_dir, "overclocks", "webp", "frames")
frames = os.listdir(frames_path)
upgrades_path = os.path.join(base_dir, "upgrades", "webp")
upgrades = os.listdir(upgrades_path)
subfolder = ""
oc_type = ""
name = ""
icon = "_icon.png"
png_exclude = "png:exclude-chunks=date,tIME"

for frame in frames:
    if "Clean" in frame:
        subfolder = "01-Clean"
        oc_type = "Clean"
    elif "Balanced" in frame:
        subfolder = "02-Balanced"
        oc_type = "Balanced"
    elif "Unstable" in frame:
        subfolder = "03-Unstable"
        oc_type = "Unstable"

    frame = os.path.join(frames_path, frame)
    dest_path = os.path.join(base_dir, "overclocks", "png", subfolder)

    for upgrade in upgrades:
        if "48px" in upgrade:
            if "Overclock" in upgrade:
                name = upgrade[20:-5]
            elif "Upgrade" in upgrade:
                name = upgrade[18:-5]
            upgrade = os.path.join(upgrades_path, upgrade)
            dest = os.path.join(dest_path, name + "_" + oc_type + icon)
            subprocess.run(
                [
                    "composite",
                    "-gravity",
                    "center",
                    "-define",
                    png_exclude,
                    upgrade,
                    frame,
                    dest,
                ]
            )


def append_px(s: str):
    return s + "px"


depth = 4
sizes = ("16", "32", "64")
overclocks_path = os.path.join(base_dir, "overclocks", "png")
for root, dirs, files in os.walk(overclocks_path):
    if root.count(os.sep) <= depth:
        for name in files:
            src = os.path.join(root, name)
            for i in range(0, 3):
                px = append_px(sizes[i])
                new_name = name[: name.find("icon")]
                dest = os.path.join(root, px, new_name + px + icon)
                subprocess.run(
                    ["convert", src, "-define", png_exclude, "-resize", sizes[i], dest]
                )
