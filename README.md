# Leviathan
Threat Modelling Tool
[by exploitsecurity.io]

<img width="419" alt="leviathan-icon" src="https://github.com/exploitsecurityio/leviathan/assets/131332424/8885e90b-cbf3-47b3-8acb-d7e40efb50d4">

## Description

Leviathan leverages AI and NMAP to conduct a first level parse of your environment. The threat model in use is based on OWASP STRIDE. The utility scans a given host or network range and translates the findings into a highlevel overview of potential threats that may require further examination or scrutiny.

## Usage
```
python3 leviathan.py <host IP Address or Network Range>
```

## Dependencies

- Python3.11
- OPENAI module and a valid API key. More info can be found [here](https://platform.openai.com/docs/api-reference/introduction)
- python3-nmap

## Installation

- Using pip to install required libraries

```
pip3 install -r requirements.txt
```

## Screenshots



## Contact

Web: www.exploitsecurity.io

Email: info@exploitsecurity.io

## Copyright

ExploitToolFinder developed by The Security Team @ [exploitsecurity.io]

This program is freely redistributable under the terms of the GNU General Public License as published by the Free Software Foundation.

It is the intention that this software adds usefulness, however it is not currently covered under WARRANTY.

[GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)
