
import requests, webbrowser

#this function writes the search strings to an html document

def write_to_file(list, terms, networks, sterms):
    outfile = open(terms, "w")
    outfile.write('Here are Links to the Major 6 U.S. News Services, in no particular order.<br>')
    outfile.write('The links will lead you to recent searches for your search terms, ' + sterms + ', at the selected network.')
    outfile.write('<br><br>')
    for num2 in range(len(list)):
        wrtstr= '<a href = ' + list[num2] + '>' + networks[num2] + '</a> \n <br>'
        outfile.write(wrtstr)
    outfile.close()
    webbrowser.open('file:///C:/Users/mysti/thomasoriginalcode/Git/RealNews/' + terms)

#this is the main function. It retrieves and processes the necessary input

def main():
    print("")
    print("This program allows you to enter up to two search terms.")
    print("It then retrieves links to topical searches from the major 6 U.S. News Networks.")
    print("The author of the code has no affiliation with any of these networks, and is not trying to advance a particular perspective.")
    print("The purpose of the program is to help users to get accurate news, avoiding 'Fake News' sites.")
    print("")
    srchlst = []
    for elem in range(2):
        addr = input("Please enter a search term: ")
        srchlst.append(addr)
        print("")
    sterms = srchlst[0] + " and " + srchlst[1]
    serchn = "RealNews_" + srchlst[0] + srchlst[1] + ".html"
    netwrk = ['abc', 'cbs', 'nbc', 'msnbc', 'foxnews', 'cnn']
    serclst = []
    for num1 in range(6):
        serclst.append("https://www.google.com/search?&as_sitesearch=" + netwrk[num1] + ".com&as_q=" + srchlst[0] + "%2C+" + srchlst[1])
    print("A webpage will now open in your browser with the links you requested.") 
    write_to_file(serclst, serchn, netwrk, sterms)


## THE GHOST OF THE SHADOW ##

if __name__ == "__main__":
   main()


