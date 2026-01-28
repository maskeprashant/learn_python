import sys

def main():
    if len(sys.argv)<3:
        print("Please enter name and age.")
        print("Usage: Assessment.py <name> <age>")
        sys.exit(1)
    
    name = sys.argv[1]
    age = int(sys.argv[2])
    print(f"Hello {name}, aged {age}, Welcome to Python L1.")

main()
