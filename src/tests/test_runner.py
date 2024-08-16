import os
import subprocess
import sys


def clean_reports():
    """Clears previous reports."""
    if os.path.exists("reports"):
        for file in os.listdir("reports"):
            file_path = os.path.join("reports", file)
            if os.path.isfile(file_path):
                os.unlink(file_path)


def run_behave_tests():
    """Execute the tests of `behave`."""
    print("Running tests of `behave`...")
    result = subprocess.run(['behave', '--tags=-wip'], check=True)
    return result.returncode


def run_pytest_tests():
    """Execute the tests of `pytest`."""
    print("Running tests of `pytest`...")
    result = subprocess.run(['pytest', '--cov=utils', '--cov-report=term-missing'], check=True)
    return result.returncode


def main():
    clean_reports()
    try:
        behave_returncode = run_behave_tests()
        pytest_returncode = run_pytest_tests()

        if behave_returncode == 0 and pytest_returncode == 0:
            print("All tests passed successfully!")
            sys.exit(0)
        else:
            print("Some tests failed.")
            sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"Error running the tests: {e}")
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
