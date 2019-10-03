#Missing_Residues.py
#Author: Punit Sundar
#Last Updated: Sep. 30, 2019
#Purpose: Program outputs the missing residues in the G chain of
#         the 2r6g sequence given a .txt file


filename = input("What's the filename of your 2r6g text file?: ")

my_file = open(filename, 'r')
file_contents = my_file.readlines()  #Turns each line in the file into
                                     #a list

atom_file = open("without_anisou_full.txt",'w')  #This file will only
                                                 #contain ATOM lines

count = 0
for i in file_contents:
    count += 1
    if i.startswith("ATOM") and file_contents[count-1][13:16] == 'CA '\
    and file_contents[count-1][21]== 'G':
        atom_file.write(i)  #In the atom only file, program will write
                            #only the lines with 'ATOM', 'CA', and chain
                            #'G' in them

atom_file.close()

atom_only_file = open("without_anisou_full.txt", 'r')
atom_contents = atom_only_file.readlines()  #Turns each line in the file
                                            #into a list

residue_number_list = []  #Empty list that will store all residue
                          #numbers that are present in the atom file
count = 0
for i in atom_contents:
    count += 1
    residue_number_list.append(int(atom_contents[count-1][23:27]))
    #Added each residue number into the list
    
max_residue_number = max(residue_number_list)  #296 is the max

for i in range(1,max_residue_number+1): # #'s from 0 to the max residue #
    if i not in residue_number_list: #Sees if each # from 1 to 296 is in
        print(i)                     #our list

end_message = 'Your file with only CA Atoms in chain G will be found in'
print(end_message, '"without_anisou_full.txt"')

atom_only_file.close() 

my_file.close()

