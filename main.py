from time import time

# defining the accuracy of input
def typeErrors(prompt):
    global iwords    # input words

    words = prompt.split()
    errors = 0

    for i in range (len(iwords)):
        if i in (0,len(iwords)-1):
            if iwords[i]==words[i]:
                continue
            else :
                errors+=1
        else :
            if iwords[i]==words[i]:
                if ((iwords[i+1] == words[i+1]) & (iwords[i-1]== words[i-1])):
                    continue
                else:
                    errors+=1
            else:
                errors+=1

    return errors

#calculate speed in words per minute
def typingSpeed(iprompt,start_time,end_time):

    global time
    global iwords

    iwords = iprompt.split()
    total_words = len (iwords)
    speed = total_words/time

    return speed

def timeElapsed(start_time,end_time):
    return end_time - start_time

if __name__ == '__main__':
    import random

    eg1 = "Python is a OOP language released in 1991."
    eg2 = "Shri Bhagubhai Mafatlal Polytechnic"
    eg3 = "Python is a high-level, interpreted, general-purpose programming language."

    list = [eg1, eg2, eg3]
    prompt = random.choice(list)


    print("Type this :- ",prompt)

    #input
    input("press ENTER when you are ready ")

    #recording time taken to input

    stime = time()
    iprompt= input()
    etime = time()

    time = round(timeElapsed(stime,etime),2)
    speed = typingSpeed(iprompt,stime,etime)
    errors = typeErrors(prompt)

    #print
    print("Total time Elapsed : ",time,"s")
    print("your average speed was: ",speed,"words/minute")
    print("with a total of ",errors,"errors")



















