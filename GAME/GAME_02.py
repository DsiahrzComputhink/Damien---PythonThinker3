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

# Exploit types
exploits = {
    "sshcrack": "SSH Cracking",
    "ftpbounce": "FTP Bounce Exploit",
    "sqlinject": "SQL Injection",
    "proxybypass": "Proxy Bypass",
    "smtpoverflow": "SMTP Overflow",
    "webexploit": "Web Server Exploit"
}

# Active session
network = {}
hacked_nodes = []
trace_active = False

def generate_random_ip():
    return f"192.168.{random.randint(1, 50)}.{random.randint(1, 255)}"

def generate_random_name():
    prefixes = ["Workstation", "Server", "Router", "Firewall", "Database"]
    suffixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
    return f"{random.choice(prefixes)}-{random.choice(suffixes)}"

def scan():
    print(f"{style.byellow}🔍 Scanning for nearby devices...{style.RESET}")
    time.sleep(1.5)
    
    found_ips = []
    for _ in range(random.randint(2, 5)):
        ip = generate_random_ip()
        if ip not in network:
            name = generate_random_name()
            vulnerabilities = random.sample(list(exploits.keys()), random.randint(1, 3))
            network[ip] = {"name": name, "vulnerabilities": vulnerabilities}
            found_ips.append(ip)

    if found_ips:
        print(f"{style.bgreen}✅ Found {len(found_ips)} new devices!{style.RESET}")
        for ip in found_ips:
            print(f"🔗 {style.dcyan}{network[ip]['name']} ({ip}) - Possible Exploits: {', '.join(network[ip]['vulnerabilities'])}{style.RESET}")
    else:
        print(f"{style.dred}⚠ No new devices found.{style.RESET}")

def trace_timer():
    global trace_active
    trace_active = True
    for i in range(90, 0, -1):  # 90 seconds countdown
        print(f"{style.bred}⚠ TRACE IN PROGRESS! Disconnect in {i} seconds!{style.RESET}", end="\r")
        time.sleep(1)
    print(f"\n{style.dred}💀 You've been traced! GAME OVER!{style.RESET}")
    exit()

def exploit(ip, method):
    if ip not in network:
        print(f"{style.bred}❌ Invalid target.{style.RESET}")
        return
    
    if method not in network[ip]["vulnerabilities"]:
        print(f"{style.dred}❌ Exploit failed! {method} is not a valid attack for this target.{style.RESET}")
        return
    
    print(f"{style.byellow}🔓 Launching {exploits[method]} on {network[ip]['name']} ({ip})...{style.RESET}")
    time.sleep(2)
    print(f"{style.bgreen}✅ {network[ip]['name']} ({ip}) hacked successfully using {exploits[method]}!{style.RESET}")
    hacked_nodes.append(ip)
    global trace_active
    trace_active = False

def exploit_all(ip):
    if ip not in network:
        print(f"{style.bred}❌ Invalid target.{style.RESET}")
        return

    print(f"{style.byellow}🔓 Attempting all exploits on {network[ip]['name']} ({ip})...{style.RESET}")
    for method in exploits.keys():
        if method in network[ip]["vulnerabilities"]:
            exploit(ip, method)

def disconnect():
    global trace_active
    print(f"🔌 {style.bblue}Disconnected.{style.RESET}")
    if trace_active:
        trace_active = False
        print(f"🚀 {style.bgreen}You escaped before getting traced!{style.RESET}")

def terminal():
    print(f"{style.bwhite}💻 Welcome to Hacknet-Python! Type 'help' for commands.{style.RESET}")
    while True:
        cmd = input(f"\n{style.bblue}root@hacker:~$ {style.RESET}").strip().lower()

        if cmd == "exit":
            print(f"{style.bred}👋 Shutting down...{style.RESET}")
            break
        elif cmd == "scan":
            scan()
        elif cmd.startswith("exploit "):
            parts = cmd.split(" ")
            if len(parts) == 2:
                exploit_all(parts[1])
            else:
                print(f"{style.dred}❌ Usage: exploit <IP>{style.RESET}")
        elif cmd == "disconnect":
            disconnect()
        elif cmd == "help":
            print(f"{style.bwhite}📜 Commands: {style.RESET}scan, exploit <IP>, disconnect, exit")
            print(f"{style.byellow}Available Exploits: {', '.join(exploits.keys())}{style.RESET}")
        else:
            print(f"{style.bred}❌ Command not found.{style.RESET}")

terminal()