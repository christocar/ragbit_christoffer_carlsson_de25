from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data"

if __name__ == '__main__':
    print(DATA_PATH)