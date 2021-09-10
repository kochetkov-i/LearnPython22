classes_info = [
    {'school_class': '4a', 'scores': [3,4,4,5,2,5,3,5]}, 
    {'school_class': '4b', 'scores': [3,4,4,5,2]}, 
    {'school_class': '5a', 'scores': [3,4,4,5,2]}, 
    {'school_class': '6b', 'scores': [5,5,5,5,5]}, 
    {'school_class': '9a', 'scores': [2,2,2,2,2]}, 
    {'school_class': '7c', 'scores': [3,4,4]}
    ]

all_scores = []

for class_info in classes_info:
    avg_class = sum(class_info["scores"]) / len(class_info["scores"])
    output_avg_class = f"AVG {class_info['school_class']} class value is {avg_class}"
    print(output_avg_class)
    all_scores.extend(class_info["scores"])

avg_class_score = sum(all_scores) / len(all_scores)
output_avg_all = f"AVG all classes value is {avg_class_score}"
print(output_avg_all)
