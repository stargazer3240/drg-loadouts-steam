import os
import subprocess
from constants import (
    OVERCLOCK_PATH,
    UPGRADE_PATH,
    DEST_PATH,
    ICON_SUFFIX,
    PNG_EXCLUDE,
    UPGRADES,
)
from get_upgrade_name import get_upgrade_name


def run_convert(src, size, dest):
    subprocess.run(["convert", src, "-define", PNG_EXCLUDE, "-resize", size, dest])


def append_px(size):
    return size + "px"


# This loop creates the 16px version of each upgrade/overclock icon.
SIZE = "16"
for upgrade in UPGRADES:
    src = os.path.join(UPGRADE_PATH, upgrade)
    name = get_upgrade_name(upgrade)
    size_px = append_px(SIZE)
    dest = os.path.join(DEST_PATH, name + "_" + size_px + ICON_SUFFIX)
    run_convert(src, SIZE, dest)

# This loop creates the 64, 32 and 16 pixel version of each overclock composition.
sizes = ("16", "32", "64")
OVERCLOCKS = os.listdir(OVERCLOCK_PATH)
for overclock in OVERCLOCKS:
    src = os.path.join(OVERCLOCK_PATH, overclock)
    for sz in sizes:
        name = overclock[: overclock.find(ICON_SUFFIX)]
        size_px = append_px(sz)
        dest = os.path.join(DEST_PATH, name + "_" + size_px + ICON_SUFFIX)
        run_convert(src, sz, dest)
