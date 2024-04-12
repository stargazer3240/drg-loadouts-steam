import os

ICON_SUFFIX = "_icon.png"
PNG_EXCLUDE = "png:exclude-chunks=date,tIME"

BASE_DIR = os.path.join(os.path.relpath("../"), "src", "icons", "modifications")
FRAME_PATH = os.path.join(BASE_DIR, "frames")
UPGRADE_PATH = os.path.join(BASE_DIR, "upgrades")
OVERCLOCK_PATH = os.path.join(BASE_DIR, "overclocks")
DEST_PATH = os.path.join(os.path.relpath("../"), "dest")

FRAMES = os.listdir(FRAME_PATH)
UPGRADES = os.listdir(UPGRADE_PATH)
