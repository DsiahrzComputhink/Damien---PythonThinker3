import time
import random
import threading

# Text Styling Class
class style():
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    CANCEL = '\033[9m'
    bgbwhite = '\033[7m'
    black = '\033[8m'
    bgray = '\033[30m'
    dred = '\033[31m'
    dgreen = '\033[32m'
    dyellow = '\033[33m'
    dblue = '\033[34m'
    dpurple = '\033[35m'
    dcyan = '\033[36m'
    dwhite = '\033[37m'
    bgray = '\033[90m'
    bred = '\033[91m'
    bgreen = '\033[92m'
    byellow = '\033[93m'
    bblue = '\033[94m'
    bpurple = '\033[95m'
    bcyan = '\033[96m'
    bwhite = '\033[97m'
    RESET = '\033[0m'

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
        print(f"{style.bred}⚠ TRACE IN PROGRESS! Disconnect in {i} seconds!{style.RESET}", end="\r")
        time.sleep(1)
    print(f"\n{style.dred}💀 You've been traced! GAME OVER!{style.RESET}")
    exit()

def scan_network():
    """Scans the network for hackable systems."""
    print(f"\n{style.byellow}🔍 Scanning for active systems...{style.RESET}")
    for ip, data in network.items():
        sec_color = {"low": style.bgreen, "high": style.byellow, "critical": style.bred}[data["security"]]
        print(f"📡 {ip} [{sec_color}{data['security'].capitalize()} Security{style.RESET}] - {data['name']}")
    print(f"💡 {style.dcyan}Use 'connect <IP>' to access a system.{style.RESET}")

def connect(ip):
    """Connects to a system and starts hacking."""
    if ip in network:
        print(f"🔌 {style.bgreen}Connected to {ip} - {network[ip]['name']}{style.RESET}")
        print(f"💡 {style.dcyan}Use 'bruteforce' to hack the system.{style.RESET}")
    else:
        print(f"{style.bred}Invalid IP.{style.RESET}")

def brute_force(ip):
    """Tries to hack a system using brute force."""
    if ip not in network:
        print(f"{style.bred}Invalid target.{style.RESET}")
        return

    print(f"🔓 {style.byellow}Starting brute force attack...{style.RESET}")
    attempts = 0
    security = network[ip]["security"]

    # Simulate difficulty levels
    max_attempts = {"low": 5, "high": 10, "critical": 15}[security]

    # Start trace timer if security is high or critical
    if security in ["high", "critical"]:
        threading.Thread(target=trace_timer, daemon=True).start()

    while attempts < max_attempts:
        guess = f"pass{random.randint(100,999)}"
        print(f"{style.dcyan}🔑 Trying {guess}...{style.RESET}")
        time.sleep(0.5)

        if guess == network[ip]["password"]:
            print(f"{style.bgreen}SUCCESS! You hacked {ip} - {network[ip]['name']}{style.RESET}")
            hacked_nodes.append(ip)
            global trace_active
            trace_active = False  # Cancel tracing if hacked in time
            return

        attempts += 1

    print(f"{style.bred}Brute force failed.{style.RESET}")

def disconnect():
    """Disconnects from the system and stops tracing."""
    global trace_active
    print(f"🔌 {style.bblue}Disconnected.{style.RESET}")
    if trace_active:
        trace_active = False
        print(f" {style.bgreen}You escaped before getting traced!{style.RESET}")

def check_missions():
    """Checks available missions."""
    print(f"\n{style.byellow}Active Missions:{style.RESET}")
    for mission in missions:
        status = f"{style.bgreen}✔ Completed{style.RESET}" if mission["target"] in hacked_nodes else f"{style.bred}Pendin{style.RESET}"
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
        print(f"💰 {style.bgreen}You earned ${earned}! Total Balance: ${player_money}{style.RESET}")
    else:
        print(f"{style.bred}❌ No rewards available.{style.RESET}")

# Fake terminal loop
def terminal():
    print(f"{style.bwhite}💻 Welcome to Hacknet-Python! Type 'help' for commands.{style.RESET}")
    while True:
        cmd = input(f"\n{style.bblue}root@hacker:~$ {style.RESET}").strip().lower()

        if cmd == "exit":
            print(f"{style.bred}👋 Shutting down...{style.RESET}")
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
            print(f"{style.bwhite}Commands: {style.RESET}scan, connect <IP>, bruteforce <IP>, disconnect, missions, claim, exit")
        else:
            print(f"{style.bred} Command not found.{style.RESET}")

terminal()