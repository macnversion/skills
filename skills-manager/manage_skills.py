#!/usr/bin/env python3
"""
Unified Skills Manager for Open Code and Antigravity
Install, list, and remove skills across different AI assistants.
"""
import os
import sys
import shutil
import argparse
from pathlib import Path

def get_source_skills_dir():
    """Get the source directory containing available skills."""
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    
    if not repo_root.exists() or not repo_root.is_dir():
        print(f"Error: Could not locate source skills directory at {repo_root}")
        sys.exit(1)
        
    return repo_root

def get_dest_skills_dir(target, scope="global"):
    """Get destination directory based on target (opencode/antigravity) and scope."""
    if target == "opencode":
        # Open Code only has global scope
        return Path.home() / ".config" / "opencode" / "skills"
    elif target == "antigravity":
        if scope == "global":
            return Path.home() / ".gemini" / "antigravity" / "skills"
        else:  # workspace
            # Find .agent directory by searching upward from current directory
            current = Path.cwd()
            while current != current.parent:
                agent_dir = current / ".agent"
                if agent_dir.exists() and agent_dir.is_dir():
                    return agent_dir / "skills"
                current = current.parent
            # If not found, use current directory
            return Path.cwd() / ".agent" / "skills"
    else:
        print(f"Error: Invalid target '{target}'")
        sys.exit(1)

def list_installed_skills(dest_root):
    """List all installed skills in the destination directory."""
    if not dest_root.exists():
        print("No skills installed yet (destination directory does not exist).")
        return

    skills = [d.name for d in dest_root.iterdir() if d.is_dir() and not d.name.startswith(".")]
    
    if not skills:
        print("No skills installed.")
    else:
        print(f"Installed Skills ({len(skills)}):")
        for skill in sorted(skills):
            print(f"  - {skill}")

def install_skill(skill_name, source_path, dest_path):
    """Install a single skill."""
    print(f"Installing '{skill_name}'...")
    
    if not source_path.exists():
        print(f"  Warning: Source skill '{skill_name}' not found at {source_path}. Skipping.")
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
        print(f"  ❌ Error installing {skill_name}: {e}")
        return False

def remove_skill(skill_name, dest_path):
    """Remove a single skill."""
    print(f"Removing '{skill_name}'...")
    
    if not dest_path.exists():
        print(f"  Warning: Skill '{skill_name}' is not installed (path {dest_path} not found). Skipping.")
        return False
        
    try:
        shutil.rmtree(dest_path)
        print(f"  ✅ Successfully removed {dest_path}")
        return True
    except Exception as e:
        print(f"  ❌ Error removing {skill_name}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Unified Skills Manager for Open Code and Antigravity.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Install all skills to Open Code
  %(prog)s install --all --target opencode
  
  # Install a specific skill to Antigravity (global)
  %(prog)s install git-formatter --target antigravity
  
  # Install to Antigravity workspace
  %(prog)s install git-formatter --target antigravity --scope workspace
  
  # List installed skills
  %(prog)s list --target opencode
  %(prog)s list --target antigravity --scope workspace
        """
    )
    
    parser.add_argument(
        "--target", 
        choices=["opencode", "antigravity"], 
        required=True,
        help="Target AI assistant (opencode or antigravity)"
    )
    parser.add_argument(
        "--scope", 
        choices=["global", "workspace"], 
        default="global",
        help="Scope for Antigravity installation (ignored for Open Code)"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Install Command
    install_parser = subparsers.add_parser("install", help="Install or update skills")
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

    # Validate scope for opencode
    if args.target == "opencode" and args.scope == "workspace":
        print("Warning: Open Code does not support workspace scope. Using global scope.")
        args.scope = "global"

    source_root = get_source_skills_dir()
    dest_root = get_dest_skills_dir(args.target, args.scope)

    print("=" * 60)
    print(f"Target:      {args.target.upper()}")
    print(f"Source:      {source_root}")
    print(f"Destination: {dest_root}")
    if args.target == "antigravity":
        print(f"Scope:       {args.scope.upper()}")
    print("=" * 60)

    if args.command == "list":
        list_installed_skills(dest_root)
        
    elif args.command == "install":
        if not args.skill and not args.all:
            print("Error: Please specify a skill name or use --all")
            sys.exit(1)
            
        if args.all:
            # Exclude installer directories
            skills_to_install = [
                d.name for d in source_root.iterdir() 
                if d.is_dir() 
                and not d.name.startswith(".") 
                and d.name not in ["skills-manager", "antigravity-installer", "opencode-installer"]
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
        print("=" * 60)
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
        print("=" * 60)
        print(f"Done. Removed {success_count}/{len(skills_to_remove)} skills.")

if __name__ == "__main__":
    main()
