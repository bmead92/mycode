#!/usr/bin/env python3

# imports to work with shutil and os
import shutil
import os

# move into the oworking directory
os.chdir("/home/student/mycode/")

# copy the fileA into fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy folder at source A into path B
shutil.copytree("5g_research/", "5g_research_backup/")

