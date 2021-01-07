from lxml import html
import requests
# https://docs.python-guide.org/scenarios/scrape/

keywords = input("Enter your keywords: ")

page = requests.get('https://www.dizy.com/it/cruciverba/?q=' + keywords.replace(" ","+"))
tree = html.fromstring(page.content)

# Select the attribute 'href' for each 'a' tag
# which is a son of a 'li' tag, wherever in the document
links = tree.xpath('//li/a/@href')
links = list(dict.fromkeys(links))

results = []
for link in links:
    page2 = requests.get('https://www.dizy.com/' + link)
    tree = html.fromstring(page2.content)
    
    # Select the 'b' tag, son of all the 'td' tags,
    # sons of the second 'tr' tag, son of a 'table' tag, wherever in the document
    words = tree.xpath('//table/tr[2]/td/b/text()')
    
    # It could be the case that exist more than 1 solution for each definition
    for w in words:
        results.append(w)

# Remove possible duplicates
results = list(set(results))
print("\nRISULTATI TROVATI: ", len(results))
for word in results:
    print("- " + str(len(word.replace(" ", ""))) + " lettere: " + word)
print()
