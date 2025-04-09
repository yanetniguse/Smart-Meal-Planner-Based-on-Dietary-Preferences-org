function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value) / 100; // Convert cm to meters

    if (!weight || !height) {
        alert("Please enter weight and height to calculate BMI.");
        return;
    }

    // BMI Formula: weight (kg) / (height (m) * height (m))
    const bmi = (weight / (height * height)).toFixed(1);
    let status = "";
    
    if (bmi < 18.5) {
        status = "Underweight";
    } else if (bmi >= 18.5 && bmi <= 24.9) {
        status = "Healthy Weight";
    } else if (bmi >= 25 && bmi <= 29.9) {
        status = "Overweight";
    } else {
        status = "Obese";
    }

    // Display BMI Result
    document.getElementById('bmi-result').innerHTML = `Your BMI: <strong>${bmi}</strong> (${status})`;

    // Send BMI data to Flask for recommendations
    fetch('/recommendations', {
        method: 'POST',
        body: JSON.stringify({ bmi: bmi, status: status }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('recommendation-output').innerHTML = `<strong>Recommended Daily Calorie Intake:</strong> ${data.calories} kcal/day<br>
        <strong>Suggested Foods:</strong> ${data.foods}`;
    });
}
