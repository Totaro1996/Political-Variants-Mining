from bs4 import BeautifulSoup

tei_doc = 'Verri_digitale.xml'
with open(tei_doc, 'r', encoding='utf8') as tei:
    soup = BeautifulSoup(tei, 'lxml')



def read_tei(tei_file):
    with open(tei_file, 'r', encoding='utf8') as tei:
        soup = BeautifulSoup(tei, 'lxml')
    return soup
    #raise RuntimeError('Cannot generate a soup from the input')



soup = read_tei('Verri_digitale.xml')


following = soup.find_all('add', type='#following')
addiction = soup.find_all('add', category='#addiction')
writtenabove = soup.find_all('add', type='#writtenabove')
from_ = soup.find_all('add', type='#from')
preceding =  soup.find_all('add', type='#before')
overwritten = soup.find_all('add', type='#overwritten')


stats = []
for i in following:
    stats.append(i)
#print("following:", len(stats))

stats2 = []
for i in addiction:
    stats2.append(i)
#print("addiction:", len(stats2))

stats3 = []
for i in writtenabove:
    stats3.append(i)
#print("writtenabove:",len(stats3))

stats4 = []
for i in from_:
    stats4.append(i)
#print("from:", len(stats4))

stats5 = []
for i in preceding:
    stats5.append(i)
#print("preceding:",len(stats5))

stats6 = []
for i in overwritten:
    stats6.append(i)
#print("overwritten:", len(stats6))


