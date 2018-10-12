
import requests, webbrowser

#this function writes the search strings to an html document

def write_to_file(list, terms):
    outfile = open(terms, "w")
    outfile.write('Here are Links to the Major 6 U.S. News Services, for your topics.')
    outfile.write('<br><br>')
    for elem in list:
        wrtstr= '<a href = ' + elem + '>' + elem + '</a> \n <br>'
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
    serchn = "RealNews_" + srchlst[0] + srchlst[1] + ".html"
    serclst = []
    serclst.append("https://www.google.com/search?&as_sitesearch=nbc.com&as_q=" + srchlst[0] + "%2C+" + srchlst[1])
    serclst.append("https://www.google.com/search?&as_sitesearch=abc.com&as_q=" + srchlst[0] + "%2C+" + srchlst[1])
    serclst.append("https://www.google.com/search?&as_sitesearch=cbs.com&as_q=" + srchlst[0] + "%2C+" + srchlst[1])
    serclst.append("https://www.google.com/search?&as_sitesearch=msnbc.com&as_q=" + srchlst[0] + "%2C+" + srchlst[1])
    serclst.append("https://www.google.com/search?&as_sitesearch=foxnews.com&as_q=" + srchlst[0] + "%2C+" + srchlst[1])
    serclst.append("https://www.google.com/search?&as_sitesearch=cnn.com&as_q=" + srchlst[0] + "%2C+" + srchlst[1])
    write_to_file(serclst, serchn)


## THE GHOST OF THE SHADOW ##

if __name__ == "__main__":
   main()


