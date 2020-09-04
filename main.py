import math

from essential_generators import DocumentGenerator
from pip._vendor.distlib.compat import raw_input

class VectorCompare:
  # measures how strong the match is
  def magnitude(self,concordance):
    if type(concordance) != dict:
      raise ValueError('Value passed in magnitude() not a str')
    totalMagnitude = 0
    for word,count in concordance.items():
      totalMagnitude += count ** 2
    return math.sqrt(totalMagnitude)

  # calculates a relation between the inputed word and document
  def relation(self,concordance1, concordance2):
    if type(concordance1) != dict:
      raise ValueError('First value passed in relation() not a str')
    if type(concordance2) != dict:
      raise ValueError('Second value passed in relation() not a str')
    topvalue = 0
    for word, count in concordance1.items():
      if word in concordance2.keys():
        topvalue += count * concordance2[word]
    if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
      return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
    else:
      return 0

  # concordance is count of every word in documents
  def concordance(self,document):
    if type(document) != str:
      raise ValueError('Value passed in concordance() not a str')
    count = {}
    for word in document.split(' '):
      if word in count.keys():
        count[word] = count[word] + 1
      else:
        count[word] = 1
    return count



v = VectorCompare()
gen = DocumentGenerator()
documentDic = {}
index = {}
searchterm = ""


#test with a small sample size of 1000 documents
for x in range(0,1000):
    documentDic[x] = gen.paragraph()

for x in range(0, 1000):
    index[x] = v.concordance(documentDic[x].lower())

#search for inputed word
while(searchterm != "<exit>"):

    searchterm = raw_input('Enter Search Term: ')
    matches = []

    for i in range(len(index)):
      con = v.concordance(searchterm.lower())
      relation = v.relation(con,index[i])
      if relation != 0:
        matches.append((relation,documentDic[i][:100]))

    matches.sort(reverse=True)

    # print out best results
    for i in matches:
      print(i[0], i[1])
