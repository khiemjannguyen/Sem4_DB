<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Amazon Scraper</h3>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project
This project is an assignment for the database lecture in the 4th semester IT-Automotive at the DHBW Stuttgart.\
The Amazon Scraper is a tool which helps you to track the price of your next possible Amazon purchase. If you are planning to buy a product on Amazon, but the price seems to expensive, the Amazon Scraper will help you! All you have to do is to specify the Amazon-URL, your desired price and your email. The Amazon Scraper will track the price of the given product and will notify your email, when the price drops to your desired price.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The Amazon Scraper needs the Google Chrome Web Browser on your machine to run. [Here](https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQjw4v2EBhCtARIsACan3nz6dkC9Z2wt1t7aMX1zI67pYvRWkZMIsn-BZ63UmzKfNp96wCwVJngaAhsfEALw_wcB&gclsrc=aw.ds) you can install Google Chrome.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/khiemjannguyen/Sem4_DB.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```


<!-- USAGE EXAMPLES -->
## Usage

### Navigate to scraper
Open your folder, where you cloned the repository and navigate to scraper:
   ```sh
   cd ./scraper
   ```

### Docker run InfluxDB
Start InfluxDB with Docker:
   ```sh
   bash start_InfluxDB.sh
   ```

### Run Amazon Scraper
1. Run the Amazon Scraper:
   ```sh
   python main.py
   ```
2. Enter the Amazon-URL:
    ```sh
    Please paste URL of Amazon Product URL: 
    ```
3. Enter your desired price:
    ```sh
    Please enter Wish Price [xx.xx]:
    ```  
4. Enter your email:
    ```sh
    Please enter your E-Mail: 
    ```
5. If you want to watch the current price course in InfluxDB enter "True". It will automatically open the InfluxDB UI in your Chrome Web Browser:
    ```sh
    Open InfluxDB GUI to see Price Chart [True||False]:  
    ```

## Testing
### Navigate to scraper
Open your folder, where you cloned the repository and navigate to scraper:
   ```sh
   cd ./scraper
   ```
### Run Unittest
   ```sh
   bash run_tests.sh
   ```

## BUG FIX
When "UnicodeEncodeError: 'ascii' codec can't encode character 'something e.g:"\xc5"' in position 398: ordinal not in range(128)" occurs:
1. open 'opt/anaconda3/lib/python3.8/smtplib.py", line 859'
   ```
   msg = _fix_eols(msg).encode('ascii')
   ```
1. change 'opt/anaconda3/lib/python3.8/smtplib.py", line 859' to
   ```
   msg = _fix_eols(msg).encode('utf-8')
   ```





