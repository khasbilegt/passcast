#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title pass
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🔐
# @raycast.argument1 { "type": "text", "placeholder": "Path (e.g Email/zx2c4.com)" }
# @raycast.argument2 { "type": "text", "placeholder": "Password", "secure": true }
# @raycast.packageName Utils

# Documentation:
# @raycast.description Unix pass password manager integration for Raycast
# @raycast.author Khasbilegt.TS
# @raycast.authorURL https://github.com/khasbilegt

import subprocess
import sys

from pathlib import Path

PASSWORD_STORE_PATH = Path("~/.password-store").expanduser()
PASSWORD_PATH = (PASSWORD_STORE_PATH / Path(f"{sys.argv[1]}.gpg")).resolve()

try:
    if PASSWORD_PATH.exists():
        subprocess.run(
            ["gpgconf", "--reload", "gpg-agent"],
            check=True,
            capture_output=True,
        )
        content = subprocess.run(
            [
                "gpg",
                "--decrypt",
                "--pinentry-mode",
                "loopback",
                "--passphrase",
                f"{sys.argv[2]}",
                f"{PASSWORD_PATH}",
            ],
            text=True,
            check=True,
            capture_output=True,
        )
        copied = subprocess.run(
            ["pass", "-c", f"{sys.argv[1]}"],
            text=True,
            check=True,
            capture_output=True,
        )

        print(f"🔑 {content.stdout}")
        print(f"🤖 {copied.stdout}")
    else:
        print("🔴 Password not found!")
except subprocess.CalledProcessError as e:
    print(f"{e.stderr}")
