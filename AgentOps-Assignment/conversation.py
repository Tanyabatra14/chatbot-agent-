from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


OUTLET_DATA = {
    "delhi": {
        "timings": {
            "weekdays": {
                "lunch": "12:00 PM - 3:00 PM",
                "dinner": "7:00 PM - 11:00 PM"
            },
            "sunday": {
                "lunch": "12:30 PM - 4:00 PM"
            }
        }
    },
    "bangalore": {
        "timings": {
            "weekdays": {
                "lunch": "12:00 PM - 3:30 PM",
                "dinner": "7:00 PM - 10:30 PM"
            },
            "sunday": {
                "lunch": "12:00 PM - 4:00 PM"
            }
        }
    }
}

@app.get("/api/location")
def get_location(city: str):
    city = city.lower()
    if city in OUTLET_DATA:
        return OUTLET_DATA[city]
    return JSONResponse(content={"error": "Location not found"}, status_code=404)

@app.get("/api/menu")
def get_menu(type: str):
    MENU = {
        "lunch": ["BBQ Chicken", "Paneer Tikka", "Biryani"],
        "dinner": ["Grilled Fish", "Dal Makhani", "Butter Naan"]
    }
    if type in MENU:
        return {"items": MENU[type]}
    return JSONResponse(content={"error": "Menu type not found"}, status_code=404)