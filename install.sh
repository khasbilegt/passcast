#!/usr/bin/env bash
# shellcheck shell=dash
set -u

command -v "curl" > /dev/null 2>&1 || { echo "curl command not found" >&2; exit 1; }
command -v "rm" > /dev/null 2>&1 || { echo "rm command not found" >&2; exit 1; }
command -v "mkdir" > /dev/null 2>&1 || { echo "mkdir command not found" >&2; exit 1; }
command -v "rmdir" > /dev/null 2>&1 || { echo "rmdir command not found" >&2; exit 1; }
command -v "pass" > /dev/null 2>&1 || { echo "pass command not found" >&2; exit 1; }

OUTPUT_PATH="${HOME}/.config/raycast/scripts"

main() {
    if [ ! -d "${HOME}/.password-store" ]; then
        echo "${HOME}/.password-store directory not found" >&2;
        exit 1;
    fi

    if [ ! -d "${HOME}/.config" ]; then
        mkdir -p "${HOME}/.config"
    fi

    if [ -d "${HOME}/.config/raycast" ]; then
        if [ -d "${OUTPUT_PATH}" ]; then
            # Removing outdated version
            rmdir "${OUTPUT_PATH}"
        fi

        mkdir -p "${OUTPUT_PATH}"
    else
        mkdir -p "${OUTPUT_PATH}"
    fi

    curl https://raw.githubusercontent.com/khasbilegt/passcast/main/passcast.py -o "${OUTPUT_PATH}/passcast.py"
}

main || exit 1
