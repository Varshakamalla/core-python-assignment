def Cal_feedback(ratings):
    count=0
    for rating in ratings:
        if rating==4 or rating==5:
            count+=1
    positive_percentage = (count / len(ratings)) * 100
    return f"Positive Feedback: {positive_percentage:.2f}%"
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
result = Cal_feedback(ratings)
print(result)