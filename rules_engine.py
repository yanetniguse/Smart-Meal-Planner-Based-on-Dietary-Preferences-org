# rules_engine.py
import random

meal_data = {
    "Grilled Vegetable Bowl": {
        "nutrition": "200 kcal, 10g protein, 5g fat",
        "link": "https://dishingouthealth.com/roasted-veggie-glow-bowls/"
    },
    "Vegan Buddha Bowl": {
        "nutrition": "350 kcal, 12g protein, 15g fat",
        "link": "https://www.feastingathome.com/vegan-buddha-bowls/"
    },
    
}

def get_meals_by_preferences(preferences):
    rules = {
        "vegetarian": ["Veggie Stir Fry", "Quinoa Salad", "Mushroom Pasta",["Grilled Vegetable Bowl", "Mushroom Quinoa", "Vegetarian Sushi"]],
        "vegan": ["Lentil Soup", "Vegan Burrito", "Tofu Stir Fry","Raw Vegan Salad", "Vegan Buddha Bowl", "Lentil Stew"],
        "keto": ["Grilled Chicken & Avocado", "Cheesy Omelet", "Zucchini Lasagna"],
        "gluten-free": ["Salmon with Roasted Veggies", "Stuffed Peppers", "Grilled Steak & Beans"],
        "high-protein": ["Turkey Wrap", "Protein Smoothie", "Beef & Broccoli"],
        "low-carb": ["Zucchini Noodles", "Egg Muffins", "Cauliflower Pizza"],
        "dairy-free": ["Chicken Stir Fry", "Coconut Curry", "Dairy-Free Oatmeal"],
        "nut-free": ["Rice & Beans", "Vegetable Soup", "Fish with Veggies"],
        "low-fat": ["Steamed Veggies & Grilled Fish", "Boiled Eggs with Fruit", "Grilled Tofu", "Boiled Vegetables", "Steamed Chicken Breast", "Fruit Salad"],
        "diabetic-friendly": ["Chickpea Salad", "Low-carb Chicken Bowl", "Steamed Greens & Beans","Low-Carb Veggie Bowl", "Grilled Fish with Broccoli", "Quinoa & Avocado"]
    }

    meals = []
    for pref in preferences:
        meals.extend(rules.get(pref, []))

    # fallback if nothing selected
    if not meals:
        meals = ["Mixed Veg Rice", "Chicken Soup", "Fruit Salad"]

    return list(set(meals))  # remove duplicates


def filter_meals(meals, allergies, religion, raw_food, on_diet, other_notes):
    # Remove meals based on allergies
    filtered = [meal for meal in meals if not any(a in meal.lower() for a in allergies.split(','))]

    # Apply religious filters
    if "Judaism" in religion:
        filtered = [meal for meal in filtered if "pork" not in meal.lower()]
    if "Islam" in religion:
        filtered = [meal for meal in filtered if "pork" not in meal.lower() and "alcohol" not in meal.lower()]
    if "Roman Catholicism" in religion:
        # Avoid meat on Fridays — assume we just exclude meat for simplicity
        filtered = [meal for meal in filtered if "chicken" not in meal.lower() and "beef" not in meal.lower()]
    if "Orthodox Christianity" in religion:
        # No animal products on Wed & Fri
        filtered = [meal for meal in filtered if "chicken" not in meal.lower() and "egg" not in meal.lower() and "milk" not in meal.lower()]
    if "Mormonism" in religion:
        filtered = [meal for meal in filtered if "coffee" not in meal.lower() and "tea" not in meal.lower() and "alcohol" not in meal.lower()]

    # Handle raw food
    if raw_food == "yes":
        filtered = [meal for meal in filtered if "raw" in meal.lower() or "salad" in meal.lower()]

    # Diet filter
    if on_diet == "yes":
        filtered = [meal for meal in filtered if "salad" in meal.lower() or "steamed" in meal.lower() or "boiled" in meal.lower()]

    # Basic fallback
    if not filtered:
        filtered = ["Customized Fruit Bowl", "Couscous Salad", "Vegetable Lentil Soup"]

    return list(set(filtered))


def generate_multi_day_meal_plan(preferences, days, allergies, religion, raw_food, on_diet, other_notes, meals_per_day):
    all_meals = get_meals_by_preferences(preferences)
    meals = filter_meals(all_meals, allergies, religion, raw_food, on_diet, other_notes)

    meal_plan = {}
    for day in range(1, days + 1):
        daily = random.sample(meals, k=min(meals_per_day, len(meals)))
        # Add nutrition info
        detailed = [
            {
                "name": meal,
                "nutrition": meal_data.get(meal, {}).get("nutrition", "N/A"),
                "link": meal_data.get(meal, {}).get("link", "#")
            } for meal in daily
        ]
        meal_plan[f"Day {day}"] = detailed

    return meal_plan



    
