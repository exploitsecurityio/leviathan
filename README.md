# Leviathan
Threat Modelling Tool
[by exploitsecurity.io]

<img width="419" alt="leviathan-icon" src="https://github.com/exploitsecurityio/leviathan/assets/131332424/8885e90b-cbf3-47b3-8acb-d7e40efb50d4">

## Description

Leviathan leverages OpenAI and NMAP to conduct a first level parse of your environment. A basic threat model is formulated using the OWASP STRIDE framework. The Leviathan utility scans a given host or network range and translates the findings into a highlevel overview of potential threats that call for further examination or scrutiny. The WebUI is then presented to the user, which allows for a highlevel overview of potential threats within the environment.

NEXT STEP: Applying a quantifiable lens, the next step would be a penetration test to help solidify the results and to provide mitigations where necessary.

## Usage
```
python3 leviathan.py <host IP Address or Network Range>
```

## Dependencies

- Python3.11
- OPENAI module and a valid API key. More info can be found [here](https://platform.openai.com/docs/api-reference/introduction)
- python3-nmap
- NODEJS
- NPM

## Manual Installation

- Clone the GIT hub repository

```
git clone https://github.com/exploitsecurityio/leviathan.git
```

- Clone the python-nmap3 repo

```
git clone https://github.com/nmmapper/python3-nmap.git
```

- Run Python VENV
```
python -m venv venv
source venv/bin/activate
```

- Using pip to install required libraries

```
pip install -r requirements.txt
```

- Install openai
```
pip install openai
```

- Install python3-nmap
```
pip install python3-nmap
```

- NODEJS Installation
```
apt-get install nodejs
```

- NPM Installation
  
```
npm init -y
npm install express
```

- Install CORS Module

```
npm install cors --save
```

- Install html2pdf Module

```
npm install --save html2pdf.js
```

- Server will run on http://localhost:3000

## Screenshots

<img width="813" alt="image" src="https://github.com/exploitsecurityio/leviathan/assets/131332424/064faaeb-6efb-4e2d-8bba-2191aa7b96d0">

<img width="1512" alt="image" src="https://github.com/exploitsecurityio/leviathan/assets/131332424/b4d7b5c6-8500-40d8-b130-00930fb746d7">

## Contact

Web: www.exploitsecurity.io

Email: info@exploitsecurity.io

## Copyright

Leviathan was developed by The Security Team @ [exploitsecurity.io]

This program is freely redistributable under the terms of the GNU General Public License as published by the Free Software Foundation.

It is the intention that this software adds usefulness, however it is not currently covered under WARRANTY.

[GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)
