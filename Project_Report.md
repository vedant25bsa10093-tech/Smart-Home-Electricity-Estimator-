# 5. `Project_Report.md` (formal report for submission)

 ⁠markdown
# Project Report — Smart Home Electricity Usage Estimator

## 1. Problem Definition
Many households receive monthly electricity bills without understanding which appliances contribute most to the usage and how daily habits influence the bill. This project provides a lightweight estimator to raise awareness and help users reduce costs.

## 2. Objectives
 1.⁠ ⁠Calculate per-appliance and total monthly energy consumption (kWh).
 2.⁠ ⁠Estimate monthly electricity bill using a user-specified rate.
 3.⁠ ⁠Identify top-consuming appliances and give simple suggestions.
 4.⁠ ⁠Provide save/load and report export functionality.

## 3. Scope and Limitations
*Scope:* Home users who can enter appliance wattage and estimated daily usage. No real-time monitoring or hardware integration.

*Limitations:* Accuracy depends on user-provided data (estimated hours). Does not interface with smart meters.

## 4. System Design
### High-level modules
•⁠  ⁠*Data model:* ⁠ Appliance ⁠ (name, watt, hours/day)
•⁠  ⁠*Estimator logic:* computations for kWh and cost
•⁠  ⁠*Persistence:* JSON save/load
•⁠  ⁠*Interface:* Console-based menu
•⁠  ⁠*Reporting:* Plain-text report export

### Data structures
•⁠  ⁠List of ⁠ Appliance ⁠ objects
•⁠  ⁠JSON file for persistence

## 5. Algorithm & Pseudocode
*Monthly kWh per appliance* = (watt * hours_per_day * 30) / 1000

Pseudocode (summary):
•⁠  ⁠Start program
•⁠  ⁠Load saved appliance list (if exists)
•⁠  ⁠Show menu to user
•⁠  ⁠If user adds appliance → append to list
•⁠  ⁠If user requests summary → compute total_kwh and bill
•⁠  ⁠If user saves → write JSON
•⁠  ⁠If user exports report → write plain text

## 6. Implementation Details
Language: Python 3 (no external packages)
Main file: ⁠ electricity_estimator.py ⁠

Key functions:
•⁠  ⁠⁠ Appliance.monthly_kwh() ⁠ → compute kWh
•⁠  ⁠⁠ Estimator.total_monthly_kwh() ⁠ → sum of appliances
•⁠  ⁠⁠ Estimator.bill_estimate(rate) ⁠ → multiply total by rate
•⁠  ⁠⁠ Estimator.save() ⁠ / ⁠ load() ⁠ → JSON persistence

## 7. Testing
### Test cases
 1.⁠ ⁠*Single appliance* — 75W, 10 h/day, rate ₹8
   - Expected monthly kWh: 22.5
   - Expected bill: ₹180
 2.⁠ ⁠*Multiple appliances* — fridge, fan, LED bulb
   - Validate percentages sum to ~100%
 3.⁠ ⁠*Empty data* — try summary → prompt to add appliances

### Edge cases
•⁠  ⁠Non-numeric input handled by prompting again
•⁠  ⁠Removing nonexistent appliance returns "Not found"

## 8. Usage guide
 1.⁠ ⁠Run ⁠ python3 electricity_estimator.py ⁠
 2.⁠ ⁠Use menu options to add appliances and estimate bills
 3.⁠ ⁠Save data to ⁠ appliances.json ⁠ for later reuse
 4.⁠ ⁠Export a report for submission or sharing

## 9. Future Work
•⁠  ⁠Add CSV export and simple plotting (matplotlib)
•⁠  ⁠Add household profiles (multiple rooms)
•⁠  ⁠Integrate with a smart meter API for real-time data
•⁠  ⁠Add tariff slabs and time-of-use rates

## 10. Conclusion
This project provides a simple yet practical tool for everyday users to estimate electricity consumption and make better decisions to reduce bills. It demonstrates the application of basic programming concepts—data structures, file I/O, modularization, and arithmetic computations—towards a real-world problem.
