#!/usr/bin/python

############################################## About Author #########################################
# Created by: Alsamman M. Alsamman                                                                  #
# Emails: smahmoud [at] ageri.sci.eg or A.Alsamman [at] cgiar.org or SammanMohammed [at] gmail.com  #
# License: MIT License - https://opensource.org/licenses/MIT                                        #
# Disclaimer: The script comes with no warranty, use at your own risk                               #
# This script is not intended for commercial use                                                    #
#####################################################################################################

# countwords using python 2.7 in gedit

# Tab Trigger: removeDuplicates
# Shortcut Key: Ctrl+Shift+D
# Drop targets: text/plain

# $<
import re
lines = $GEDIT_SELECTED_TEXT
output = ""
duplicatesCount = 0
counts = dict()
for line in lines.splitlines():
    if line in counts:
        counts[line] += 1
        duplicatesCount += 1
    else:
        counts[line] = 1
output += "Duplicates: " + str(duplicatesCount) + "\n"
uniqueCount = 0
for line in counts:
    if counts[line] == 1:
        uniqueCount += 1
output += "Unique: " + str(uniqueCount) + "\n"
for line in counts:
    output += line + "\n"
return output
# >