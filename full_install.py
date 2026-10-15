#!/usr/bin/env python3
"""Installs EduAi_Pro's backend and frontend dependencies, and creates desktop
shortcut that launches the app.

Usage:
    python3 full_install.py

Run from anywhere - the script locates the repo root from its own path.
"""
import os
import platform
import shutil
import stat
import subprocess
import sys
import venv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
BACKEND_DIR = REPO_ROOT / "backend"
FRONTEND_DIR = REPO_ROOT / "frontend"
VENV_DIR = BACKEND_DIR / ".venv"
ICONS_DIR = REPO_ROOT / "assets" / "icons"
ICON_ICO = ICONS_DIR / "EduAi_Pro.ico"
ICON_ICNS = ICONS_DIR / "EduAi_Pro.icns"
ICON_PNG = ICONS_DIR / "EduAi_Pro.png"
IS_WINDOWS = platform.system() == "Windows"
IS_MAC = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"
MIN_PYTHON = (3, 9)
MIN_NODE = (20, 19, 0)


def check_python_version():
    if sys.version_info < MIN_PYTHON:
        print(
            f"EduAi_Pro requires Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ - "
            f"found {platform.python_version()}. Install a newer Python and re-run this script."
        )
        sys.exit(1)


def ensure_node():
    """Installs Node.js via the OS package manager if npm isn't already on PATH."""
    if shutil.which("npm"):
        raw_version = subprocess.check_output(
            ["node", "--version"], text=True
        ).strip().lstrip("v")
        try:
            current = tuple(int(part) for part in raw_version.split(".")[:3])
        except ValueError:
            current = (0, 0, 0)
        supported = (
            current[0] == 20 and current >= MIN_NODE
        ) or current >= (22, 12, 0)
        if not supported:
            print(
                f"EduAi_Pro requires Node.js {'.'.join(map(str, MIN_NODE))}+ "
                f"(or Node.js 22.12+); found {raw_version}. "
                "Upgrade Node.js from https://nodejs.org and re-run this installer."
            )
            sys.exit(1)
        return
    print("\n== Node.js not found - attempting to install it ==")
    if IS_MAC and shutil.which("brew"):
        run(["brew", "install", "node"])
    elif IS_LINUX and shutil.which("apt-get"):
        run(["sudo", "apt-get", "update"])
        run(["sudo", "apt-get", "install", "-y", "nodejs", "npm"])
    elif IS_WINDOWS and shutil.which("winget"):
        run(["winget", "install", "-e", "--id", "OpenJS.NodeJS.LTS"])
    else:
        print(
            "Could not auto-install Node.js on this system. "
            "Install it manually from https://nodejs.org and re-run this script."
        )
        sys.exit(1)

    if not shutil.which("npm"):
        print("Node.js install finished but npm is still not on PATH - open a new terminal and re-run this script.")
        sys.exit(1)


def venv_python() -> Path:
    return VENV_DIR / ("Scripts/python.exe" if IS_WINDOWS else "bin/python")


