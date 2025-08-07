#working with api's
#a weather api app
# api key 5a6f6e2c3efc7757d2356aaf9529b3f1
import sys
import requests
from  PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.tempreture = QLabel(self)
        self.emoji = QLabel( self)
        self.description = QLabel( self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("weather app")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.tempreture)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description)


        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.tempreture.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.tempreture.setObjectName("Tempreture")
        self.emoji.setObjectName("Emoji")
        self.description.setObjectName("Description")

        self.setStyleSheet("""
        QLabel, QpushButton{
                           font-family: calibri;
                           } 


        QLabel#Tempreture{
                           font-size: 30px; }
        QLabel#Description{
                           font-size: 40px; }
        QLabel#Emoji{
                           font-size: 40px; 
                           font-family: segoe UI emoji;}
        QLabel#city_label{
                           font-size: 40px;
                           font-style: Italic;}
        QLineEdit#city_input{
                           font-size: 40px;}
        QPushButton#get_weather_button{
                           font-size: 30px;
                           font-weight: bold;}

                           """)
        

        self.get_weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        api_key = "5a6f6e2c3efc7757d2356aaf9529b3f1"

        city = self.city_input.text()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try: 

            response = requests.get(url)
            response.raise_for_status()

            data = response.json()


            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPls check your input")
                case 401:
                    self.display_error("Unauthorized \nInvalid API")
                case 403:
                    self.display_error("Forbidden\nAccess Denied")
                case 404:
                    self.display_error("Not Found\ncity not found")
                case 500:
                    self.display_error("Internal Server Error\nPls try again later")
                case 502:
                    self.display_error("Bad Gateway\nInvalid Response From Server")
                case 503:
                    self.display_error("Service Unavliable\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout\nNo Response from the Server")
                case _:
                    self.display_error(f"HTTP Error\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nCheck Your internet")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirections:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request ERror:\n{req_error}")
            
    def display_error(self, message):
        self.tempreture.setText(message) 
    def display_weather(self, data):
        temprature_K = data["main"]["temp"]
        temprature_c = temprature_K - 273.15
        temprature_f = (temprature_K * 9/5) - 459.67
        weather_description = data["weather"][0]["description"]

        self.tempreture.setText(f"{temprature_f:.0f}\u00B0F")
        self.description.setText(weather_description)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    WeatherApp = WeatherApp()
    WeatherApp.show()
    sys.exit(app.exec_())