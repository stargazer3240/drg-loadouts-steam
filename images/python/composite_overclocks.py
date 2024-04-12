import os
import subprocess
from constants import (
    FRAME_PATH,
    UPGRADE_PATH,
    PNG_EXCLUDE,
    ICON_SUFFIX,
    OVERCLOCK_PATH,
    FRAMES,
    UPGRADES,
)
from get_upgrade_name import get_upgrade_name


def composite_overclock(upgrade, oc_type, frame) -> None:
    if "48px" in upgrade:
        name = get_upgrade_name(upgrade)
        upgrade = os.path.join(UPGRADE_PATH, upgrade)
        dest = os.path.join(OVERCLOCK_PATH, name + "_" + oc_type + ICON_SUFFIX)
        run_composite(upgrade, frame, dest)


def run_composite(upgrade, frame, dest):
    subprocess.run(
        [
            "composite",
            "-gravity",
            "center",
            "-define",
            PNG_EXCLUDE,
            upgrade,
            frame,
            dest,
        ]
    )


def find_oc_type(frame):
    oc_type = ""
    if "Clean" in frame:
        oc_type = "Clean"
    elif "Balanced" in frame:
        oc_type = "Balanced"
    elif "Unstable" in frame:
        oc_type = "Unstable"

    return oc_type


# This loop matchs each of the three frames with each upgrade/overclock icon and
# then composite the overclock icons
for frame in FRAMES:
    oc_type = find_oc_type(frame)
    frame_with_path = os.path.join(FRAME_PATH, frame)
    for upgrade in UPGRADES:
        composite_overclock(upgrade, oc_type, frame_with_path)
