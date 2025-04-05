Pymap:A Simple Network Scanning Tool


Overview
Pymap is a Python-based network scanning tool that combines command-line parameter functionality with an interactive menu.It allows users to perform various network scanning tasks,such as testing connectivity,scanning ports,and detecting operating systems.

How to get started?
   After Cloning,
      pip install -r requirements.txt

Features

1. Command-Line Parameters:

• Users can specify tasks directly through command-line arguments.

• Supports options for connectivity testing,port scanning,OS detection,and executing terminal commands.


2. Interactive Menu:

• After processing command-line parameters,the tool enters an interactive mode.

• Users can choose from a menu to perform tasks interactively.


3. Flexibility:

• Combines the convenience of command-line tools with the ease of use of interactive menus.


How to Use


1.Command-Line Parameters
To use Pymap with command-line parameters,run the script with the appropriate options.Here are some examples:


• Test Connectivity to a Host:

```bash
  python pymap.py -c 192.168.1.1
  ```

This will ping the specified IP address to test connectivity.


• Scan Ports on a Specified IP:

```bash
  python pymap.py -s 192.168.1.1 -p 1-100
  ```

This will scan ports 1 to 100 on the specified IP address.


• Scan Operating System of a Host:

```bash
  python pymap.py -o 192.168.1.1
  ```

This will attempt to detect the operating system of the specified IP address.


• Execute a Terminal Command:

```bash
  python pymap.py -t "ls -l"
  ```

This will execute the specified command in the terminal.


2.Interactive Menu
If no command-line parameters are provided,or after processing the parameters,Pymap will enter an interactive menu.The menu provides the following options:


• 1.Test Connectivity to Host:

• Enter the IP address to test connectivity using the`ping`command.


• 2.Scan Specified IP Address Port:

• Enter the IP address and port range to scan for open ports.


• 3.Scan Operating System:

• Enter the IP address to detect the operating system of the host.


• 4.Free Use at the Current Terminal:

• Enter any terminal command to execute it directly.


• 5.Exit:

• Exit the program.


Example Usage

1. Using Command-Line Parameters:

```bash
   python pymap.py -s 192.168.1.1 -p 80-443
   ```

This will scan ports 80 to 443 on the IP address`192.168.1.1`.


2. Using Interactive Menu:

• Run the script without any parameters:

```bash
     python pymap.py
     ```


• Follow the on-screen menu to choose an option,for example:

```
     What's your choice? (1, 2, 3, 4, 5)
     2
     Enter IP address: 192.168.1.1
     Enter port range (e.g., 80,443 or 1-100): 1-100
     ```



Requirements

• Python 3

• `python-nmap`library(install using`pip install python-nmap`)


Conclusion
Pymap is a versatile tool that combines the power of command-line parameters with the flexibility of an interactive menu.Whether you prefer quick command-line operations or a more interactive approach,Pymap can meet your needs.
