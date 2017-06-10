import json
import urllib

while True:
    # Get input URL
    url = raw_input("Enter URL: ")
    # Check valid input
    if len(url) < 1:
        break

    # Get data
    print("Retrieving", url)
    connection = urllib.urlopen(url)
    data = connection.read()
    print("Retrieved", len(data), "characters")

    # Parse and deserialize
    try:
        js = json.loads(str(data))
    except:
        js = None
    
    print(json.dumps(js, indent=4))

    comments = js["comments"]

    result = 0

    for comment in comments:
        result += comment["count"]

    print("\n")
    print("Result = {}".format(result))