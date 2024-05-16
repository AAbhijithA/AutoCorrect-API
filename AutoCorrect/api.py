from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

class Trie:
    def __init__(self):
        self.prefix_of = 0
        self.branches = 0
        self.word = False
        self.next = {}

Root = Trie()

with open('words_alpha.txt', 'r') as file:
    for line in file:
        word = line.strip()
        Node = Root
        for c in word:
            if c in Node.next:
                Node.next[c].prefix_of += 1
            else:
                Node.next[c] = Trie()
                Node.next[c].prefix_of = 1
                Node.branches += 1
            Node = Node.next[c]
        Node.word = True

def autocorrect(word,i,Node,edit_distance,suggestions,sug,searchspace):
    if(len(suggestions) == searchspace):
        return
    if(i == len(word)):
        print(sug)
        if Node.word == True:
            suggestions.append([Node.prefix_of,edit_distance,sug])
        return
    if word[i] in Node.next:
        autocorrect(word,i+1,Node.next[word[i]],edit_distance,suggestions,sug+word[i],searchspace)
    check = []
    for key in Node.next:
        check.append([key,Node.next[key].prefix_of])
    check.sort(key = lambda x : x[1])
    child = Node.branches
    while(child > 0):
        if(word[i] != check[child-1][0]):
            autocorrect(word,i+1,Node.next[check[child-1][0]],edit_distance+1,suggestions,sug+check[child-1][0],searchspace)
        child -= 1
    return
        
@app.get("/autocorrect")
async def AutoCorrecter(word: str, suggestion: int, searchspace: int):
    suggestions = []
    global Root
    autocorrect(word,0,Root,0,suggestions,"",searchspace)
    suggestions.sort(key = lambda x : (x[1],-x[0]))
    best_suggestions = []
    for i in range(0,min(suggestion,len(suggestions))):
        best_suggestions.append(suggestions[i][2])
    return best_suggestions

