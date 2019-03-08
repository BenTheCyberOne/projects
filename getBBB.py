"""
Version: 1.0.0
Developed by: Ben Breshears (bhbreshears@dmacc.edu)
Scrapes the BBB for businesses with given parameters using lxml and requests libraries

"""
from lxml import html
import requests
def main():
    print("### WARNING: CURRENTLY CAN ONLY BE USED WITH THE FOLLOWING OPTIONS:\n>A LOCATION\n>ACCREDITED FILER\n>JOB TYPE (QUERY)")
    fileName = input("Please enter filename for output files(leave out the ext): ")
    f = open(fileName,"x")
    loc = input("Please enter a city: (Ex. Des Moines)")
    loc2 = input("Please enter the state: (Ex. IA)")
    acc = input("Search for accredited businesses only? (y or n) ")
    entity = input("Enter the job title to scrape: ")
    if acc == 'n':
        filter = ""
    else:
        filter ="filter_accredited=1&"
    finalLink = ("https://www.bbb.org/search?"+filter+"find_country=USA&find_loc="+loc+"%2C%20"+loc2+"&find_text="+entity+"&find_type=Category&page=1&sort=Relevance/")
    page = requests.get()
if __name__ == "__main__":
    main()
