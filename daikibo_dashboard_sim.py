import random
statuses = ["Healthy", "Warning", "Critical"]

factories = {
    "Factory A": ["Machine 1", "Machine 2", "Machine 3"],
    "Factory B": ["Machine 1", "Machine 2", "Machine 3"],
    "Factory C": ["Machine 1", "Machine 2", "Machine 3"],
    "Factory D": ["Machine 1", "Machine 2", "Machine 3"]
}

def show_status():
    print("\n Machine Health Status:\n")
    for factory, machines in factories.items():
        print(f" {factory}")
        for machine in machines:
            status = random.choice(statuses)
            print(f"   {machine}: {status}")
        print()

print("Welcome to Daikibo's Machine Health Dashboard")
show_status()
