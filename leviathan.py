import nmap3
import json
from openai import OpenAI
import sys
import os
import subprocess

def scan():
    host = str(sys.argv[1])
    print("[*] Discovery in progress")
    nmap = nmap3.NmapScanTechniques()
    results = nmap.nmap_syn_scan(host, args="-Pn --open")
    return results

def produce_json(results):
    print("[*] Formulating results")
    OPENAI_API_KEY = "<API_KEY>"
    client = OpenAI(api_key=OPENAI_API_KEY)
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
            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.2/html2pdf.bundle.min.js"></script>
        </head>
        <body>
        <div id="content">
            <h1>Leviathan</h1>
            <img src="leviathan-icon.png" style="width:10%;height:10%;"> 
            <h2>[by exploitsecurity.io]</h2>
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
                    <!-- Data will be inserted here by JavaScript -->
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
            </div>
            <br>
            <button id="exportButton">Export to PDF</button>
            <script src="export.js"></script>
        </body>
        </html>
        """
    
    html_file_path = 'leviathan_threat_model.html'
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_content)

def start_npm():
    print ("[*] Server is running on http://localhost:3000")
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
    if len(sys.argv) == 2:
        banner()
        main()
    else:
        print ("Usage: %s <IP or IP Range> " %sys.argv[0])

