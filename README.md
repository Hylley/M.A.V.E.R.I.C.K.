# M.A.V.E.R.I.C.K.

Maverick (or simply Mav) is a machine-learning conversational artificial intelligence build in Python, wich make it's responses based on collections of known conversations. Made entirelly for interacting on Twitter ([@Maverick5000](https://twitter.com/Maverick5000)).

## 🔧 Installing
You can clone this repo via:
`git clone https://github.com/Hylley/M.A.V.E.R.I.C.K.`

But before executing, there are some python libraries and dependencies we need to focus.
My personal recommendation is that you use a virtual environment prepared specifically for this project.
You can install the virtualenv tool via:
```
pip install virtualenv
```
and then, at the project main folder type:
```
virtualenv [virtual environment preferred name]
```
With your virtual enviroment in hands, run ```[virtual environment name]\Scripts\activate``` at your terminal and you're ready to go.

Now, let's install our dependecies by:
```
pip install tweepy
pip install python-dotenv
```

Store all your Twitter API keys in a .env file at the project's main folder using the model:
```
API_KEY = [YOUR KEY HERE]
API_KEY_SECRET = [YOUR KEY HERE]

BEARER_TOKEN = [YOUR KEY HERE]

ACCESS_TOKEN = [YOUR KEY HERE]
ACCESS_TOKEN_SECRET = [YOUR KEY HERE]
```

Type ```python main.py``` to execute the main file and see the magic happen.


## 💻 A little bit of theory...

So you can know what you're diving into.

An untrained instance instance starts off with no knowledge of how to communicate. Each time a user enter a new sentence, it saves the text and the sentence it was in respose. As it receives more and more inputs and knowlege, it can reply with more accuracy of each response.

In a nutshell, when an user types a statment, the bot always search at it's database for the closest mach. It can do so converting each statement into a *vector* a.k.a. **[Text Vectorization](https://www.deepset.ai/blog/what-is-text-vectorization-in-nlp)**;

After that, it uses **[cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)** to measure the similarity between those vectiors. For example:
```
SimilarityCosine(
 "This is a sentence.",
 "This is a similar sentence."
)

# outputs 0.9
```
While:
```
SimilarityCosine(
 "This is a sentence.",
 "That's a different statement."
)

# outputs 0.2
```

After the search, the AI picks the most higher value, checks for the registered respose, tag it as the response and store the relation at the database.

That's basicaly it. Have fun!
