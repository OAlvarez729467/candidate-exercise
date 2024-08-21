import os
import sys
import subprocess


def run_pytest():
    features_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'features'))
    try:
        subprocess.run(['pytest'], cwd=features_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error trying to run pytest: {e}")
        sys.exit(1)


def main():
    run_pytest()


if __name__ == "__main__":
    main()
