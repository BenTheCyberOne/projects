from lxml import html
import requests
def main():
    fileName = input(print("Please enter the filename: "))
    f = open(fileName,"x")
    
    page = requests.get()
