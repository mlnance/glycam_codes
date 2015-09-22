#!/usr/bin/python

########################################################################
# see glycam.org/docs/forcefield/glycam-naming-2/ for more information #

# this program, the information from the site above to generate a CSV
# file of carbohydrate names for use in Rosetta
########################################################################


import os

# filename preparation
working_dir = os.getcwd() + '/'
filename = working_dir + "full_glycam.codes"
file_header = "Code,Rosetta Code,Default HETNAM,terminal\n"

# one letter code dictionary
# { "one letter GLYCAM code", "Rosetta code" }
one_letter_code_dict = { 'A' : "Ara", 'D' : "Lyx", 'R' : "Rib", 'X' : "Xyl", 'N' : "All", 'E' : "Alt", 'L' : "Gal", 'G' : "Glc", 'K' : "Gul", 'I' : "Ido", 'M' : "Man", 'T' : "Tal", 'C' : "Fru", 'P' : "Psi", 'B' : "Sor", 'J' : "Tag", 'F' : "Fuc", 'Q' : "Qui", 'H' : "Rha", 'O' : "GalA", 'Z' : "GlcA", 'U' : "IdoA", 'V' : "GalNAc", 'Y' : "GlcNAc", 'W' : "ManNAc", 'S' : "NeuNAc" }

default_hetnam = "test"

with open( filename, 'wb' ) as fh:
    # write the file header
    fh.write( file_header )
    
    # cycle through 0-6 (number of open valence positions)
    for open_valence_position in range( 0, 6 + 1 ):
        
        # loop for pyranose, D, alpha sugars
        # example) 1GA
        for key in one_letter_code_dict.keys():
            # create the three-letter GLYCAM code
            GLYCAM_code = str( open_valence_position ) + key + 'A'
            
            # row = GLYCAM code, Rosetta code, default HETNAM
            row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
            fh.write( row )
    fh.write( '\n' )

            
    # cycle through 0-6 (number of open valence positions)
    for open_valence_position in range( 0, 6 + 1 ):
        
        # loop for pyranose, D, beta sugars
        # example) 1GB
        for key in one_letter_code_dict.keys():
            # create the three-letter GLYCAM code
            GLYCAM_code = str( open_valence_position ) + key + 'B'
            
            # row = GLYCAM code, Rosetta code, default HETNAM
            row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
            fh.write( row )
    fh.write( '\n' )


    # cycle through 0-6 (number of open valence positions)
    for open_valence_position in range( 0, 6 + 1 ):
        
        # loop for pyranose, L, alpha sugars
        # example) 1gA
        for key in one_letter_code_dict.keys():
            # create the three-letter GLYCAM code
            GLYCAM_code = str( open_valence_position ) + key.lower() + 'A'
            
            # row = GLYCAM code, Rosetta code, default HETNAM
            row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
            fh.write( row )
    fh.write( '\n' )


    # cycle through 0-6 (number of open valence positions)
    for open_valence_position in range( 0, 6 + 1 ):
        
        # loop for pyranose, L, beta sugars
        # example) 1gB
        for key in one_letter_code_dict.keys():
            # create the three-letter GLYCAM code
            GLYCAM_code = str( open_valence_position ) + key.lower() + 'B'
            
            # row = GLYCAM code, Rosetta code, default HETNAM
            row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
            fh.write( row )
    fh.write( '\n' )


    # cycle through 0-6 (number of open valence positions)
    for open_valence_position in range( 0, 6 + 1 ):
        
        # loop for furanose, D, alpha sugars
        # example) 1Ga
        for key in one_letter_code_dict.keys():
            # create the three-letter GLYCAM code
            GLYCAM_code = str( open_valence_position ) + key + 'a'
            
            # row = GLYCAM code, Rosetta code, default HETNAM
            row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
            fh.write( row )
    fh.write( '\n' )


    # cycle through 0-6 (number of open valence positions)
    for open_valence_position in range( 0, 6 + 1 ):
        
        # loop for furanose, D, beta sugars
        # example) 1Gb
        for key in one_letter_code_dict.keys():
            # create the three-letter GLYCAM code
            GLYCAM_code = str( open_valence_position ) + key + 'b'
            
            # row = GLYCAM code, Rosetta code, default HETNAM
            row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
            fh.write( row )
    fh.write( '\n' )


    # loop for furanose, L, alpha sugars
    # example) 1ga
    for key in one_letter_code_dict.keys():
        # create the three-letter GLYCAM code
        GLYCAM_code = str( open_valence_position ) + key.lower() + 'a'
        
        # row = GLYCAM code, Rosetta code, default HETNAM
        row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
        fh.write( row )
    fh.write( '\n' )


    # cycle through 0-6 (number of open valence positions)
    for open_valence_position in range( 0, 6 + 1 ):
        
        # loop for furanose, L, beta sugars
        # example) 1gb
        for key in one_letter_code_dict.keys():
            # create the three-letter GLYCAM code
            GLYCAM_code = str( open_valence_position ) + key.lower() + 'b'
            
            # row = GLYCAM code, Rosetta code, default HETNAM
            row = GLYCAM_code + ',' + one_letter_code_dict[key] + ',' + default_hetnam + '\n'
            fh.write( row )
    fh.write( '\n' )

