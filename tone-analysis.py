#python3
from textblob import TextBlob

print("Tone analysis for Python")
print("Please input a statement regarding the product")
text_to_analyze = TextBlob(input())


#polarity [-1,1], subjectivity [0,1]
#if p < 0 , then negative; if p>.4, then positive; else, nuetral

if text_to_analyze.sentiment.polarity > .4:
    print("Thanks for your positive statement")
elif text_to_analyze.sentiment.polarity < 0:
    print("I am sorry to hear about your poor statement")
else: 
    print("That is a pretty neutral answer")
    
print(text_to_analyze.sentiment)