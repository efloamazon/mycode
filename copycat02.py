#!/usr/bin/env python3

import shutil
import os


os.chdir("/home/student/mycode/")

shutil.copy("5g_research02/sdn_network02.txt", "5g_research/sdn_network.txt.copy")

shutil.copytree("5g_research02/", "5g_research_backup/")


