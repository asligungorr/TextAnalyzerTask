# TEXT ANALYZER

In this task, you are going to implement a word analyzer for a given text.

## Task

You are going to find the following details of a given text:

- Word count
- Number of Letters
- Longest word
- Average word length
- Reading Duration in Seconds
- BONUS: Median word length
- BOUNS: Median word when all words sorted by length
- BONUS: Top 5 most common words
- BONUS: Guess the text language (english and turkish only)

You are going to create a **REST API** to provide these values. You must create a **REST API** not a HTML interface. You can use one of the **Go**, **Python** and **Javascript** programming languages to implement the task.

You **don't need any third party library** like flask or gorilla for this task. Standart libraries in python, go, and javascript (nodejs) have all you need. Therefore, don't use them.

You also don't need to use any third party library to guess text language. Just search for stopwords to determine the text language.

## HTTP REST API

```
PATH: /analyze
METHOD: POST
BODY: JSON

SAMPLE: 
POST http://localhost:8080/analyze
REQUEST BODY:
{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
}

RESPONSE:
{
    "wordCount": 94,
    "letters": 577,
    "longest": "Neurologically",
    "avgLength": 4.2,
    "duration": 47,
    "medianWordLength": 3,
    "medianWord: get,
    "language": "en"
}

```

⚠️ Response data created hypothetically and they are not real values.

**BONUS:** 

Add filtering options to the request body. If there is no option given on request return all fields.

```
PATH: /analyze
METHOD: POST
BODY: JSON

SAMPLE: 
POST http://localhost:8080/analyze
REQUEST BODY:
{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
    "analysis": ["wordCount", "language"]
}

RESPONSE:
{
    "wordCount": 94,
    "language": "en"
}

```

or get filtering options from URL:
```
http://localhost:8080/analyze?analysis=wordCount,language
```

## Notes

- Don't share your code online publicly. Use Gitlab or Github for private git repository.
- Optional bonuses will give you extra points.   
- If you can't start immediately, please notify us by replying to this mail.  
- Add @sercand, @utkayd, @iremkaraoglu to collaborators list on Gitlab or Github. 
