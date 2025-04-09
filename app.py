from flask import Flask, render_template, request, jsonify, send_file, session
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import timedelta
import random
import io

app = Flask(__name__, template_folder='templates')
app.secret_key = 'mealplannersecret'
app.permanent_session_lifetime = timedelta(hours=1)

# ---------------------------- MOCK DATA ---------------------------- #
meal_data = {
    "Grilled Vegetable Bowl": {"nutrition": "200 kcal, 10g protein", "link": "https://example.com/veg-bowl"},
    "Vegan Buddha Bowl": {"nutrition": "350 kcal, 12g protein", "link": "https://example.com/buddha-bowl"},
    "Tofu Stir Fry": {"nutrition": "400 kcal, 20g protein", "link": "https://example.com/tofu-stirfry"},
    "Fruit Salad": {"nutrition": "150 kcal, 2g protein", "link": "https://example.com/fruit-salad"},
    "Lentil Soup": {"nutrition": "300 kcal, 18g protein", "link": "https://example.com/lentil-soup"},
    "Chickpea Curry": {"nutrition": "450 kcal, 15g protein", "link": "https://example.com/chickpea-curry"},
    "Quinoa Salad": {"nutrition": "330 kcal, 12g protein", "link": "https://example.com/quinoa-salad"}
}
meal_pool = list(meal_data.keys())

religious_rules = {
    "None": [],
    "Judaism": ["pork", "shellfish"],
    "Islam": ["pork", "alcohol"],
    "Roman Catholicism": ["meat on Friday"],
    "Orthodox Christianity": ["animal product on Wednesday", "animal product on Friday"],
    "Mormonism": ["alcohol", "coffee", "tea"],
    "Hinduism": ["beef"],
    "Buddhism": ["meat"],
    "Sikhism": ["halal", "kosher"]
}

CALORIE_RECOMMENDATIONS = {
    "Underweight": {"calories": 2500, "foods": "Nuts, Avocados, Whole Grains, Protein-rich foods"},
    "Healthy Weight": {"calories": 2000, "foods": "Balanced diet with lean proteins, fruits, and vegetables"},
    "Overweight": {"calories": 1800, "foods": "High-fiber foods, Lean proteins, Low-fat dairy"},
    "Obese": {"calories": 1500, "foods": "Leafy greens, Lean meat, Low-carb foods"}
}

GOAL_RECOMMENDATIONS = {
    "muscle_gain": {
        "title": "💪 Muscle Building Plan",
        "description": "Focus on high-protein foods, resistance training, and calorie surplus.",
        "foods": "Chicken, Salmon, Eggs, Greek yogurt, Almonds, Quinoa"
    },
    "weight_loss": {
        "title": "🏋️ Weight Loss Plan",
        "description": "Prioritize a calorie deficit with high-fiber and lean protein foods.",
        "foods": "Leafy greens, Lean meats, Oats, Nuts, Avocados, Chia seeds"
    },
    "hair_growth": {
        "title": "✨ Hair Growth Plan",
        "description": "Consume foods rich in biotin, zinc, and omega-3.",
        "foods": "Fish, Walnuts, Eggs, Berries, Sweet potatoes, Spinach"
    },
    "energy_boost": {
        "title": "⚡ Energy Boost Plan",
        "description": "Eat complex carbs and maintain stable blood sugar.",
        "foods": "Bananas, Whole grains, Nuts, Dark chocolate, Greek yogurt, Lentils"
    }
}

# ------------------------ UTILITY FUNCTIONS ------------------------ #
def generate_varied_meal_plan(days, meals_per_day):
    meal_plan = {}
    used_meals = set()

    for day in range(1, days + 1):
        available_meals = [m for m in meal_pool if m not in used_meals]
        choices = random.sample(available_meals, min(meals_per_day, len(available_meals)))

        daily_meals = [{
            "name": meal,
            "nutrition": meal_data[meal]["nutrition"],
            "link": meal_data[meal]["link"]
        } for meal in choices]

        used_meals.update(choices)
        if len(used_meals) >= len(meal_pool):
            used_meals.clear()

        meal_plan[f"Day {day}"] = daily_meals
    return meal_plan

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def calculate_calorie_goal(bmi, current_calories):
    if bmi > 30:
        return "obese", current_calories * 0.8
    elif 25 < bmi <= 30:
        return "overweight", current_calories * 0.9
    elif 18.5 < bmi <= 25:
        return "healthy", current_calories
    else:
        return "underweight", current_calories * 1.1

# ----------------------------- ROUTES ------------------------------ #
@app.route('/')
def index():
    return render_template('index.html', religions=list(religious_rules.keys()))

@app.route('/results', methods=['POST'])
def results():
    days = int(request.form.get('days'))
    meals_per_day = int(request.form.get('meals_per_day'))
    religion = request.form.get('religion')
    other_notes = request.form.get("other_notes", "")
    session["other_notes"] = other_notes  # For future access



    plan = generate_varied_meal_plan(days, meals_per_day)
    session['meal_plan'] = plan
    return render_template('results.html', meal_plan=plan, editable=True)

@app.route('/edit', methods=['POST'])
def edit():
    session['meal_plan'] = request.json.get('meal_plan')
    return jsonify({"message": "Meal plan updated successfully"})

@app.route('/get_plan', methods=['GET'])
def get_plan():
    return jsonify(session.get('meal_plan', {}))

@app.route('/clear_plan', methods=['POST'])
def clear_plan():
    session.pop('meal_plan', None)
    return jsonify({"message": "Meal plan cleared"})

@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    meal_plan = session.get('meal_plan')
    if not meal_plan:
        return "No meal plan data available in session.", 400

    try:
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        y = height - 50

        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, y, "Smart Meal Plan")
        y -= 40

        for day, meals in meal_plan.items():
            p.setFont("Helvetica-Bold", 12)
            p.drawString(50, y, f"{day}")
            y -= 20

            p.setFont("Helvetica", 11)
            for meal in meals:
                name = meal.get("name", "N/A")
                nutrition = meal.get("nutrition", "N/A")
                p.drawString(70, y, f"- {name} | {nutrition}")
                y -= 20

                if y < 50:
                    p.showPage()
                    y = height - 50

        p.save()
        buffer.seek(0)

        return send_file(buffer, as_attachment=True, download_name="meal_plan.pdf", mimetype="application/pdf")
    
    except Exception as e:
        return f"PDF generation failed: {str(e)}", 500



@app.route("/recommendations", methods=["POST"])
def get_recommendations():
    data = request.json
    status = data.get("status")
    recommendation = CALORIE_RECOMMENDATIONS.get(status, {"calories": "N/A", "foods": "N/A"})
    return jsonify(recommendation)

@app.route("/goal_recommendations", methods=["POST"])
def goal_recommendations():
    data = request.json
    goal = data.get("goal")
    recommendation = GOAL_RECOMMENDATIONS.get(goal, {
        "title": "Unknown Goal",
        "description": "No specific recommendations available.",
        "foods": "N/A"
    })
    return jsonify(recommendation)

# ---------------------------- MAIN ---------------------------- #
if __name__ == '__main__':
    app.run(debug=True)
