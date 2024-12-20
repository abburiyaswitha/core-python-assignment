def calculate_positive_feedback_percentage(ratings):
    if len(ratings) == 0:
        return 0
    positive_ratings = [rating for rating in ratings if rating >= 4]
    positive_percentage = (len(positive_ratings) / len(ratings)) * 100
    return positive_percentage
ratings = []
num_ratings = int(input("Enter the number of ratings:"))
for _ in range(num_ratings):
    rating = int(input("Enter rating (1-5):"))
    ratings.append(rating)
positive_percentage = calculate_positive_feedback_percentage(ratings)
print(f"Positive Feedback:{positive_percentage}%")
