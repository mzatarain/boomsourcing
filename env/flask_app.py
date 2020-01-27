from flask import Flask,jsonify, request

app = Flask(__name__)

#This is just a test API
@app.route('/', methods=['GET','POST'])
def index():
     if(request.method == 'POST'):
          some_json = request.get_json()
          return jsonify({'you sent': some_json}), 201
     else:
          return jsonify({"about":"Test API!"})

#Task 1
# Write an API that get the location of each number from a CSV file using Libphone numbers library.
# We provide the numbers.csv in this repo, please generate and output.csv and include it in your solution.
#Create API
@app.route('/numbers_location/',methods = ['GET'])
#Define method numbers_location
def numbers_location():
     #Import required modules
     import phonenumbers, csv
     from phonenumbers import geocoder
     #Start try-catch statement
     try:
          #Open file numbers.csv and store values in a list
          with open('./numbers.csv', newline='') as csvfile:
               data = list(csv.reader(csvfile))
          with open('./output.csv', 'w', newline='') as csvfile:
               fieldnames = ['phone_number', 'is_valid','location']
               writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
               writer.writeheader()
               
               #Run a loop of numbers list starting at position 1 to avoid the first value of the list(The title "numbers"), which is not a phone number
               for x in data[1:]:
                    #Convert objects into strings to allow phonenumbers.parse method to parse the numbers in a valid format.
                    x = ''.join(x)
                    #Parse phone numbers
                    number = phonenumbers.parse(x, "US")
                    #Get location, phone number in international format and check if the phone number is valid
                    isValid = phonenumbers.is_valid_number(number)
                    location = geocoder.description_for_number(number, "en")
                    phonenumber = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                    #Print values in console
                    print(phonenumber)
                    print(isValid)
                    print(location)
                    writer.writerow({'phone_number': phonenumber, 'is_valid': isValid, 'location': location})         
          #Return successful message.
          return 'Output.csv file was generated correctly'
     except phonenumbers.NumberParseException as e:
          #Print exception message
          return "Exeption message: " + str(e)

#Task 2
# Write an API that get a closest phone number based on another phone number
@app.route('/locate_numbers/<string:number>',methods = ['GET'])
def locate_numbers(number):
     import phonenumbers, csv
     from phonenumbers import geocoder  
     try:
          ClosestNumber = ''
          ClosestLocation = ''
          x = phonenumbers.parse(number, None)
          n = phonenumbers.format_number(x, "US")
          isValid = phonenumbers.is_valid_number(x)
          #print(isValid)
          if isValid == True:
               location = geocoder.description_for_number(x, "en")
               #print(location)
               with open('./numbers.csv', newline='') as csvfile:
                    data = list(csv.reader(csvfile))
                    #print(data)
                    for y in data[1:]:
                         y = ''.join(y)
                         #print(y)
                         numberToCompare = phonenumbers.parse(y, "US")
                         #print(numberToCompare)
                         isValidToCompare = phonenumbers.is_valid_number(numberToCompare)
                         #print(isValidToCompare)
                         if isValidToCompare == True:
                              locationToCompare = geocoder.description_for_number(numberToCompare, "en")
                              if location is locationToCompare:
                                   ClosestNumberFormated = phonenumbers.format_number(numberToCompare, "US")
                                   ClosestNumber = str(ClosestNumberFormated)
                                   ClosestLocation = str(locationToCompare)                                   
          else:
               return 'Please provide a valid phone number'
          return jsonify({'Provided Number': str(n),'Provided Number Location':str(location),'Closest Number': ClosestNumber, 'Closest Location': ClosestLocation})
     except phonenumbers.NumberParseException as e:
          #Print exception message
          return "Exeption message: " + str(e)

if __name__ == '__main__' :
     app.run(debug=True, host='0.0.0.0')