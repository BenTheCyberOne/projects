"""
Version: 1.0.0
Developed by: Ben Breshears (bhbreshears@dmacc.edu)
Scrapes the BBB for businesses with given parameters using lxml and requests libraries

"""
from lxml import html
import requests
def main():
    print("### WARNING: CURRENTLY CAN ONLY BE USED WITH THE FOLLOWING OPTIONS:\n>A LOCATION\n>ACCREDITED FILER\nPlease note that in order to search for something besides 'Electrician', you must enter the FULL find_entity code during the scrapping!")
    fileName = input(print("Please enter filename for output files(leave out the ext): "))
    f = open(fileName,"x")
    loc = input(print("Please enter a location exactly like the example: (Ex. Des Moines, IA)"))
    acc = input(print("Search for accredited businesses only? (Y or N) "))
    entity = input(print("#OPTIONAL# Enter the find_entity EXACTLY how it appears, press enter for default (Electrician): "))
    page = requests.get()
