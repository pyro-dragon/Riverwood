label test:
    
    $harf = ChatResourceManager()
    
    $fileContents = "Nothing"
    
    $fileContents = game.getFolderData("resources/names")
    
    $testname = harf.names[10].name
    $testsex = harf.names[10].male
    
    "Name: [testname]\nSex: [testsex]"
    
    #$typeobj = type(fileContents[0]).__name__
    #"Type: [typeobj]"
    
    #if type(fileContents[0]).__name__ == "list": 
    #    "This is an array"
    #elif type(fileContents[0]).__name__ == "dict":
    #    "This is an object"
    #else:
    #    "I have no idea"
    
    # Auto file reading
    python:
        import os
        for fname in os.listdir(config.gamedir + '/resources'):
            #say(None, "File: " + fname);
            #if fname.endswith(('.txt', '.xml', 'json')):

            if fname.endswith("txt"):
                #say(None, "Open " + "resources/" + fname);
                f = open(renpy.loader.transfn("resources/" + fname),"r")
                for line in f:
                    fileContents = line
                f.close()
                #tag = fname[:-4]
                #fname =  'gfx/' + fname
            #renpy.image(tag, fname)

    #"Flat file: [fileContents]"
    
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
        
    #"Flat file: [fileContents]"

    # XML file
    python:
        # import xml related libraries
        import xml.etree.ElementTree as elementtree
        # parse the missions.xml file
        tree = elementtree.parse(renpy.loader.transfn("resources/missions.xml"))
        root = tree.getroot()
        fileContents = root.text
        
    #"XML file: [fileContents]"

    # Load JSON file?
    python:
        import json
        json_data=open(renpy.loader.transfn("resources/missions.json")).read()
        data = json.loads(json_data)
        fileContents = data["missions"]
            
    #"JSON file: [fileContents]"
    
    "END OF TEST"
 