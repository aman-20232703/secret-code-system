import random
import string
random_letters = ''.join(random.choices(string.ascii_lowercase, k=3))
st=input("emter message: ")
words= st.split(" ")

coding=True
if(coding):
    nwords=[]
    for word in words:
        if (len(word)>=3):
            r1=random_letters
            r2=random_letters

            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if (len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)

        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))