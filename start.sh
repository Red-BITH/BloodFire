#!/bin/bash

printf "\033[0;31m"

cat << "EOF"
 ██████╗    ██╗  ██╗     █████╗     ███╗   ██╗     ██████╗     ███████╗
██╔════╝    ██║  ██║    ██╔══██╗    ████╗  ██║    ██╔════╝     ██╔════╝
██║         ███████║    ███████║    ██╔██╗ ██║    ██║  ███╗    █████╗  
██║         ██╔══██║    ██╔══██║    ██║╚██╗██║    ██║   ██║    ██╔══╝  
╚██████╗    ██║  ██║    ██║  ██║    ██║ ╚████║    ╚██████╔╝    ███████╗
 ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝     ╚═════╝     ╚══════╝
                                                                       
EOF

printf "\033[1;33m 

How will you setup tool?
(write number)

1 - setup with Terminal
2 - setup with Gui (only kali linux! and you will just do the setup with the gui)

"

change() {
  read -p "$(printf '\033[0;34m--->')" s
  if [ "$s" == "1" ]; then
    python system/setup.py 
  elif [ "$s" == "2" ]; then
    sudo python system/gui.py
  fi
}

change






