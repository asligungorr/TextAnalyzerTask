###Requires: 
version Python3.10

Only accepts POST requests
Address: http://localhost:8080/analyze

#Test 1:

-http://localhost:8080/analyze \r\n
-{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing. However, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place. Neurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
}

#Test 2:

-http://localhost:8080/analyze
-{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing. However, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place. Neurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world.",
	"analysis": ["wordCount", "language"]
}

#Test 3:

-http://localhost:8080/analyze?analysis=wordCount,language
-{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing. However, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place. Neurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
}
