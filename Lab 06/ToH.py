def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, helper, source, destination)

# Get user input
n = int(input("Enter the number of disks: "))

# Call the function
tower_of_hanoi(n, 'A', 'B', 'C')
print(f"\nTotal moves: {2**n - 1} (2^{n} - 1)")
