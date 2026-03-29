from pathlib import Path
import shutil

HOME = Path.home()
DOTFILES = Path("dotfilesconfig")

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

    print(f"Applying {cfg}...")

    dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)

print("Done!")

wall_src = DOTFILES / "Wallpapers"
wall_dst = HOME / "Wallpapers"

wall_dst.mkdir(parents=True, exist_ok=True)

for file in wall_src.iterdir():
    if file.is_file():
        shutil.copy(file, wall_dst)

print("Wallpaper copied")

shutil.copy(
        DOTFILES / "zsh/.zshrc",
        HOME / ".zshrc"
)
