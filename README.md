# Smart Home Electricity Usage Estimator

The **Smart Home Electricity Usage Estimator** is a beginner friendly Python project designed to help users understand how much electricity their household appliances consume. By entering the power rating and daily usage of each appliance, this tool calculates energy consumption, estimates monthly electricity bills, identifies high consumption devices, and encourages energy saving habits. The project is simple, practical, and perfect for students, hobbyists, and anyone who wants better control over their electricity usage.

---

##  Key Features

- Add any number of home appliances
- Input power rating (in watts) and daily usage (hours)
- Automatically calculates:
  - Daily electricity usage (kWh)
  - Monthly consumption (kWh × 30 days)
  - Estimated electricity bill (₹)
- Identifies the appliance that consumes the most energy
- Clean, menu based interactive system
- Beginner friendly code with clear structure
- No external dependencies — runs using core Python only

---

##  Why This Project?

Electricity bills can be confusing, and most households don’t know which appliances consume the most power.  
This project solves that by providing:

- Simple & accurate consumption estimates  
- Awareness about high energy devices  
- A tool to track electricity usage  
- A practical real world mini project ideal for college submissions  

This is not just an assignment level project — it is actually useful in real life.

---

##  Project Structure

Smart-Electricity-Estimator/
electricity_estimator.py
README.md

**electricity_estimator.py**  
The main program that performs all calculations and provides the menu interface.

**sample_appliances.txt**  
Optional file to store appliance lists.

---

##  How the Program Works

### 1. User Inputs
- Appliance Name  
- Power Rating (W)  
- Daily Usage (hours)  
- Electricity Rate (₹ per kWh)

### 2. Calculations Performed

Formula used: Daily Energy (kWh) = (Watt × Hours) / 1000
Then:Monthly Consumption = Daily Energy × 30
Estimated Bill = Monthly Consumption × Electricity Rate

### 3. Output Provided

- Total daily consumption  
- Total monthly consumption  
- Estimated monthly bill  
- Highest consuming appliance (with exact kWh usage)

---

## Example Usage

Enter appliance name: Fan
Power rating (W): 75
Daily usage (hours): 8

Enter appliance name: Refrigerator
Power rating (W): 150
Daily usage (hours): 24

Enter electricity rate (₹ per kWh): 8

Program Output:
Total daily consumption: 4.2 kWh
Total monthly consumption: 126 kWh
Estimated monthly bill: ₹1008
Highest consuming appliance: Refrigerator (108 kWh/month)

## Code Overview 

•	Appliance Class
Stores name, wattage, hours used, and auto calculates energy.
	•	Main Menu Loop
Allows adding appliances, viewing summary, and generating reports.
	•	Summary Function
Displays total usage and highest consuming appliance.
	•	Bill Estimation Function
Takes electricity rate and calculates final cost.


## Real-World Use Cases
•	Helps families track energy usage
•	Useful for hostel rooms to avoid bill surprises
•	Students can use it to understand electricity consumption concepts
•	Can be extended into a complete smart home dashboard in the future


## Contribution Guide

Contributions are welcome!
	1.	Fork the repository
	2.	Create a new branch
	3.	Push improvements
	4.	Submit a Pull Request


