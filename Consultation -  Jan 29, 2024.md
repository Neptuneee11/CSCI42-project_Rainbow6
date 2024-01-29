Bike stations around ateneo

* keeping track of each people and bikes
* qr code for each bike
* Each station has its own locations
* Bikes can be taken and returned to a station
* Time will only be measured when the bike is parked at a station
* Transaction details will include Customer info, bike borrowed, location borrowed, time returned, location returned.
* ateneo ID e wallets could be integrated
* GPS data nice to have not a req
## software side requirements

Django

## Minimum viable product

Keep track of customers and the bike, most important
#### Authentication
Pwedeng django. It has built in login logout.
* log in 
* log out
* registration
	* due diligence
#### Customer DB
wag na sqlite
pwedeng SQL if deployed to a live environment

#### Deployment
up to you how far you want it

#### The bikes
purchased in bulk as an organization. User lent bikes will be for later if may oras pa.

##### securing the bikes problem
We can get away with combination locks. Once the qr code gets scanned and linked with user ID, it reveals the combination in the app.
let's put aside the security for now.

> No need to account for malicious players for now. 
#### Renting process
meron na. will do later


#### Software requirements
Library to access **cameras** for qr code scanning
Library for qr code
JavaScript for this
REST API for the frontend
REST framework for the backend (django)
	builds on top of the views
FrontEnd

#### Deployment
Pack it up in Docker
make an image
for ease of deployment

#### Make hats
roles for each features
Hopefully by the end of the day or tomorrow morning

GPS is not something we should worry about. Pwede naman pero kaya naman pag wala. Figure it out.

#### Chat log

![consultation1](/attachments/consultation_chat_1.png)