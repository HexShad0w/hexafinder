# Hexafinder

**Hexafinder** is a simple yet powerful tool for automated subdomain enumeration. By integrating **Subfinder**, **Httpx**, **Katana**, and **grep**, **Hexafinder** enables users to discover subdomains, scan for live hosts, and sort results—all in one streamlined tool.

## Features

- **Automated Subdomain Discovery**: Utilizes **Subfinder** to find subdomains quickly and efficiently.
- **Live Host Scanning**: Leverages **Httpx** to check for live hosts among discovered subdomains.
- **Advanced Filtering**: Incorporates **Katana** for comprehensive filtering of results based on various criteria.
- **Custom Sorting**: Uses **grep** for advanced sorting of output to meet user preferences.
- **Full Automation**: Facilitates an efficient workflow for subdomain enumeration without manual intervention.

## Installation

To use **Hexafinder**, you need to install the following tools:

1. **Subfinder**: Follow the instructions on the [Subfinder GitHub page](https://github.com/projectdiscovery/subfinder) to install it.
2. **Httpx**: You can find the installation instructions for **Httpx** on its [GitHub page](https://github.com/projectdiscovery/httpx).
3. **Katana**: Install **Katana** as described in its [GitHub repository](https://github.com/projectdiscovery/katana).
4. **Grep**: Ensure **grep** is installed on your system (it’s typically included in most Unix/Linux distributions).

After installing the necessary tools, clone the **Hexafinder** repository:

```bash
git clone https://github.com/yourusername/hexafinder.git
cd hexafinder
