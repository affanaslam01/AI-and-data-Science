#4.	Write a code to get first and second best scores from the list:
#Scores_list = [40, 89, 90, 89, 23, 90, 50]
Scores_list=[40,89,90,89,23,90,50]
s=[]
for scores in Scores_list:
    if scores not in s:
        s.append(scores)
s.sort(reverse=True)
print("Fist best scores: ",s[0])
print("Second best score: ",s[1])
