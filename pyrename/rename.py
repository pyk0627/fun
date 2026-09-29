from pathlib import Path
def main():
    test_dir=Path("./test_files")

    if test_dir.exists():
        print("success find folder")
        print(f"files of folder:{list(test_dir.iterdir())}")
    else:
        print("failed to find folder")

if __name__ == "__main__":
    main()
