import random
from datetime import datetime, timedelta

def generate_flights():
    operators = [
        {
            "name": "Global Airways",
            "start": datetime(2000, 1, 2),
            "end": datetime(2005, 6, 9),
            "routes": [("LHR", "JFK"), ("JFK", "LHR"), ("LHR", "DXB"), ("DXB", "LHR"), ("LHR", "SIN"), ("SIN", "LHR")],
            "color": "#3366cc",
            "count": 150
        },
        {
            "name": "EuroFly",
            "start": datetime(2005, 8, 11),
            "end": datetime(2012, 9, 11),
            "routes": [("LHR", "CDG"), ("CDG", "LHR"), ("LHR", "AMS"), ("AMS", "LHR"), ("LHR", "FRA"), ("FRA", "LHR"), ("LHR", "MAD"), ("MAD", "LHR")],
            "color": "#109618",
            "count": 200
        },
        {
            "name": "SwiftCargo",
            "start": datetime(2013, 3, 21),
            "end": datetime(2020, 10, 9),
            "routes": [("HKG", "SIN"), ("SIN", "HKG"), ("HKG", "NRT"), ("NRT", "HKG"), ("HKG", "PVG"), ("PVG", "HKG"), ("HKG", "SYD"), ("SYD", "HKG")],
            "color": "#316395",
            "count": 250
        },
        {
            "name": "Global Logistics",
            "start": datetime(2020, 11, 21),
            "end": datetime(2023, 12, 31),
            "routes": [("HKG", "LHR"), ("LHR", "HKG"), ("HKG", "LAX"), ("LAX", "HKG"), ("HKG", "FRA"), ("FRA", "HKG")],
            "color": "#0099c6",
            "count": 150
        }
    ]

    events = []
    for op in operators:
        current_time = op["start"]
        for _ in range(op["count"]):
            # Random gap between flights (12 to 48 hours)
            gap = timedelta(hours=random.uniform(12, 48))
            current_time += gap
            
            if current_time > op["end"]:
                break
                
            # Random flight duration (1.5 to 3.5 hours)
            duration = timedelta(hours=random.uniform(1.5, 3.5))
            end_time = current_time + duration
            
            if end_time > op["end"]:
                break
                
            route = random.choice(op["routes"])
            title = f"Flight: {route[0]} - {route[1]}"
            
            start_str = current_time.strftime("%b %d %Y %H:%M:%S GMT")
            end_str = end_time.strftime("%b %d %Y %H:%M:%S GMT")
            
            event = f'    <event start="{start_str}" end="{end_str}" title="{title}" color="{op["color"]}">\n'
            event += f'        Scheduled flight from {route[0]} to {route[1]} by {op["name"]}.\n'
            event += '    </event>'
            events.append(event)
            
            current_time = end_time

    return "\n".join(events)

if __name__ == "__main__":
    flights_xml = generate_flights()
    with open("flights_fragment.xml", "w") as f:
        f.write(flights_xml)
    print(f"Generated {len(flights_xml.split('</event>')) - 1} flights.")
