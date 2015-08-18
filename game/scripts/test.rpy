label test:
    
    $fileContents = "Nothing"
    
    # Flat file
    python:
        # open the file
        f = open(renpy.loader.transfn("resources/missions.txt"),"r")
        # iterate over its lines and do something with them
        for line in f:
            #do_something(line)
            fileContents = line
        # when finished, close the file
        f.close()
        
    "Flat file: [fileContents]"

    # XML file
    python:
        # import xml related libraries
        import xml.etree.ElementTree as elementtree
        # parse the missions.xml file
        tree = elementtree.parse(renpy.loader.transfn("resources/missions.xml"))
        root = tree.getroot()
        fileContents = root.text
        
    "XML file: [fileContents]"

    # Load JSON file?
    python:
        import json
        json_data=open(renpy.loader.transfn("resources/missions.json")).read()
        data = json.loads(json_data)
        fileContents = data["missions"]
            
    "JSON file: [fileContents]"
    
    "END OF TEST"
 