#!/usr/bin/env python3
"""
IP Information Tool - Get your IP addresses in a clean way
Usage: python3 ip_info.py
"""

import subprocess
import re
import socket

def get_ip_info():
    """Get IP information from ip a command"""
    
    print("\n" + "="*50)
    print(" IP INFORMATION TOOL v1.0")
    print("="*50 + "\n")
    
    # Run ip a command
    try:
        result = subprocess.run(['ip', 'a'], capture_output=True, text=True)
        output = result.stdout
    except FileNotFoundError:
        print("[!] This script is for Linux/WSL only")
        return
    
    # Find all IPv4 addresses
    ipv4_pattern = r'inet (\d+\.\d+\.\d+\.\d+)/\d+'
    ipv4_addresses = re.findall(ipv4_pattern, output)
    
    # Find all interfaces
    interface_pattern = r'\d+: (\w+):'
    interfaces = re.findall(interface_pattern, output)
    
    # Get hostname
    hostname = socket.gethostname()
    
    # Display results
    print(f"[+] Hostname: {hostname}\n")
    
    print("[+] Network Interfaces:")
    print("-" * 30)
    
    for iface in interfaces:
        if iface != 'lo':  # Skip loopback
            print(f"  • {iface}")
    
    print("\n[+] IP Addresses:")
    print("-" * 30)
    
    for ip in ipv4_addresses:
        if ip != '127.0.0.1':  # Skip localhost
            print(f"  • {ip}")
    
    # Show loopback as well
    if '127.0.0.1' in ipv4_addresses:
        print(f"  • 127.0.0.1 (localhost)")
    
    print("\n" + "="*50)
    print(" Done!")
    print("="*50 + "\n")

if __name__ == "__main__":
    get_ip_info()
