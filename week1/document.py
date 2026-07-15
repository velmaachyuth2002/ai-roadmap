from collections import Counter
class Document:
    def __init__(self,text:str,label:int):
        self.text=text
        self.label=label
        self.tokens=text.split()
    def __repr__(self):
        return f"Document({self.text}, label={self.label})"
    def __len__(self):
        return len(self.tokens)
    def __eq__(self,other):
        return self.text==other.text
    def __hash__(self):
        return hash(self.text)
    def unique_tokens(self) -> set[str]:
        return set(self.tokens)
class Corpus:
    def __init__(self,documents:list[Document]):
        self.documents=documents
    def __len__(self):
        return len(self.documents)
    def __getitem__(self,i):
        return self.documents[i]
    def doc_frequency(self) -> dict[str, int]:
        counter=Counter()
        for document in self.documents:
            counter.update(document.unique_tokens())
        return dict(counter)
    def most_common(self, n: int):
        frequencies = Counter(self.doc_frequency())
        return frequencies.most_common(n)
doc1 = Document("great film", 1)
doc2 = Document("awful pacing", 0)
doc3 = Document("great great pacing", 1)

corpus = Corpus([doc1, doc2, doc3])
for doc in corpus:
    print(doc.text)

my_set={doc1,doc2}
print(my_set)
