import os
import sys
import subprocess
import shutil

if os.geteuid() !=0:
    print("WARNING: sudo access needed, nyan ( ˵ •̀ □ •́ ˵ )!")
    os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

PKGAL = [ "xwayland", "sway", "waybar", "rofi", "neovim", "podman", "distrobox" ]
PKGAR = [ "xorg-xwayland", "sway", "waybar", "rofi", "nwg-look", "neovim", "podman", "distrobox" ]
PKGDE = [ "xwayland", "sway", "waybar", "rofi", "nwg-look", "wlogout", "neovim", "podman", "distrobox" ]
PKGFE = [ "xorg-x11-server-Xwayland", "sway", "waybar", "rofi", "wlogout", "neovim", "nix", "nix-core", "nix-daemon", "nix-devel", "nix-doc", "nix-filesystem", "nix-legacy", "nix-libs", "nix-system", "podman", "distrobox" ]

print("Time to installing packages, nyan ( ^ω^ )")

def install(cmd):
    subprocess.run(cmd, check=True)

if shutil.which("apk"):
    install(["apk", "add", *PKGAL])

elif shutil.which("pacman"):
    install([ "pacman", "-S", "--noconfirm", *PKGAR ])

elif shutil.which("apt"):
    install([ "apt", "install", "-y", "--no-install-recommends", *PKGDE ])

elif shutil.which("dnf"):
    install([ "dnf", "install", "-y", "--setopt=install_weak_deps=False", *PKGFE ])

print("It's done, nyan (˵ •̀ ᴗ - ˵ )!!")
