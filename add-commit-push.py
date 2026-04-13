print("Add-Commit-Push-with-Python")
import subprocess
import sys

def run_command(command):
    result = os.system(command)
    if result != 0:
        print(f"Error running command: {command}")
        sys.exit(1)


message = " "
if "-m" in sys.argv:
        messageIndex = sys.argv.index("-m") + 1
        if messageIndex < len(sys.argv):
            message = sys.argv[messageIndex]
        else:
            print("Error: No commit message provided after -m flag.")
            sys.exit(1)

print("git status:")
subprocess.run(["git", "status"])

confirm = input ("add, commit and push? (y/n):")
if confirm.lower() == "y":
        print("git add .")
        subprocess.run(["git", "add", "."])
        print("git commit")
        subprocess.run(["git", "commit", "-m", message])
        print("git push")
        subprocess.run(["git", "push"])
        print("Roger Roger")
        
if confirm.lower() != "y":
        print("Negative Ghost Rider")
        sys.exit(0) 

if "-f" in sys.argv:
        print("May the Force be with you!")
        subprocess.run(["git", "push", "--force"])