import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('path/to/xml/file.xml')

# Get the root element of the XML tree
root = tree.getroot()

# Define a dictionary to store the extracted data
data = {}

# Loop through the XML tree and extract the desired data
for item in root.iter('item'):
    title = item.find('title').text
    link = item.find('link').text
    pubDate = item.find('pubDate').text
    description = item.find('description').text

    # Add the extracted data to the dictionary
    data[title] = {'link': link, 'pubDate': pubDate, 'description': description}

# Print the extracted data
print(data)
