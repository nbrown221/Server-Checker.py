import random 
import csv
servers = [
    "SERVER01",
    "SERVER02",
    "SERVER03",
    "SERVER04"
]
ok = 0
warning = 0
critical = 0


def summary():
    print("-----Summary-----")
    print(f"Total servers: {len(servers)}")
    print(f"There are {ok} oks")
    print(f"There are {warning} warnings ")
    print(f"There are {critical} criticals")
    print()
    return

def check_disk():
    return random.randint(1, 150)
results = []
for server in servers:
    gb  = check_disk()
    print(f"{server} - C: {gb} GB free")
    if gb < 10: 
        critical += 1
        print("STATUS: CRITICAL")
        print()
        results.append({
        "server": server,
        "free_space": gb, 
        "status": "CRITICAL"})
    elif gb < 25:
        warning += 1
        print("STATUS: WARNING")
        print()
        results.append({
        "server": server,
        "free_space": gb, 
        "status": "WARNING"})
    else: 
        ok += 1
        print("STATUS: OK")
        print()
        results.append({
        "server": server,
        "free_space": gb, 
        "status": "OK"})

summary()
for result in results:
    print(f"{result['server']} - {result['free_space']} - {result['status']}")

with open("Server_report.csv", "w", newline="") as file:
    fieldnames = ["server", "free_space", "status"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
    print("\nServer_report.csv created successfully.")