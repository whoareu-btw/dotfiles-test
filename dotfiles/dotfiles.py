from pathlib import Path
import shutil

HOME = Path.home()
SCRIPT_DIR = Path(__file__).parent
DOTFILES = SCRIPT_DIR / "dotfilesconfig"

configs = [
        "sway",
        "foot",
        "alacritty",
        "waybar",
        "wlogout",
        "rofi",
        "fuzzel",
        "nvim",
]

for cfg in configs:
    src = DOTFILES / cfg
    dst = HOME / ".config" / cfg

    print(f"Applying {cfg} ...")

    dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)

zshrc_paths = [
        DOTFILES / "zsh/.zshrc",
        DOTFILES / ".zshrc"
]

for path in zshrc_paths:
    if path.exists():
        shutil.copy(path, HOME / ".zshrc")
        break
print("Applying zshrc ...")

wall_src = DOTFILES / "Wallpapers"
wall_dst = HOME / "Wallpapers"

wall_dst.mkdir(parents=True, exist_ok=True)

for file in wall_src.iterdir():
    if file.is_file():
        shutil.copy(file, wall_dst)

print("Copying wallpaper ...")

print ("Done!")
