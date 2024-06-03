import nmap3
import json
from openai import OpenAI
import sys
import os

def scan():
    host = str(sys.argv[1])
    print("[*] Discovery in progress")
    nmap = nmap3.NmapScanTechniques()
    results = nmap.nmap_syn_scan(host, args="-Pn --open")
    return results

def produce_json(results):
    print("[*] Formulating results")
    OPENAI_API_KEY = str(sys.argv[2])
    client = OpenAI(api_key=OPENAI_API_KEY)
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "using data from "+str(results)+", formulate a standard stride threat model. Output the results in json format using ONLY use these specific parameter fields 'ipAddress', 'port', 'threatCategory', 'violates' and 'example' and add a comma between open and closed curly brackets",
                    "response_format":"json_object"
                }
            ],
            model="gpt-3.5-turbo",
        )
        response_json = (response.choices[0].message.content)
        json_file_path = 'leviathan_threat_model.json'
        with open(json_file_path, 'w') as json_file:
            json_file.write("["+response_json+"]")
    except:
        print ("[*] PLEASE ENTER A VALID OPENAI API KEY !")
        sys.exit()

def produce_html():
    print ("[*] Creating content")
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Leviathan</title>
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
                .center {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 15%;
                    height: 15%
                }
                .center1 {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 5%;
                    height: 5%
                }
                .topic { 
                    padding: 5px;
                    text-align: center;
                    text-decoration: none;
                    margin-left: auto;
                    margin-right: auto;
                }

            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.2/html2pdf.bundle.min.js"></script>
        </head>
        <body>
        <button id="exportButton">Export to PDF</button>
        <script src="export.js"></script>
        <div id="content">
            <img src="leviathan.png" class="center">
            <br>
            <img src="leviathan-icon.png" class="center"> 
            <br>
            <table>
                <thead>
                    <tr>
                        <th>IP Address</th>
                        <th>Port</th>
                        <th>Threat Category</th>
                        <th>Violates</th>
                        <th>Examples</th>
                    </tr>
                </thead>
                <tbody id="threat-table-body">
                </tbody>
            </table>

            <script>
                fetch('http://localhost:3000/data')
                    .then(response => response.json())
                    .then(data => {
                        const tableBody = document.getElementById('threat-table-body');
                        data.forEach(item => {
                            const row = document.createElement('tr');
                            row.innerHTML = `
                                <td>${item.ipAddress}</td>
                                <td>${item.port}</td>
                                <td>${item.threatCategory}</td>
                                <td>${item.violates}</td>
                                <td>${item.example}</td>
                            `;
                            tableBody.appendChild(row);
                        });
                    })
                    .catch(error => console.error('Error fetching data:', error));
            </script>
            <br>
            <img src="Color logo - no background.png" class="center1">
            <p class="topic">
            <a href="https://www.exploitsecurity.io">www.exploitsecurity.io</a>
            </p>
            </div>
        </body>

        </html>
        """
    
    html_file_path = 'leviathan_threat_model.html'
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_content)

def start_npm():
    print ("[*] Server is running on http://"localhost:3000")
    os.system("node server.js > /dev/null")

def banner():
    if os.name == 'posix':
        clr_cmd = ('clear')
    elif os.name == 'nt':
        clr_cmd = ('cls')
    os.system(clr_cmd)
    print(":::        :::::::::: :::     ::: :::::::::::     ::: ::::::::::: :::    :::     :::     ::::    :::")
    print(":+:        :+:        :+:     :+:     :+:       :+: :+:   :+:     :+:    :+:   :+: :+:   :+:+:   :+:")
    print("+:+        +:+        +:+     +:+     +:+      +:+   +:+  +:+     +:+    +:+  +:+   +:+  :+:+:+  +:+")   
    print("+#+        +#++:++#   +#+     +:+     +#+     +#++:++#++: +#+     +#++:++#++ +#++:++#++: +#+ +:+ +#+")    
    print("+#+        +#+         +#+   +#+      +#+     +#+     +#+ +#+     +#+    +#+ +#+     +#+ +#+  +#+#+#")     
    print("#+#        #+#          #+#+#+#       #+#     #+#     #+# #+#     #+#    #+# #+#     #+# #+#   #+#+#")      
    print("########## ##########     ###     ########### ###     ### ###     ###    ### ###     ### ###    ####")
    print("[by exploitsecurity.io]\n")
    

def main():
    results = scan()
    produce_json(results)
    produce_html()
    start_npm()

if (__name__ == '__main__'):
    if len(sys.argv) == 3:
        banner()
        main()
    else:
        print ("Usage: %s <IP or IP Range> <valid openai api_key>" %sys.argv[0])