def run(cmd, cwd=None):
    print(f"$ {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def install_backend():
    print("\n== Installing backend ==")
    if not venv_python().exists():
        venv.EnvBuilder(with_pip=True).create(VENV_DIR)
    run([str(venv_python()), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(venv_python()), "-m", "pip", "install", "-r", str(BACKEND_DIR / "requirements.txt")])


def prepare_database():
    """Create/update the configured SQL database and import legacy JSON.

    DATABASE_URL may point at PostgreSQL. When it is not set, EduAI_Pro uses
    its documented local SQLite fallback so the one-file installer remains
    useful on computers that do not have Docker or PostgreSQL installed.
    """
    print("\n== Preparing EduAI_Pro database ==")
    run([str(venv_python()), "-m", "alembic", "upgrade", "head"], cwd=BACKEND_DIR)
    run([str(venv_python()), "-m", "scripts.migrate_json_to_db"], cwd=BACKEND_DIR)


def install_frontend():
    print("\n== Installing frontend ==")
    ensure_node()
    run([shutil.which("npm"), "install"], cwd=FRONTEND_DIR)


def write_launcher() -> Path:
    """Writes a script that starts the backend and frontend dev servers and
    opens the app in a browser, returning its path."""
    if IS_WINDOWS:
        launcher = REPO_ROOT / "start_EduAi_Pro.bat"
        py = venv_python()
        npm = shutil.which("npm") or "npm"
        launcher.write_text(
            "@echo off\r\n"
            f'cd "{BACKEND_DIR}"\r\n'
            f'start "EduAi_Pro backend" "{py}" -m uvicorn app.main:app --port 8000\r\n'
            f'cd "{FRONTEND_DIR}"\r\n'
            f'start "EduAi_Pro frontend" "{npm}" run dev\r\n'
            "timeout /t 3 >nul\r\n"
            "start http://localhost:5173\r\n"
        )
    else:
        launcher = REPO_ROOT / "start_EduAi_Pro.sh"
        py = venv_python()
        open_cmd = "open" if IS_MAC else "xdg-open"
        launcher.write_text(
            "#!/usr/bin/env bash\n"
            f'cd "{BACKEND_DIR}" && "{py}" -m uvicorn app.main:app --port 8000 &\n'
            f'cd "{FRONTEND_DIR}" && npm run dev &\n'
            "sleep 3\n"
            f"{open_cmd} http://localhost:5173\n"
            "wait\n"
        )
        launcher.chmod(launcher.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    print(f"Launcher written to {launcher}")
    return launcher


def desktop_dirs():
    """Return the normal Desktop and every configured OneDrive Desktop.

    Windows always receives a normal Desktop target. A Desktop directory is
    also created under each configured OneDrive root, ensuring the shortcut is
    available in both locations even when Known Folder Move is enabled.
    """
    home = Path.home()
    candidates = [home / "Desktop"]

    onedrive_roots = []
    for variable in ("OneDrive", "ONEDRIVE", "OneDriveConsumer", "OneDriveCommercial"):
        value = os.environ.get(variable)
        if value:
            onedrive_roots.append(Path(value))
    default_onedrive = home / "OneDrive"
    if default_onedrive.exists():
        onedrive_roots.append(default_onedrive)
    candidates.extend(root / "Desktop" for root in onedrive_roots)

    seen, dirs = set(), []
    for d in candidates:
        key = str(d).casefold() if IS_WINDOWS else str(d)
        if key in seen:
            continue
        try:
            d.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            print(f"Could not prepare Desktop folder {d}: {exc}")
            continue
        seen.add(key)
        dirs.append(d)
    return dirs


def create_shortcut_windows(desktop_dir: Path, launcher: Path):
    shortcut_path = desktop_dir / "EduAi_Pro.lnk"
    try:
        icon_line = (
            f"$shortcut.IconLocation = '{str(ICON_ICO).replace(chr(39), chr(39) * 2)}'; "
            if ICON_ICO.exists() else ""
        )
        ps_script = (
            "$shell = New-Object -ComObject WScript.Shell; "
            f"$shortcut = $shell.CreateShortcut('{str(shortcut_path).replace(chr(39), chr(39) * 2)}'); "
            f"$shortcut.TargetPath = '{str(launcher).replace(chr(39), chr(39) * 2)}'; "
            f"$shortcut.WorkingDirectory = '{str(REPO_ROOT).replace(chr(39), chr(39) * 2)}'; "
            f"{icon_line}"
            "$shortcut.Save()"
        )
        run(["powershell.exe", "-NoProfile", "-Command", ps_script])
        print(f"Shortcut created: {shortcut_path}")
    except (OSError, subprocess.CalledProcessError):
        fallback = desktop_dir / "EduAi_Pro.bat"
        shutil.copy(launcher, fallback)
        print(f"Could not create a .lnk shortcut; copied a launcher to {fallback}.")


def create_shortcut_mac(desktop_dir: Path, launcher: Path):
    """Wraps the launcher in a minimal .app bundle so Finder/Dock show the
    EduAi_Pro icon instead of a generic script icon."""
    if not ICON_ICNS.exists():
        shortcut_path = desktop_dir / "EduAi_Pro.command"
        shutil.copy(launcher, shortcut_path)
        shortcut_path.chmod(shortcut_path.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        print(f"Shortcut created: {shortcut_path}")
        return

    app_path = desktop_dir / "EduAi_Pro.app"
    contents = app_path / "Contents"
    macos_dir = contents / "MacOS"
    resources_dir = contents / "Resources"
    macos_dir.mkdir(parents=True, exist_ok=True)
    resources_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy(ICON_ICNS, resources_dir / "EduAi_Pro.icns")

    runner = macos_dir / "EduAi_Pro"
    runner.write_text(f'#!/usr/bin/env bash\nexec "{launcher}"\n')
    runner.chmod(runner.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    (contents / "Info.plist").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
        '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
        '<plist version="1.0"><dict>\n'
        "  <key>CFBundleName</key><string>EduAi_Pro</string>\n"
        "  <key>CFBundleExecutable</key><string>EduAi_Pro</string>\n"
        "  <key>CFBundleIconFile</key><string>EduAi_Pro.icns</string>\n"
        "  <key>CFBundleIdentifier</key><string>com.eduaipro.launcher</string>\n"
        "  <key>CFBundlePackageType</key><string>APPL</string>\n"
        "</dict></plist>\n"
    )
    print(f"Shortcut created: {app_path}")


def create_shortcut_linux(desktop_dir: Path, launcher: Path):
    shortcut_path = desktop_dir / "EduAi_Pro.desktop"
    icon_line = f"Icon={ICON_PNG}\n" if ICON_PNG.exists() else ""
    shortcut_path.write_text(
        "[Desktop Entry]\n"
        "Type=Application\n"
        "Name=EduAi_Pro\n"
        f"Exec={launcher}\n"
        f"Path={REPO_ROOT}\n"
        f"{icon_line}"
        "Terminal=true\n"
    )
    shortcut_path.chmod(shortcut_path.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    print(f"Shortcut created: {shortcut_path}")


def create_shortcuts(launcher: Path):
    dirs = desktop_dirs()
    if not dirs:
        print("No Desktop directory found - skipping shortcut creation.")
        return
    for desktop_dir in dirs:
        if IS_WINDOWS:
            create_shortcut_windows(desktop_dir, launcher)
        elif IS_MAC:
            create_shortcut_mac(desktop_dir, launcher)
        else:
            create_shortcut_linux(desktop_dir, launcher)


def launch(launcher: Path):
    print(f"\n== Starting EduAi_Pro ==\n$ {launcher}")
    if IS_WINDOWS:
        subprocess.Popen(["cmd", "/c", "start", "", str(launcher)], cwd=REPO_ROOT)
    else:
        subprocess.Popen([str(launcher)], cwd=REPO_ROOT)


def main():
    check_python_version()
    install_backend()
    prepare_database()
    install_frontend()
    launcher = write_launcher()
    create_shortcuts(launcher)
    print("\nInstall complete. Double-click the EduAi_Pro desktop shortcut, or run "
          f"{launcher.name} directly, to start the app.")
    launch(launcher)


if __name__ == "__main__":
    main()
