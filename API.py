import requests

def headerHTML():
        myfile = open("API.html","w")
        myfile.write("<!DOCTYPE html>")
        myfile.write("<head>")
        myfile.write("<link rel='stylesheet' type='text/css' href='API.css'>")
        myfile.write("</head>")
        myfile.close()

def topcontainerHTML():
        myfile = open("API.html","a")
        myfile.write("<div class=\"top-container\">")
        myfile.write("<div id=\"example1\">")
        myfile.write("<h1><font face= \"verdana\" size=\"10\" color=\"white\"><center>Your City's Environmental Data</center></font></h1>")
        myfile.write("</div>")
        myfile.write("</div>")
        myfile.close()

def sidenavHTML():
        myfile = open("API.html","a")
        myfile.write("<body>")
        myfile.write("<div id=\"main\">")
        myfile.write("<font face = \"verdana\" size=\"3\"><span style=\"font-size:30px;cursor:pointer\" onclick=\"openNav()\">&#9776; About</font></span>")
        myfile.write("</div>")
        myfile.write("<a href=\"javascript:void(0)\" class=\"closebtn\" onclick=\"closeNav()\">&times;</a>")
        myfile.write("<a href=\"#\">About</a>")
        myfile.write("<a href=\"#\">Definitions</a>")
        myfile.write("<a href=\"#\">Contact</a>")
        myfile.write("</div>")
        myfile.write("</body>")
        myfile.close()

def formatingHTML():
        myfile = open("API.html","a")
        myfile.write("<p>")
        myfile.write("</p>")
        myfile.write("<hr>")
        myfile.close()

def scriptHTML():
        myfile = open("API.html","a")
        myfile.write("<script>")
        myfile.write("function openNav() {document.getElementById('mySidenav').style.width = '250px';}")
        myfile.write("function closeNav() {document.getElementById('mySidenav').style.width = '0';}")
        myfile.write("</script>")
        myfile.close()

def closeHTML():
        myfile = open("API.html","a")
        myfile.write("</body>")
        myfile.write("</head>")
        myfile.close()

def writeHTML(sunrise):
        myfile = open("API.html","a")
        myfile.write("<p>\"+sunrise+\"</p>")
        myfile.close()


def main():
        response = requests.get("https://api.ipgeolocation.io/astronomy?apiKey=7dd2a9a9007443a993d63c89761304d6")


        if (response.status_code == 200):
                data = response.content 

                datajson = response.json()
                sunrise = datajson['sunrise']
                sunset = datajson['sunset']
                date = datajson ['date']
                city = datajson['location']['city']
                print ("Your City: "+city)
                print("Current Date: "+date)
                print("Sunrise: "+sunrise+" a.m.")
                print("Sunset: "+ sunset)


        else:
                data = "Error has occured"
                writeHTML(data)

headerHTML()
topcontainerHTML()
sidenavHTML()
formatingHTML()
scriptHTML()
closeHTML()
main()
