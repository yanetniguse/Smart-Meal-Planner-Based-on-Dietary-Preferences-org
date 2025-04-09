
# Smart Meal Planner Based on Dietary Preferences 🥗

## Overview 🌐

The **Smart Meal Planner** is an intelligent web application designed to help users plan meals based on their unique dietary preferences, health conditions, and specific fitness goals. By leveraging **Flask** and **Python**, this solution provides personalized meal plans, health-based recommendations, and interactive tools to support users on their journey to optimal health and wellness. 💪🍏

---

## The Problem We Solve 🧐

Many existing meal planning apps fail to deliver a tailored approach. They overlook important factors such as:
- **Dietary preferences** 🌱
- **Health conditions** 🏥
- **Religious restrictions** ✝️
- **Raw food diets** 🥒
- **Specific fitness goals** 🏋️‍♂️

Users often need a more **comprehensive and personalized** solution. Our app offers just that—meal plans customized to **individual needs** and **lifestyle factors**, along with real-time guidance and actionable recommendations.

---

## Our Solution: Smart Meal Planner 🚀

Unlike generic meal planners, **Smart Meal Planner** offers a **highly personalized** solution that combines multiple health factors and user inputs to generate custom meal plans.

### Key Features: ✨

1. **Personalized Meal Planning** 🍽️
   - Generate meal plans based on:
     - Number of days 🗓️
     - Meals per day 🍴
     - Religious restrictions and allergies 🚫
     - Health conditions and dietary lifestyle 💡
   - **Edit**, **save**, and **download** meal plans as PDFs for later use 📥

2. **BMI Calculator** 🧑‍⚕️
   - Users can calculate their **Body Mass Index (BMI)** and receive personalized **action plans** based on their health status.

3. **Goal-Oriented Nutrition** 🎯
   - Users with specific goals (e.g., building muscle, growing hair) get personalized meal suggestions with calorie and nutrient requirements.

4. **Interactive Chatbot** 🤖
   - Our AI chatbot offers **real-time guidance** for meal planning, answering questions, and assisting with meal adjustments.

---

## Why This Solution is Unique and Valuable ✨

1. **Highly Personalized** 🎨: Customizes meal plans for a **variety of user preferences**, goals, and health conditions.
2. **Comprehensive Health Focus** 🏥: Offers a **holistic health tool** that includes BMI calculations and goal-specific meal recommendations.
3. **Interactivity** 🔄: Users can **edit**, **save**, and **retrieve** meal plans, offering high flexibility.
4. **Tech-Driven** 💻: Built with **Flask** for scalability and powered by a **rules engine** for dynamic meal plan generation.

This project stands out due to its focus on personalized, data-driven meal planning in a way that traditional tools don't, providing users with a comprehensive wellness solution.

---

## Project Structure 📂

```
mealplanner:.
├── app.py                # Core Flask application 🧑‍💻
├── templates             # HTML templates 📑
│   ├── index.html        # Homepage template 🏠
│   ├── results.html      # Results page 📝
├── static                # Static files (CSS) 🎨
│   ├── style.css         # Custom styles 🎨
├── rules_engine.py       # Meal planning logic ⚙️
└── README.md             # Project documentation 📖
```

---

## Installation Instructions ⚙️

### Step 1: Clone the repository
```bash
git clone https://github.com/yanetniguse/Smart-Meal-Planner-Based-on-Dietary-Preferences-org.git
```

### Step 2: Set up the environment
```bash
cd Smart-Meal-Planner-Based-on-Dietary-Preferences-org
python -m venv myenv
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the app
```bash
python app.py
```

Access the app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 🌍

---
## Screenshots 📸

Here are some screenshots showcasing the key features of the **Smart Meal Planner** app:

### 1. **Homepage** 🏠
![Homepage](https://github.com/user-attachments/assets/5623adbe-ec12-4ddf-8249-8e7077c1ae2d)
![Homepage](https://github.com/user-attachments/assets/3c3c06a8-069c-4d15-bc49-a2bbd8f2ae72)


_A user-friendly landing page where users can enter their preferences and generate personalized meal plans._

### 2. **Meal Plan Results** 🍽️
![image](https://github.com/user-attachments/assets/ec6e5521-58f9-4c9d-8772-1a38d4916985)

_The meal plan generated based on the user's dietary preferences, goals, and health conditions. Editable and downloadable._

### 3. **BMI Calculator** 🧑‍⚕️
![BMI Calculator](https://github.com/user-attachments/assets/f8598932-d48a-4e3f-8a27-4324ecf853f0)
![BMI Calculator](https://github.com/user-attachments/assets/92caa430-95d9-4592-b05d-03893f3b2207)

_A simple yet effective BMI calculator providing health recommendations based on the user's weight and height._

### 4. **Goal-Based Nutrition** 🎯
![Goal-Based Nutrition](https://github.com/user-attachments/assets/02b021dc-5d4f-4383-9d64-b1a67371b329)
![Goal-Based Nutrition](https://github.com/user-attachments/assets/940505fd-a8c0-4a9f-83e5-f1d5e29f99bc)
![Goal-Based Nutrition](https://github.com/user-attachments/assets/a3a845c9-33a7-47c6-a007-c4d8f6fe4401)
![Goal-Based Nutrition](https://github.com/user-attachments/assets/7c1faefb-7bc7-4884-8696-23d7d0d78499)
![Goal-Based Nutrition](https://github.com/user-attachments/assets/4ab0f5d0-703b-450c-b61a-a8a95165a9a3)

_Providing personalized meal suggestions for specific goals like muscle gain or weight loss._

### 5. **Interactive Chatbot** 🤖
![Chatbot](https://github.com/user-attachments/assets/41df0aef-b9d0-4145-887a-cf5efd713178)
![Chatbot](https://github.com/user-attachments/assets/4545b312-6b95-44c3-b40d-0bfd452e1a47)

_An interactive chatbot that guides users through meal planning and answers dietary questions in real time._

---

*Note: Screenshots above are for demo purposes. Actual user experience may vary based on input preferences and goals.*

## Acknowledgments 🙌

This project was created under the mentorship of **Austin Odera**. Their guidance has been crucial in the development of this application. 🙏

### 👨‍💻 **Contributors**:

- **James Otieno** - [@jayotieno](https://github.com/jayotieno)
- **Yanet Niguse** - [@yanetniguse](https://github.com/yanetniguse)
- **Dhruv Pokhariyal** - [@P0lcahontas](https://github.com/P0lcahontas)
- **Kwame Lucheveli** - [@luche3002](https://github.com/luche3002)

---

## Technology Stack 💻

- **Backend**: **Flask** for the web framework
- **Frontend**: **HTML** and **CSS**
- **AI & Logic**: Custom **rules engine** for dynamic meal generation

---

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Conclusion 🌟

The **Smart Meal Planner** offers a **holistic approach** to meal planning, focusing on health, wellness, and personalized nutrition. By combining the latest technologies and a user-centered design, it provides a solution that stands out from the crowd, empowering users to make healthier decisions that align with their unique needs. 

```
