def analyze_pet_behavior(user_text, pet_type):
    text = user_text.lower()

    possible_interpretation = []
    what_to_observe = []
    vet_prep = []

    severity = "Low"

    # Simple keyword-based logic
    if any(word in text for word in ["not eating", "不吃", "no come", "no come", "eating less", "eat less", "食欲差", "食慾差"]):
        possible_interpretation.append("Possible appetite-related issue, stress, discomfort, or illness.")
        what_to_observe.extend([
            "Appetite changes",
            "Water intake",
            "Vomiting or diarrhea",
            "Energy level"
        ])
        vet_prep.extend([
            "Record how long the appetite change has lasted",
            "Note any vomiting, diarrhea, or lethargy",
            "Write down recent food changes"
        ])
        severity = "Medium"

    if any(word in text for word in ["hiding", "躲", "hides", "hiding under", "躲起来"]):
        possible_interpretation.append("Possible stress, pain, fear, or environmental discomfort.")
        what_to_observe.extend([
            "Activity level",
            "Reaction to touch",
            "Litter box / toilet behavior",
            "Whether this behavior is new"
        ])
        vet_prep.extend([
            "Note when the hiding started",
            "Mention any recent change in environment",
            "Record whether the pet is also eating/drinking less"
        ])
        severity = "Medium"

    if any(word in text for word in ["vomit", "vomiting", "吐", "diarrhea", "拉稀", "软便", "bloody", "blood"]):
        possible_interpretation.append("Possible digestive issue or urgent health concern.")
        what_to_observe.extend([
            "Frequency of vomiting/diarrhea",
            "Blood presence",
            "Hydration",
            "Energy level"
        ])
        vet_prep.extend([
            "Record frequency and duration",
            "Take a photo if possible",
            "Note food intake and water intake"
        ])
        severity = "High"

    if any(word in text for word in ["licking paw", "licking", "舔", "itching", "抓", "scratching"]):
        possible_interpretation.append("Possible irritation, allergy, stress, or skin discomfort.")
        what_to_observe.extend([
            "Skin redness",
            "Hair loss",
            "Frequency of licking/scratching",
            "Any new food or products"
        ])
        vet_prep.extend([
            "Note when the behavior appears most often",
            "Check for redness or wounds",
            "Write down any recent product or diet change"
        ])
        if severity == "Low":
            severity = "Medium"

    if not possible_interpretation:
        possible_interpretation.append("General behavioral change detected, but more details are needed.")
        what_to_observe.extend([
            "Appetite",
            "Water intake",
            "Activity level",
            "Sleep",
            "Toilet behavior"
        ])
        vet_prep.extend([
            "Record when the change started",
            "Describe how often it happens",
            "Take notes before a vet visit if symptoms persist"
        ])

    # remove duplicates while keeping order
    def unique_keep_order(items):
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    what_to_observe = unique_keep_order(what_to_observe)
    vet_prep = unique_keep_order(vet_prep)
    possible_interpretation = unique_keep_order(possible_interpretation)

    result = f"""
## Possible interpretation
- {" ".join(possible_interpretation)}

## Severity level
- {severity}

## What to observe
""" + "\n".join([f"- {item}" for item in what_to_observe]) + """

## Before visiting the vet
""" + "\n".join([f"- {item}" for item in vet_prep]) + """

## Important note
- This tool is only for observation support and visit preparation.
- It is not a medical diagnosis.
"""

    return result