import os
print("""\033[0;31m

 ██████╗    ██╗  ██╗     █████╗     ███╗   ██╗     ██████╗     ███████╗
██╔════╝    ██║  ██║    ██╔══██╗    ████╗  ██║    ██╔════╝     ██╔════╝
██║         ███████║    ███████║    ██╔██╗ ██║    ██║  ███╗    █████╗  
██║         ██╔══██║    ██╔══██║    ██║╚██╗██║    ██║   ██║    ██╔══╝  
╚██████╗    ██║  ██║    ██║  ██║    ██║ ╚████║    ╚██████╔╝    ███████╗
 ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝     ╚═════╝     ╚══════╝
                                                                       
""")
print("""\033[1;33m 

How will you setup tool?
(write number)

1 - setup with Terminal
2 - setup with Gui (only kali linux! and you will just do the setup with the gui)

""")
def change():
  s = input("\033[0;34m--->")
  
  if s == "1":
    os.system("sudo python /log/setup.py")
  elif s == "2":
    os.system("sudo python /log/setup2.py")
  else:
    change()
