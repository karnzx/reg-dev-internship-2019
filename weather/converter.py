#sorry just relaize internship 2019 yesterday T^T 
import json
import xmltodict
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "\\input.xml", 'r') as f:
    xmlString = f.read()
 
print("XML input (sample.xml):")
print(xmlString)
     
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
 
print("\nJSON output(output.json):")
print(jsonString)
 
with open(dir_path + "\\output.json", 'w') as f:
    f.write(jsonString)