# M.A.V.E.R.I.C.K.

Maverick (or simply Mav) is a machine-learning conversational artificial intelligence build in Python, wich make it's responses based on collections of known conversations. Made entirelly for interacting on Twitter ([@Maverick5000](https://twitter.com/Maverick5000)).

## 🔧 Installing
You can clone this repo via:
`git clone https://github.com/Hylley/M.A.V.E.R.I.C.K.`

But before running, there are some dependencies we need to focus on.
My personal recommendation is that you use a virtual environment prepared specifically for this project.
You can install the virtualenv tool via:
```
pip install virtualenv
```
and then, in the main project folder, type:
```
virtualenv [preferred_name]
```
With your virtual environment in hand, run ```[preferred_name]\Scripts\activate``` in your terminal and you're ready to go.

Now, install the dependencies by:
```
pip install tweepy
pip install python-dotenv
```

Next, store all your Twitter API keys in an ".env" file in the main project folder using the model:
```
API_KEY = [YOUR_KEY_HERE]
API_KEY_SECRET = [YOUR_KEY_HERE]

BEARER_TOKEN = [YOUR_KEY_HERE]

ACCESS_TOKEN = [YOUR_KEY_HERE]
ACCESS_TOKEN_SECRET = [YOUR_KEY_HERE]
```

Type ```python main.py``` to run the main file and watch the magic happen.


## 💻 A little bit of theory...

So you can know what you're diving into.

An untrained instance starts off with no knowledge of how to communicate. Each time a user enter a new sentence, it saves the its content and the content of the sentence that was in respose. As it receives more and more inputs and knowlege, it can reply more accurately the next time.

In a nutshell, when an user types a statment, the bot always searches its database for the closest mach. It can do so converting each statement into a *vector* a.k.a. **[Text Vectorization](https://www.deepset.ai/blog/what-is-text-vectorization-in-nlp)**. For example:
```
GenerateVector("This is a cool sentence.")

# outputs: {
  'This': 1,
  'is': 1,
  'a': 1,
  'cool': 1,
  'sentence': 1
}
```

After that, it uses **[cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)** to measure the similarity between these vectors. For example:
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

After the fetch, the AI picks the highest value, checks for the recorded respose, tag it as an answer and store that relationship in the database.

That's basicaly it. Have fun!
