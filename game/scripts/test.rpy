label test:
    
    # Flat file
    python:
        # open the file
        f = open(renpy.loader.transfn("resources/missions.txt"),"r")
        # iterate over its lines and do something with them
        for line in f:
            do_something(line)
        # when finished, close the file
        f.close()

    # XML file
    python:
        # import xml related libraries
        import xml.etree.ElementTree as elementtree
        # parse the missions.xml file
        tree = elementtree.parse(renpy.loader.transfn("resources/missions.xml"))

    # Load JSON file?
    python:
        import json
        with open(renpy.loader.transfn("resources/missions.json") as data_file:    
            data = json.load(data_file)
    
    "END OF TEST"
 