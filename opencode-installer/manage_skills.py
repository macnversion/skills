#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path

def get_source_skills_dir():
    # Assumes script is in <repo>/opencode-installer/manage_skills.py
    # Skills are in <repo>/skills
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    skills_dir = repo_root / "skills"
    
    if not skills_dir.exists() or not skills_dir.is_dir():
        print(f"Error: Could not locate source skills directory at {skills_dir}")
        sys.exit(1)
        
    return skills_dir

def get_dest_skills_dir():
    # Default Open Code global skills directory
    dest_dir = Path.home() / ".config" / "opencode" / "skills"
    return dest_dir

def list_installed_skills(dest_root):
    if not dest_root.exists():
        print("No skills installed yet (destination directory does not exist).")
        return

    skills = [d.name for d in dest_root.iterdir() if d.is_dir() and not d.name.startswith(".")]
    
    if not skills:
        print("No skills installed.")
    else:
        print(f"Installed Skills ({len(skills)}):")
        for skill in sorted(skills):
            print(f" - {skill}")

def install_skill(plugin_name, source_path, dest_path):
    print(f"Installing '{plugin_name}'...")
    
    if not source_path.exists():
        print(f"  Warning: Source skill '{plugin_name}' not found at {source_path}. Skipping.")
        return False

    try:
        # 1. Remove destination if it exists (Overwrite behavior)
        if dest_path.exists():
            print(f"  Removing existing installation at {dest_path}")
            shutil.rmtree(dest_path)
        
        # 2. Create parent directory if needed
        dest_path.parent.mkdir(parents=True, exist_ok=True)
            
        # 3. Copy source to destination
        shutil.copytree(source_path, dest_path)
        print(f"  ✅ Successfully installed to {dest_path}")
        return True
        
    except Exception as e:
        print(f"  ❌ Error installing {plugin_name}: {e}")
        return False

def remove_skill(plugin_name, dest_path):
    print(f"Removing '{plugin_name}'...")
    
    if not dest_path.exists():
        print(f"  Warning: Skill '{plugin_name}' is not installed (path {dest_path} not found). Skipping.")
        return False
        
    try:
        shutil.rmtree(dest_path)
        print(f"  ✅ Successfully removed {dest_path}")
        return True
    except Exception as e:
        print(f"  ❌ Error removing {plugin_name}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Manage Open Code skills (Install, List, Remove).")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Install Command
    install_parser = subparsers.add_parser("install", help="Install or Update (Overwrite) skills")
    install_parser.add_argument("skill", nargs="?", help="Name of the skill to install")
    install_parser.add_argument("-a", "--all", action="store_true", help="Install ALL available skills")

    # List Command
    subparsers.add_parser("list", help="List installed skills")

    # Remove Command
    remove_parser = subparsers.add_parser("remove", help="Remove skills")
    remove_parser.add_argument("skill", nargs="?", help="Name of the skill to remove")
    remove_parser.add_argument("-a", "--all", action="store_true", help="Remove ALL installed skills")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    source_root = get_source_skills_dir()
    dest_root = get_dest_skills_dir()

    print(f"Source:      {source_root}")
    print(f"Destination: {dest_root}")
    print("-" * 50)

    if args.command == "list":
        list_installed_skills(dest_root)
        
    elif args.command == "install":
        if not args.skill and not args.all:
            print("Error: Please specify a skill name or use --all")
            sys.exit(1)
            
        if args.all:
            skills_to_install = [
                d.name for d in source_root.iterdir() 
                if d.is_dir() and not d.name.startswith(".")
            ]
            print(f"Found {len(skills_to_install)} skills to install.")
        else:
            skills_to_install = [args.skill]

        success_count = 0
        for skill_name in skills_to_install:
            src = source_root / skill_name
            dst = dest_root / skill_name
            if install_skill(skill_name, src, dst):
                success_count += 1
        print("-" * 50)
        print(f"Done. Installed {success_count}/{len(skills_to_install)} skills.")

    elif args.command == "remove":
        if not args.skill and not args.all:
            print("Error: Please specify a skill name or use --all")
            sys.exit(1)
            
        if args.all:
            if not dest_root.exists():
                print("No skills to remove.")
                sys.exit(0)
                
            skills_to_remove = [
                d.name for d in dest_root.iterdir() 
                if d.is_dir() and not d.name.startswith(".")
            ]
            print(f"Found {len(skills_to_remove)} skills to remove.")
        else:
            skills_to_remove = [args.skill]

        success_count = 0
        for skill_name in skills_to_remove:
            dst = dest_root / skill_name
            if remove_skill(skill_name, dst):
                success_count += 1
        print("-" * 50)
        print(f"Done. Removed {success_count}/{len(skills_to_remove)} skills.")

if __name__ == "__main__":
    main()
