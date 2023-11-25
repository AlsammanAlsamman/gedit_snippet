#!/usr/bin/python

############################################## About Author #########################################
# Created by: Alsamman M. Alsamman                                                                  #
# Emails: smahmoud [at] ageri.sci.eg or A.Alsamman [at] cgiar.org or SammanMohammed [at] gmail.com  #
# License: MIT License - https://opensource.org/licenses/MIT                                        #
# Disclaimer: The script comes with no warranty, use at your own risk                               #
# This script is not intended for commercial use                                                    #
#####################################################################################################

# countwords using python 2.7 in gedit

# Tab Trigger: countwords
# Shortcut Key: Ctrl+Shift+C
# Drop targets: text/plain

#$<
import re
lines = $GEDIT_SELECTED_TEXT
output = ""
total = 0
counts = dict()
for line in lines.splitlines():
    words = re.findall(r'\w+', line)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
# calculate total words
for word in counts:
    total += counts[word]
output += "Total words: %d\n" % total
output += "Word\tCount\tPercent\n"
for word in sorted(counts):
    output += "%s\t%d\t%.2f%%\n" % (word, counts[word], (float(counts[word])/total)*100)
return output
#>