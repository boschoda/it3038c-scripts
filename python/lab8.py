import requests, re
from bs4 import BeautifulSoup

r = requests.get ('https://www.cherrygroveanimalhospital.vet/services').content
soup = BeautifulSoup(r, 'html.parser')
span = soup.find("h2", {"class":"title-heading-left fusion-responsive-typography-calculated"})
title = span.title
span = soup.find("span", {"class":"fusion-button button-flat fusion-button-default-size button-default button-1 fusion-button-default-span fusion-button-default-type"})
app = span.app
span = soup.find("span", {"class":"fusion-layout-column fusion_builder_column fusion-builder-column-1 fusion_builder_column_2_5 2_5 fusion-two-fifth fusion-column-last fusion-column-no-min-height"})
contact = span.contact

print("Cherry Grove's motto is %s and you can %s and find the following information %s" % (title, app, contact))