import sys


def sum_numbers(filepath):
    total = 0
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                num = float(line)
                total += num
            except ValueError:
                print(f"Warning: skipping non-numeric line: {line}")
    return total


def main():
    if len(sys.argv) != 2:
        print("Usage: python sum_numbers.py <file>")
        sys.exit(1)
    filepath = sys.argv[1]
    total = sum_numbers(filepath)
    print(f"Sum: {total}")


if __name__ == "__main__":
    main()
