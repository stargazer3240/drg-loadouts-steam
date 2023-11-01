import os
import subprocess

icon_suffix = "_icon.png"
png_exclude = "png:exclude-chunks=date,tIME"

base_dir = os.path.join(os.path.relpath("."), "icons")
frames_path = os.path.join(base_dir, "overclocks", "webp", "frames")
upgrades_path = os.path.join(base_dir, "upgrades")
upgrades_src = os.path.join(upgrades_path, "webp")
frames = os.listdir(frames_path)
upgrades = os.listdir(upgrades_src)


def run_composite(upgrade: str, frame: str, dest: str) -> None:
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


def get_upgrade_name(upgrade: str) -> str:
    name = ""
    if "Overclock" in upgrade:
        name = upgrade[20:-5]
    elif "Upgrade" in upgrade:
        name = upgrade[18:-5]
    return name


def composite_overclock(upgrade: str) -> None:
    if "48px" in upgrade:
        name = get_upgrade_name(upgrade)
        upgrade = os.path.join(upgrades_path, upgrade)
        dest = os.path.join(dest_path, name + "_" + oc_type + icon_suffix)
        run_composite(upgrade, frame, dest)


def find_oc_type(frame: str) -> tuple[str, str]:
    subfolder = ""
    oc_type = ""
    if "Clean" in frame:
        subfolder = "01-Clean"
        oc_type = "Clean"
    elif "Balanced" in frame:
        subfolder = "02-Balanced"
        oc_type = "Balanced"
    elif "Unstable" in frame:
        subfolder = "03-Unstable"
        oc_type = "Unstable"

    return subfolder, oc_type


# This loop matchs each of the three frames with each upgrade/overclock icon and
# then uses Magick composite.
for frame in frames:
    subfolder, oc_type = find_oc_type(frame)
    frame = os.path.join(frames_path, frame)
    dest_path = os.path.join(base_dir, "overclocks", "png", subfolder)
    for upgrade in upgrades:
        composite_overclock(upgrade)


def run_convert(src: str, size: str, dest: str) -> None:
    subprocess.run(["convert", src, "-define", png_exclude, "-resize", size, dest])


def append_px(size: str) -> str:
    return size + "px"


# This loop creates the 16px version of each upgrade/overclock icon.
size = "16"
for upgrade in upgrades:
    src = os.path.join(upgrades_src, upgrade)
    name = get_upgrade_name(upgrade)
    size_px = append_px(size)
    dest = os.path.join(upgrades_path, "png", name + "_" + size_px + icon_suffix)
    run_convert(src, size, dest)


# This loop creates the 64, 32 and 16 pixel version of each overclock composition.
depth = 4
sizes = ("16", "32", "64")
overclocks_path = os.path.join(base_dir, "overclocks", "png")
for root, dirs, files in os.walk(overclocks_path):
    if root.count(os.sep) <= depth:
        for name in files:
            src = os.path.join(root, name)
            for i in range(0, 3):
                size_px = append_px(sizes[i])
                new_name = name[: name.find("icon")]
                dest = os.path.join(root, size_px, new_name + size_px + icon_suffix)
                run_convert(src, sizes[i], dest)
