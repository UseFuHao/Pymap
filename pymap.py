import nmap
import argparse
import os


parser = argparse.ArgumentParser(description="Pymap - A simple network scanning tool")
parser.add_argument("-c", "--connectivity", help="Test connectivity to a host", metavar="IP")
parser.add_argument("-s", "--scan", help="Scan specified IP address for open ports", metavar="IP")
parser.add_argument("-p", "--ports", help="Specify port range to scan (e.g., 80,443 or 1-100)", metavar="PORTS")
parser.add_argument("-o", "--os", help="Scan operating system of the specified IP", metavar="IP")
parser.add_argument("-t", "--terminal", help="Free use at the current terminal", metavar="COMMAND")


args = parser.parse_args()

print("Welcome to Pymap")


if args.connectivity:
    print(f"Testing connectivity to {args.connectivity}")
    try:
        os.system(f"ping -c 4 {args.connectivity}")
    except Exception as e:
        print(f"Error: {e}")

elif args.scan and args.ports:
    scanner = nmap.PortScanner()
    print(f"Scanning {args.scan} on ports {args.ports}")
    scanner.scan(args.scan, args.ports)
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for proto in scanner[host].all_protocols():
            print(f"  Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"    Port: {port}\tState: {scanner[host][proto][port]['state']}")

elif args.os:
    scanner = nmap.PortScanner()
    print(f"Scanning OS of {args.os}")
    scanner.scan(args.os, arguments="-O")
    for host in scanner.all_hosts():
        if 'osclass' in scanner[host]:
            for osclass in scanner[host]['osclass']:
                print('OSClass.type:', osclass['type'])
                print('OSClass.vendor:', osclass['vendor'])
                print('OSClass.osfamily:', osclass['osfamily'])
                print('OSClass.osgen:', osclass['osgen'])
                print('OSClass.accuracy:', osclass['accuracy'])
        else:
            print("No OS information found")

elif args.terminal:
    print(f"Executing command: {args.terminal}")
    try:
        os.system(args.terminal)
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\nYou have the following options:")
    print("1. Test connectivity to host")
    print("2. Scan specified IP address port")
    print("3. Scan operating system")
    print("4. Free use at the current terminal")
    print("5. Exit")

    choice = input("\033[32mWhat's your choice? (1, 2, 3, 4, 5) \033[0m")

    if choice == "1":
        ip = input("\033[32mEnter IP address: \033[0m")
        try:
            os.system(f"ping -c 4 {ip}")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":
        scanip = input("Enter IP address: ")
        scanport = input("Enter port range (e.g., 80,443 or 1-100): ")
        scanner = nmap.PortScanner()
        scanner.scan(scanip, scanport)
        for host in scanner.all_hosts():
            print(f"Host: {host}")
            for proto in scanner[host].all_protocols():
                print(f"  Protocol: {proto}")
                ports = scanner[host][proto].keys()
                for port in ports:
                    print(f"    Port: {port}\tState: {scanner[host][proto][port]['state']}")

    elif choice == "3":
        scanos_ip = input("Enter IP address: ")
        scanner = nmap.PortScanner()
        scanner.scan(scanos_ip, arguments="-O")
        for host in scanner.all_hosts():
            if 'osclass' in scanner[host]:
                for osclass in scanner[host]['osclass']:
                    print('OSClass.type:', osclass['type'])
                    print('OSClass.vendor:', osclass['vendor'])
                    print('OSClass.osfamily:', osclass['osfamily'])
                    print('OSClass.osgen:', osclass['osgen'])
                    print('OSClass.accuracy:', osclass['accuracy'])
            else:
                print("No OS information found")

    elif choice == "4":
        terminal_command = input("Enter command: ")
        try:
            os.system(terminal_command)
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "5":
        print("Exiting Pymap. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

"""

This is my first tool.

I hope you like it.

Although its functions are not so good and comprehensive.

But I still want to share.



"""
