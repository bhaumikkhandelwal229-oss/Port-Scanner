⚠️ Python Port Scanner 🚀
A lightweight and efficient TCP Port Scanner built with Python. This tool helps identify open ports on a target IP address or domain, making it a great utility for network diagnostics and learning cybersecurity basics.

🛠️ Features
User-Friendly: Simple CLI interface to enter target and port range.

Fast Scanning: Uses Python's socket library for quick connection attempts.

Accurate Results: Identifies open ports by checking successful TCP handshakes.

Custom Range: Scan any range of ports (e.g., 1 to 1024).

🧰 Tech Stack
Language: Python 3.x

Modules: * socket: For network connections.

datetime: To track the duration of the scan.

🚀 How to Run
Prerequisites
Make sure you have Python installed on your system.

Steps
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/python-port-scanner.git
Navigate to the folder:

Bash
cd python-port-scanner
Run the script:

Bash
python p.py
📖 Usage
When you run the script, follow these steps:

Enter the Target IP/Domain (e.g., 127.0.0.1 or google.com).

Enter the Starting Port (e.g., 1).

Enter the Ending Port (e.g., 100).

Wait for the scan to finish. The tool will list all Open Ports found.

🛑 Disclaimer
This tool is for educational purposes only. Do not use it to scan networks or devices without explicit permission. The author is not responsible for any misuse.
