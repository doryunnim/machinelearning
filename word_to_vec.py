from gensim.models import word2vec
from konlpy.tag import Twitter

twitter = Twitter()
word_dic = {}
file = open("kowiki.xml", "r", encoding="utf8")
lines = file.read().split("\r\n")
results = []

for line in lines:
    r = []
    malist = twitter.pos(line, norm=True, stem=True) 
    for (word, pumsa) in malist:
        if not pumsa in ["Josa", "Eomi", "Punctuation"]:
            r.append(word)
    results.append((" ".join(r)).strip())
output = (" ".join(results)).strip()
with open("kowiki.wakati", "w", encoding="utf-8") as fp:
    fp.write(output)

 
file.close()

data = word2vec.LineSentence("kowiki.wakati")
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("kowiki.model")