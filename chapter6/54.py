import re
import xml.etree.ElementTree as ET

tree = ET.parse('./chapter6/nlp.txt.xml')
root = tree.getroot()

arr = []
counter = 0
for ch1 in root:
    for ch2 in ch1:
        if ch2.tag == 'sentences':
            for ch3 in ch2:
                for ch4 in ch3:
                    if ch4.tag == 'tokens':
                        for ch5 in ch4:
                            t = ''
                            for ch6 in ch5:
                                if ch6.tag == 'word':
                                    t += ch6.text
                                    t += '\t'
                                elif ch6.tag == 'lemma':
                                    t += ch6.text
                                    t += '\t'
                                elif ch6.tag == 'POS':
                                    t += ch6.text
                            arr.append(t)

for i in arr:
    print(i)
