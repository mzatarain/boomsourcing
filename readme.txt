This project was created in Ununtu 18 OS by Manuel Rodriguez Zatarain, to execute it please follow below instructions:

Open up a terminal inside the Boomsourcing folder and create a docker image of the proyect with the follow command line: 
	sudo docker build --tag boomsourcing-python-app .

create the container by running the image with below command line:
	sudo docker run --name boomsourcing -p 5000:5000 boomsourcing-python-app

after run the container you should be able to access via web browser or by a curl command

go to your browser and type:


Task 1. Generate an output.csv file from given numbers.csv:
	http://0.0.0.0:5000/numbers_location/
	-This will generate the output.csv file within the container. To access this file open up another terminal and type below commands:
	 
		sudo docker exec -it boomsourcing /bin/sh
		cat output.csv

	-All phone numbers and its locations will be also printed in the terminal

Task 2. Find closest number:
	http://0.0.0.0:5000/locate_numbers/{Type a valid number here}
	example:	
	http://0.0.0.0:5000/locate_numbers/+1 978-877-2197
	-This method compare given number with all valid phone numbers in the numbers.csv file.
	-Remember to use a phone number not included in that list or you will get the same number as a result.
	-optional valid phone numbers:
		+1 213-416-2510
		+1 571-418-3610
		+1 407-809-2009

Notes:
	I set http://0.0.0.0/5000 ip and port to avoid conflicts at another computer which may have http://127.0.0.1:5000 ip in use 

