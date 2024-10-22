Hexafinder
Hexafinder is a simple yet powerful tool for automated subdomain enumeration. By integrating Subfinder, Httpx, Katana, and grep, Hexafinder allows users to discover subdomains, scan for live hosts, and sort results—all in one streamlined tool.
Features
Automates subdomain discovery using Subfinder
Live host scanning with Httpx
Advanced filtering of results with Katana
Custom sorting using grep
Full automation for efficient subdomain enumeration
Installation
To use Hexafinder, you need to install the following tools and libraries:
Required Tools
Subfinder:
Install instructions: Subfinder GitHub
bash
go install github.com/subfinder/subfinder/v2/cmd/subfinder@latest

Httpx:
Install instructions: Httpx GitHub
bash
go install github.com/projectdiscovery/httpx/cmd/httpx@latest

Katana:
Install instructions: Katana GitHub
bash
go install github.com/awesome-vulnerabilities/katana@latest

Python Libraries
If you need any additional Python libraries, you can install them using pip. Here are common libraries that might be useful:
bash
pip install subprocess

Usage
Clone the repository:
bash
git clone https://github.com/yourusername/hexafinder.git
cd hexafinder

Run the tool:
bash
python3 hexa.py

Follow the prompts to start the subdomain enumeration process.
