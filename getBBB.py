"""
Version: 1.0.0
Developed by: Ben Breshears (bhbreshears@dmacc.edu)
Scrapes the BBB for businesses with given parameters using lxml and requests libraries

"""
from lxml import html
import requests
def main():
    print("### WARNING: CURRENTLY CAN ONLY BE USED WITH THE FOLLOWING OPTIONS:\n>A LOCATION\n>ACCREDITED FILER\n>JOB TYPE (QUERY)")
    fileName = input("Please enter filename for output files(leave out the ext): ") + '.txt'
    loc = input("Please enter a city: (Ex. Des Moines)")
    loc2 = input("Please enter the state: (Ex. IA)")
    acc = input("Search for accredited businesses only? (y or n) ")
    entity = input("Enter the job title to scrape: ")
    pageNum = input("Enter the page number: ")
    if acc == 'n':
        filter = ""
    else:
        filter ="filter_accredited=1"
    finalLink = ("https://www.bbb.org/search?"+filter+"&find_country=USA&find_loc="+loc+"%2C%20"+loc2+"&find_text="+entity+"&find_type=Category&page="+pageNum+"&sort=Relevance")
    #params = {'filter_accredited' : '1', 'find_country' : 'USA', 'find_loc' : 'Des%20Moines%2C%20IA', 'find_text' : 'Designer', 'page' : '1', 'sort' : 'Relevance' }
    headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    page = requests.get(finalLink, headers=headers)
    tree = html.fromstring(page.content)
    query = tree.xpath("/html/body/script[2]/text()")
    with open(fileName,'w') as f:
        for item in query:
            f.write("%s\n" % item)
    f.close()

if __name__ == "__main__":
    main()
