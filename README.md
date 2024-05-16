# AutoCorrect API
### An Autocorrect API built from sratch using the Trie or Prefix Tree Data Structure along with FastAPI to handle asynchronous calls.

## Working 
![](Trie.jpg)
 Trie works by storing the prefixes in a Tree Data Structure, in our implementation we used the words from the text from from this repository, feel free to check it out [Link to Repository](https://github.com/dwyl/english-words/tree/master) and the file **'words_alpha.txt'** was used since this implementation doesn't focus on special characters.
 The Trie stores the number of prefix count of the words traversed through the node, checking if the node so far represents the end of the word or not (checking if it's a valid word) for autosuggestion. The AutoCorrecter ranks valid words it found in search space sorted with respect to difference in strings (how many characters differ) in ascending order
 and total prefixes of all dictionary words passing through that node in descending order. The top (or first) 'K' suggestions are taken after sorting them. The Trie is traversed by giving priority to the next word if it exists first and other children of the node are sorted in descending order via the prefixes passing through it and we solve for the 
 solution space this way.

## Setting Up files and Run the API
### Clone the repository using the following command (or download it)
```
```
### cd into the api.py folder and set up your virtual environment and necessary files (for Windows):
```bash
> cd AutoCorrect
> python -m venv env
> env\Scripts\activate
> python -m pip install uvicorn
> python -m pip install fastapi
```
### Run the API using the Command:
```bash
> uvicorn api:app --reload
```
### Generally the API runs at 'http://127.0.0.1:8000/' (local projects)

## API Key value Parameters:

 word = the word you are trying to autocorrect
 suggestion = number of suggestions needed
 searchspace = how many solutions to maximum search for in the Trie (to reduce time taken to respond)

## How to fetch Data:

**Use the following url endpoint to request for the autosuggestions:**
```
http://127.0.0.1:8000/autocorrect?word={word_to_autocorrect}&suggestion={number_of_suggestions_needed}&searchspace={solutions_to_terminate_at}
```
***(Note: Replace 'http://127.0.0.1:8000/' if it's hosted publicly)***



