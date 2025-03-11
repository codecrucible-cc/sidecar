import subprocess
import sys

def main():
    # Try to list available tools in zed
    try:
        result = subprocess.run(['cargo', 'run', '--bin', 'anvil', '--', 'tools', 'list'], 
                              cwd='anvil',
                              capture_output=True,
                              text=True)
        print("Current tools available:")
        print(result.stdout)
        print("\nError output:")
        print(result.stderr)
    except Exception as e:
        print(f"Error running anvil: {e}")

if __name__ == "__main__":
    main()