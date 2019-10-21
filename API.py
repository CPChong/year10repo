import requests
from tkinter import *
from PIL import ImageTk,Image
import webbrowser

def headerHTML():
        myfile = open("API.html","w")
        myfile.write("<!DOCTYPE html>")
        myfile.write("<head>")
        myfile.write("<title> Environmental Data </title>")
        myfile.write("<link rel='stylesheet' type='text/css' href='API.css'>")
        myfile.write("<link rel='icon' href='sunrise-icon.png' type='image/gif' sizes='16x16'>")
        myfile.write("</head>")
        myfile.close()

def topcontainerHTML():
        myfile = open("API.html","a")
        myfile.write("<div class='top-container'>")
        myfile.write("<div id='example1'>")
        myfile.write("<h1><font face= 'verdana' size='10' color='#C4C8F9'><center>Your City's Environmental Data</center></font></h1>")
        myfile.write("</div>")
        myfile.write("</div>")
        myfile.close()

def sidenavHTML():
        myfile = open("API.html","a")
        myfile.write("<body>")
        myfile.write("<div id='mySidenav' class='sidenav'>")
        myfile.write("<a href='javascript:void(0)' class='closebtn' onclick='closeNav()'>&times;</a>")
        myfile.write("<a href='file:///Users/christopher.chong/Documents/Design/API.html'>Home</a>")
        myfile.write("<a href='file:///Users/christopher.chong/Documents/Design/Definitions.html' target='_blank'>Definitions</a>")
        myfile.write("</div>")
        myfile.write("<div id='main'>")
        myfile.write("<span style='font-size:30px;cursor:pointer' onclick='openNav()'> &#9776; More</span>")
        myfile.write("</div>")
        myfile.write("</body>")
        myfile.close()

def scriptHTML():
        myfile = open("API.html","a")
        myfile.write("<script>")
        myfile.write("function openNav() {document.getElementById('mySidenav').style.width = '250px';document.getElementById('main').style.marginLeft = '250px';document.body.style.backgroundColor = 'rgba(0,0,0,0.4)';}")
        myfile.write("function closeNav() {document.getElementById('mySidenav').style.width = '0';document.getElementById('main').style.marginLeft= '0';document.body.style.backgroundColor = 'white';}")
        myfile.write("</script>")
        myfile.close()

def closeHTML():
        myfile = open("API.html","a")
        myfile.write("</body>")
        myfile.write("<hr></hr>")
        myfile.write("</head>")
        myfile.close()

def locationdateHTML(country, province, city, longitude, latitude, date):
        myfile = open("API.html","a")
        myfile.write("<body>")
        myfile.write("<div id='main'>")
        myfile.write(f"<p><b><font face= 'arial' size='4'> Location:</font></b><td> {country}, {province}, {city}</td></p>")
        myfile.write(f"<p><b><font face= 'arial' size='4'> Longitude and Latitude:</font></b><td> {longitude}, {latitude}</td></p>")
        myfile.write(f"<p><b><font face= 'arial' size='4'> Date:</font></b><td> {date}</td></p>")
        myfile.write("</div>")
        myfile.write("</body>")


def suntableHTML(sunrise, sunset, solarnoon, daylength, sunaltitude, sundistance, sunazimuth):
        myfile = open("API.html","a")
        myfile.write("<table>")
        myfile.write("<tr>")
        myfile.write("<th>Environmental Data</th>")
        myfile.write("<th>Data</th>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Sunrise Time</td>")
        myfile.write(f"<td>{sunrise} a.m.</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Sunset Time</td>")
        myfile.write(f"<td>{sunset} p.m.</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Solar Noon</td>")
        myfile.write(f"<td>{solarnoon} p.m.</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Day Length</td>")
        myfile.write(f"<td>{daylength} hours</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Sun Altitude</td>")
        myfile.write(f"<td>{sunaltitude}</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Sun Distance</td>")
        myfile.write(f"<td>{sundistance} meters</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Sun Azimuth</td>")
        myfile.write(f"<td>{sunazimuth}</td>")
        myfile.write("</tr>")
        myfile.write("</table>")
        myfile.close()

def moontableHTML(moonrise, moonset, moonaltitude, moondistance, moonazimuth, moonparallacticangle):
        myfile = open("API.html","a")
        myfile.write("<table>")
        myfile.write("<tr>")
        myfile.write("<td>Moon Rise</td>")
        myfile.write(f"<td>{moonrise} p.m.</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Moon Set</td>")
        myfile.write(f"<td>{moonset} p.m.</td>")
        myfile.write("</tr>")
        myfile.write("<tr>")

        myfile.write("<td>Moon Alitude</td>")
        myfile.write(f"<td>{moonaltitude}</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Moon Distance</td>")
        myfile.write(f"<td>{moondistance} meters</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Moon Azimuth</td>")
        myfile.write(f"<td>{moonazimuth}</td>")
        myfile.write("</tr>")

        myfile.write("<tr>")
        myfile.write("<td>Moon Parallactic Angle</td>")
        myfile.write(f"<td>{moonparallacticangle}</td>")
        myfile.write("</tr>")
        myfile.write("</table>")
        myfile.close()
        

def main():

        response = requests.get("https://api.ipgeolocation.io/astronomy?apiKey=7dd2a9a9007443a993d63c89761304d6")
        if (response.status_code == 200):
                data = response.content 

                datajson = response.json()
                sunrise = datajson['sunrise']
                sunset = datajson['sunset']
                solarnoon = datajson ['solar_noon']
                daylength = datajson['day_length']
                sunaltitude = datajson ['sun_altitude']
                sundistance = datajson ['sun_distance']
                sunazimuth = datajson ['sun_azimuth']
                moonrise = datajson['moonrise']
                moonset = datajson['moonset']
                moonaltitude = datajson ['moon_altitude']
                moondistance = datajson ['moon_distance']
                moonazimuth = datajson ['moon_azimuth']
                moonparallacticangle = datajson ['moon_parallactic_angle']

                date = datajson ['date']
                country = datajson['location']['country_name']
                province = datajson['location']['state_prov']
                city = datajson['location']['city']
                longitutde = datajson ['location']['longitude']
                latitude = datajson ['location']['latitude']

                print("Sucess!")
                print("Example data:")
                print("Your City: "+city)
                print("Current Date: "+date)
                print("Sunrise: "+sunrise+" a.m.")
                print("Sunset: "+ sunset+" p.m.")

                headerHTML()
                topcontainerHTML()
                sidenavHTML()
                scriptHTML()
                closeHTML()
                locationdateHTML (country, province, city, longitutde, latitude, date)
                suntableHTML(sunrise, sunset, solarnoon, daylength, sunaltitude, sundistance, sunazimuth)
                moontableHTML(moonrise, moonset, moonaltitude, moondistance, moonazimuth, moonparallacticangle)

        else:
                data = "Error has occured" 
main()

def submit():
    webbrowser.open_new('file:///Users/christopher.chong/Documents/Design/API.html')


root = Tk()
root.geometry("400x250")


b1 = Button(root, text = "Click here to go to Environmental Data", command=submit)
b1.pack()



mainloop()