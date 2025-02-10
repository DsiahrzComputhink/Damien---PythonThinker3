import time
import random
import threading

# Network structure: IP -> { name, security level, password }
network = {
    "192.168.1.10": {"name": "Local Server", "security": "low", "password": "pass123"},
    "192.168.1.20": {"name": "Bank Server", "security": "high", "password": "securepass"},
    "192.168.1.30": {"name": "Government Database", "security": "critical", "password": "topsecret"},
}

# Active session
player_money = 0
hacked_nodes = []

# Fake Mission
missions = [
    {"target": "192.168.1.10", "objective": "Steal file", "reward": 100},
    {"target": "192.168.1.20", "objective": "Wipe logs", "reward": 300}
]

# Tracing System
trace_active = False

def trace_timer():
    """Starts a trace countdown (10s)."""
    global trace_active
    trace_active = True
    for i in range(10, 0, -1):
        print(f"⚠ TRACE IN PROGRESS! Disconnect in {i} seconds!", end="\r")
        time.sleep(1)
    print("\n💀 You've been traced! GAME OVER!")
    exit()

def scan_network():
    """Scans the network for hackable systems."""
    print("\n🔍 Scanning for active systems...")
    for ip, data in network.items():
        print(f"📡 {ip} [{data['security'].capitalize()} Security] - {data['name']}")
    print("💡 Use 'connect <IP>' to access a system.")

def connect(ip):
    """Connects to a system and starts hacking."""
    if ip in network:
        print(f"🔌 Connected to {ip} - {network[ip]['name']}")
        print("💡 Use 'bruteforce' to hack the system.")
    else:
        print("❌ Invalid IP.")

def brute_force(ip):
    """Tries to hack a system using brute force."""
    if ip not in network:
        print("❌ Invalid target.")
        return

    print("🔓 Starting brute force attack...")
    attempts = 0
    security = network[ip]["security"]

    # Simulate difficulty levels
    max_attempts = {"low": 5, "high": 10, "critical": 15}[security]

    # Start trace timer if security is high or critical
    if security in ["high", "critical"]:
        threading.Thread(target=trace_timer, daemon=True).start()

    while attempts < max_attempts:
        guess = f"pass{random.randint(100,999)}"
        print(f"🔑 Trying {guess}...")
        time.sleep(0.5)

        if guess == network[ip]["password"]:
            print(f"✅ SUCCESS! You hacked {ip} - {network[ip]['name']}")
            hacked_nodes.append(ip)
            global trace_active
            trace_active = False  # Cancel tracing if hacked in time
            return

        attempts += 1

    print("❌ Brute force failed.")

def disconnect():
    """Disconnects from the system and stops tracing."""
    global trace_active
    print("🔌 Disconnected.")
    if trace_active:
        trace_active = False
        print("🚀 You escaped before getting traced!")

def check_missions():
    """Checks available missions."""
    print("\n📜 Active Missions:")
    for mission in missions:
        status = "✔ Completed" if mission["target"] in hacked_nodes else "❌ Pending"
        print(f"- Hack {mission['target']} to {mission['objective']} (${mission['reward']}) [{status}]")

def claim_rewards():
    """Claims rewards for completed missions."""
    global player_money
    earned = 0
    for mission in missions:
        if mission["target"] in hacked_nodes and "claimed" not in mission:
            player_money += mission["reward"]
            earned += mission["reward"]
            mission["claimed"] = True

    if earned > 0:
        print(f"💰 You earned ${earned}! Total Balance: ${player_money}")
    else:
        print("❌ No rewards available.")

# Fake terminal loop
def terminal():
    print("💻 Welcome to Hacknet-Python! Type 'help' for commands.")
    while True:
        cmd = input("\nroot@hacker:~$ ").strip().lower()

        if cmd == "exit":
            print("👋 Shutting down...")
            break
        elif cmd == "scan":
            scan_network()
        elif cmd.startswith("connect "):
            connect(cmd.split(" ")[1])
        elif cmd.startswith("bruteforce "):
            brute_force(cmd.split(" ")[1])
        elif cmd == "disconnect":
            disconnect()
        elif cmd == "missions":
            check_missions()
        elif cmd == "claim":
            claim_rewards()
        elif cmd == "help":
            print("Commands: scan, connect <IP>, bruteforce <IP>, disconnect, missions, claim, exit")
        else:
            print("Command not found.")

terminal()
