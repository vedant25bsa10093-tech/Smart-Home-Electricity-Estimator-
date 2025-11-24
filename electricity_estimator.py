"""
Smart Home Electricity Usage Estimator
 
Features:
- Add / remove / list appliances (name, wattage, hours per day)
- Compute per-appliance kWh per month and cost
- Show total monthly consumption and bill
- Show percentage contribution and top consumers
- Save / load appliances to a JSON file
- Export a plain-text report

Author: VEDANT ANANDRAO SALUNKHE
Date: 22 NOV 2025
"""

from __future__ import annotations
import json
import os
from typing import Dict, List, Tuple

DATA_FILENAME = "appliances.json"
DAYS_IN_MONTH = 30

class Appliance:
    def __init__(self, name: str, watt: float, hours_per_day: float):
        self.name = name.strip()
        self.watt = float(watt)
        self.hours_per_day = float(hours_per_day)

    def monthly_kwh(self) -> float:
        # kWh = (Watt * hours/day * days) / 1000
        return (self.watt * self.hours_per_day * DAYS_IN_MONTH) / 1000.0

    def to_dict(self) -> Dict:
        return {"name": self.name, "watt": self.watt, "hours_per_day": self.hours_per_day}

    @staticmethod
    def from_dict(d: Dict) -> "Appliance":
        return Appliance(d["name"], d["watt"], d["hours_per_day"])


class Estimator:
    def __init__(self):
        self.appliances: List[Appliance] = []

    def add_appliance(self, name: str, watt: float, hours: float) -> None:
        self.appliances.append(Appliance(name, watt, hours))

    def remove_appliance(self, name: str) -> bool:
        name_low = name.strip().lower()
        for i, a in enumerate(self.appliances):
            if a.name.lower() == name_low:
                del self.appliances[i]
                return True
        return False

    def list_appliances(self) -> List[Dict]:
        return [a.to_dict() for a in self.appliances]

    def total_monthly_kwh(self) -> float:
        return sum(a.monthly_kwh() for a in self.appliances)

    def bill_estimate(self, rate_per_kwh: float) -> float:
        return self.total_monthly_kwh() * rate_per_kwh

    def appliance_contributions(self) -> List[Tuple[str, float, float]]:
        total = max(self.total_monthly_kwh(), 1e-9)
        items = []
        for a in self.appliances:
            kwh = a.monthly_kwh()
            pct = (kwh / total) * 100.0
            items.append((a.name, kwh, pct))
        items.sort(key=lambda x: x[1], reverse=True)
        return items

    def save(self, filename: str = DATA_FILENAME) -> None:
        data = [a.to_dict() for a in self.appliances]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self, filename: str = DATA_FILENAME) -> None:
        if not os.path.exists(filename):
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.appliances = [Appliance.from_dict(d) for d in data]

    def export_report(self, filename: str, rate_per_kwh: float) -> None:
        lines = []
        lines.append("Smart Home Electricity Usage Estimator — Report")
        lines.append("===============================================\n")
        lines.append(f"Total monthly consumption (kWh): {self.total_monthly_kwh():.2f}")
        lines.append(f"Estimated monthly bill: {self.bill_estimate(rate_per_kwh):.2f} (rate={rate_per_kwh}/kWh)\n")
        lines.append("Per-appliance breakdown:")
        for name, kwh, pct in self.appliance_contributions():
            lines.append(f"- {name}: {kwh:.2f} kWh ({pct:.1f}%)")
        lines.append("\nSuggestions:")
        # simple suggestions based on heuristics
        top_consumers = [name for name,_,_ in self.appliance_contributions()[:3]]
        if top_consumers:
            lines.append("Consider these to reduce consumption: " + ", ".join(top_consumers))
        else:
            lines.append("No appliances recorded.")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


def input_float(prompt: str, default: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            val = float(raw)
            return val
        except ValueError:
            print("Please enter a valid number.")


def main_menu():
    est = Estimator()
    est.load()
    print("\nSmart Home Electricity Usage Estimator\n---")

    while True:
        print("\nMenu:")
        print("1. Add appliance")
        print("2. Remove appliance")
        print("3. List appliances")
        print("4. Show summary & estimate bill")
        print("5. Save data")
        print("6. Load data")
        print("7. Export report")
        print("8. Exit")

        choice = input("Choose an option [1-8]: ").strip()
        if choice == "1":
            name = input("Appliance name (e.g., Fridge): ").strip()
            watt = input_float("Power rating (Watts): ")
            hours = input_float("Hours used per day (avg): ")
            est.add_appliance(name, watt, hours)
            print(f"Added {name} — {watt} W, {hours} h/day")

        elif choice == "2":
            name = input("Appliance name to remove: ").strip()
            ok = est.remove_appliance(name)
            print("Removed." if ok else "Not found.")

        elif choice == "3":
            items = est.list_appliances()
            if not items:
                print("No appliances recorded.")
            else:
                print("\nAppliances:")
                for it in items:
                    print(f"- {it['name']}: {it['watt']} W, {it['hours_per_day']} h/day")

        elif choice == "4":
            if not est.appliances:
                print("No appliances recorded. Add some first.")
                continue
            rate = input_float("Enter electricity rate per kWh (e.g., 8): ", default=8.0)
            total_kwh = est.total_monthly_kwh()
            bill = est.bill_estimate(rate)
            print(f"\nTotal monthly consumption: {total_kwh:.2f} kWh")
            print(f"Estimated monthly bill: {bill:.2f} (rate {rate}/kWh)\n")
            print("Breakdown (top first):")
            for name, kwh, pct in est.appliance_contributions():
                print(f"- {name}: {kwh:.2f} kWh ({pct:.1f}%)")

        elif choice == "5":
            est.save()
            print(f"Data saved to {DATA_FILENAME}")

        elif choice == "6":
            est.load()
            print("Data loaded.")

        elif choice == "7":
            if not est.appliances:
                print("No appliances recorded to export.")
                continue
            filename = input("Report filename (default: report.txt): ").strip() or "report.txt"
            rate = input_float("Enter electricity rate per kWh (e.g., 8): ", default=8.0)
            est.export_report(filename, rate)
            print(f"Report exported to {filename}")

        elif choice == "8":
            print("Exiting. Don't forget to save your data (option 5).")
            break

        else:
            print("Invalid option. Choose 1-8.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Bye.")
