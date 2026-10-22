port = int(input("Port: "))

if port < 0 or port > 65535:
    print("Invalid")
elif port <= 1023:
    print("Well-known")
elif port <= 49151:
    print("Registered")
elif port <= 65535:
    print("Dynamic")