list_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2,5,3,5]}, 
    {'school_class': '4b', 'scores': [3,4,4,5,2]}, 
    {'school_class': '5a', 'scores': [3,4,4,5,2]}, 
    {'school_class': '6b', 'scores': [5,5,5,5,5]}, 
    {'school_class': '9a', 'scores': [2,2,2,2,2]}, 
    {'school_class': '7c', 'scores': [3,4,4]}
    ]

all_scores = []

for class_score in list_scores:
    avg_class = sum(class_score["scores"]) / len(class_score["scores"])
    output_avg_class = f"AVG {class_score['school_class']} class value is {avg_class}"
    print(output_avg_class)
    all_scores.extend(class_score["scores"])

avg_scores = sum(all_scores) / len(all_scores)
output_avg_all = f"AVG all classes value is {avg_scores}"
print(output_avg_all)
