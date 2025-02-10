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

# Dictionary of common passwords
common_passwords = ["123456", "password", "qwerty", "abc123", "letmein", "pass123", "securepass", "topsecret"]

# Active session
player_money = 0
hacked_nodes = []
trace_active = False

# Tracing System
def trace_timer():
    """Starts a trace countdown."""
    global trace_active
    trace_active = True
    for i in range(10, 0, -1):
        print(f"{style.bred}⚠ TRACE IN PROGRESS! Disconnect in {i} seconds!{style.RESET}", end="\r")
        time.sleep(1)
    print(f"\n{style.dred}💀 You've been traced! GAME OVER!{style.RESET}")
    exit()

# Brute Force Attack
def brute_force(ip):
    """Tries to hack a system using dictionary attack first, then brute force."""
    if ip not in network:
        print(f"{style.bred}❌ Invalid target.{style.RESET}")
        return

    password_string = network[ip]["password"]
    words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    print(style.bred + "🔓 Starting hack attempt..." + style.RESET)

    # Start trace timer if security is high or critical
    if network[ip]["security"] in ["high", "critical"]:
        threading.Thread(target=trace_timer, daemon=True).start()

    # Step 1: Dictionary Attack
    print(f"{style.byellow}📖 Running Dictionary Attack...{style.RESET}")
    time.sleep(1)
    for common in common_passwords:
        print(f"{style.dcyan}🔑 Trying: {common}...{style.RESET}", end="\r")
        time.sleep(0.5)
        if common == password_string:
            print("\n" + style.bgreen + f"✅ Password Found in Dictionary! → {common}" + style.RESET)
            hacked_nodes.append(ip)
            global trace_active
            trace_active = False  # Stop tracing if hacked in time
            return

    # Step 2: Brute Force Attack (if dictionary fails)
    print("\n" + style.dred + "⚠ Dictionary Attack Failed. Switching to Brute Force..." + style.RESET)

    TIME = 0.2  # Initial delay between guesses
    guessed_password = ""

    for target_index, target_char in enumerate(password_string):
        for attempt in words:
            print(style.dcyan + f"🔑 Trying: {guessed_password + attempt}..." + style.RESET, end="\r")

            time.sleep(TIME)  # Simulate brute force delay
            if TIME > 0.01:
                TIME *= 0.99  # Speed up over time
            elif TIME <= 0.01:
                TIME *= 0.999  # Slow down speed-up rate

            if attempt == target_char:
                guessed_password += attempt
                break  # Move to the next letter

    print("\n" + style.bgreen + f"✅ Password Cracked! → {guessed_password}" + style.RESET)
    hacked_nodes.append(ip)
    trace_active = False  # Stop tracing if hacked in time

# Disconnect
def disconnect():
    """Disconnects from the system and stops tracing."""
    global trace_active
    print(f"🔌 {style.bblue}Disconnected.{style.RESET}")
    if trace_active:
        trace_active = False
        print(f"🚀 {style.bgreen}You escaped before getting traced!{style.RESET}")

# Fake terminal loop
def terminal():
    print(f"{style.bwhite}💻 Welcome to Hacknet-Python! Type 'help' for commands.{style.RESET}")
    while True:
        cmd = input(f"\n{style.bblue}root@hacker:~$ {style.RESET}").strip().lower()

        if cmd == "exit":
            print(f"{style.bred}👋 Shutting down...{style.RESET}")
            break
        elif cmd.startswith("bruteforce "):
            brute_force(cmd.split(" ")[1])
        elif cmd == "disconnect":
            disconnect()
        elif cmd == "help":
            print(f"{style.bwhite}📜 Commands: {style.RESET}bruteforce <IP>, disconnect, exit")
        else:
            print(f"{style.bred}❌ Command not found.{style.RESET}")

terminal()