#!/bin/bash
set -euo pipefail

LOG_FILE="another-dotfiles$(date +%Y%m%d_%H%M).log"

log_message() {
	echo -e "[$(date +'%Y-%m-%d %H:%M:%S') $1]" | tee -a "$LOG_FILE"
}

if ! command -v python3 &> /dev/null; then
	echo "Python not found, installing (╥﹏╥)"

	if command -v apk &> /dev/null; then
		sudo apk -U upgrade
		sudo apk add python

	elif command -v pacman &> /dev/null; then
		sudo pacman -Syu
		sudo pacman -S python

	elif command -v apt &> /dev/null; then
		sudo apt update && sudo apt upgrade
		sudo apt install python3

	elif command -v dnf &> /dev/null; then
		sudo dnf update
		sudo dnf install python

	else
		echo "Unsupported distro"
		exit 1
	fi
fi

echo "Running Python script"
python3 packages/packages.py

echo "Applying dotfiles"
python3 dotfiles/dotfiles.py
