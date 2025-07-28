import subprocess
import sys
import os

def run_script(script_path):
    script_path = os.path.normpath(script_path)
    
    print(f"\n{'='*20}")
    print(f"Executing: python {script_path}")
    print(f"{'='*20}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            check=True,
            capture_output=True,
            text=True
        )
        print("Success!")
        print("Output:")
        print(result.stdout)
        if result.stderr:
            print("Stderr:")
            print(result.stderr)
    except FileNotFoundError:
        print(f"ERROR: Script not found at '{script_path}'")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Script '{script_path}' failed with exit code {e.returncode}")
        print("Stdout:")
        print(e.stdout)
        print("Stderr:")
        print(e.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while running '{script_path}': {e}")
        sys.exit(1)

def main():
    """Main function to run the entire Screencoder workflow."""
    print("Starting the Screencoder full workflow...")

    # --- Part 1: Initial Generation with Placeholders ---
    print("\n--- Part 1: Initial Generation with Placeholders ---")
    run_script("block_parsor.py")
    run_script("html_generator.py")

    # --- Part 2: Final HTML Code Generation ---
    print("\n--- Part 2: Final HTML Code Generation ---")
    run_script("image_box_detection.py")
    run_script("UIED/run_single.py")
    run_script("mapping.py")
    run_script("image_replacer.py")

    print("\nScreencoder workflow completed successfully!")

if __name__ == "__main__":
    main()