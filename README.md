# Currency Hystory REST-API, JSON (Django)

The code works in following way:   

- The task is started by running the server , for the test server run enter the command: 
```bash
python manage.py runserver
```
- The results of the program can be viewed in the web browser at address
```bash
http://127.0.0.1:8000/ get-current-usd/
```
- When accessing the server via web browser , following actions run:
- Currency exchange rate data from http://apilayer.net/ is requested and written to the database, 
the console displays the message :
```bash
request for new rate
```
- If less than 10 seconds have passed since the last request, 
the data is not requested, but the records from the database are output, and the console displays the following message
```bash
Use recorded data
```
- The free subscriber profile at http://apilayer.net/ is used during the requests, 
therefore the number of requests is limited to 100 requests per month.
- Currency exchange rate records are stored in the database in the form of:
  - Rate.id - record identifier  
  - Rate.daytime - request time  
  - Rate.currensy - currency type  
  - Rate.rate - currency rate
- The database used is sqlite3, but another SQL database can be used.
- The database stores the last 15 values of the currency rate, 
when creating a new currency rate record, if there are more than 15 records, 
the oldest record is deleted (this functionality can be customized or disabled). 
When deleting the oldest record, the console displays the message
```bash
Item with oldest_rate.id=1 deleted
```
- When requesting web browser at http://127.0.0.1:8000/ get-current-usd/, the terminal displays a list of 10 records of the latest currency rate records in JSON format.
