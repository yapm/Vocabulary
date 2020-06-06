# -*-coding: utf8 -*
#Python 3 only

import os
import re
import sys

class Dictionnary:
    """Class defining an object for manipulating a dico for Anki Web app"""
    def __init__(self, origin_file='anki_test.txt'):
        self.original_content = open(origin_file,'r', encoding="utf8")
        self.final_file = open('final_file.txt','w', encoding="utf8")
        self.uncomplete_file = open('uncomplete_file.txt','w', encoding="utf8")
        self.l_final = []
        self.l_uncomplete = []

    def parseOrigin(self):
        """
        Function for parsing the original content
        remove \n character
        replace one or multiple "tab space" by ";" in the final sentence
        """

        for each_line in self.original_content:
            #removes the \n character from the line and adds it to l_origin
            temp_buffer = each_line.replace('\n','')

            #split each line from original list into two different lists
            temp_buffer = re.compile("\t+").split(temp_buffer)

            #join the two elements by a ";space" into a final sentence
            final_sentence = "; ".join(temp_buffer)

            #look if sentence contains ; and include it into final list
            #otherwise send this final sentence to review bcs lack of translation
            if re.search(r";",final_sentence):
                self.l_final.append(final_sentence)
            else:
                self.l_uncomplete.append(final_sentence)


    def writeFinalFile(self):
        """
        Function to write l_final into final file
        """
        for each_line in self.l_final:
            print(each_line,file=self.final_file)

    def writeUncompleteFile(self):
        """
        Function to write uncomplete sentences into uncomplete file
        """
        for each_line in self.l_uncomplete:
            print(each_line,file=self.uncomplete_file)

    def closeFiles(self):
        """
        Function to close all files
        """
        self.original_content.close()
        self.final_file.close()
        self.uncomplete_file.close()


if __name__ == '__main__':
    """Main function to call python patch_anki.py"""
    os.chdir('.')
    try:
        #sys.argv[1] allows to inclue a file as argument
        dico = Dictionnary(sys.argv[1])
    except IndexError :
        dico = Dictionnary()
    except FileNotFoundError:
        print("file not found")
        sys.exit(1)

    dico.parseOrigin()
    dico.writeFinalFile()
    dico.writeUncompleteFile()
    dico.closeFiles()
