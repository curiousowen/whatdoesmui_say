# whatdoesmui_say
The MUI Cache stores metadata about recently used files and applications, which can be invaluable during forensic investigations. This tool reads the MUI Cache entries from the Windows Registry and saves the extracted information to a CSV file for easy analysis.
Requirements

Python 3.x
Windows operating system

Installation

Ensure you have Python installed on your system. You can download it from python.org.

Clone this repository or download the script file directly.

Usage

Open a command prompt as Administrator: This ensures you have the necessary permissions to read all registry entries.

Navigate to the directory containing the script:

      cd path\to\your\script

Run the script:

      python whatdoesmuisay.py

The script will read the MUI Cache entries and save the data to mui_cache.csv in the same directory.

How This Tool Helps Analysts

Forensic Investigations

Track User Activity: The Tool can help analysts understand which applications and files were accessed recently by a user, providing a timeline of activity.
Identify Suspicious Files: By analyzing the cache, analysts can spot unusual or suspicious files and applications that may indicate malicious activity.
Support Incident Response: During incident response, quickly accessing and exporting MUI Cache data helps in creating a comprehensive report of user actions.




