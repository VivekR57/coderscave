import time
string="i am vivek from chennai"
wordcount=len(string.split())
print(string)
while True:
    t0=time.time()
    inputtext=str(input("Enter the sentence:"))
    t1=time.time()
    accuracy=len(set(inputtext.split())&set(string.split()))
    accuracy=accuracy/wordcount
    timetaken=t1-t0
    wpm=wordcount/timetaken
    print("WPM",wpm,"Accuracy",accuracy,"Timetaken",timetaken)
