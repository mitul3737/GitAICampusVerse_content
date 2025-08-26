Fill the .github/copilot-instructions.md file

![alt text](image.png)

Then create a folder called main.py and  comment there.

![alt text](image-1.png)

2. Completition Panel
We can also use "Completition Panel"


![alt text](<WhatsApp Image 2025-08-26 at 11.48.12_cd5fb618.jpg>)
![alt text](<WhatsApp Image 2025-08-26 at 11.50.20_5165b7ab.jpg>)

3. For models, we can choose the models of our choice.


![alt text](image-2.png)

4. Comment driven one


#  create an Employee class with name, age and salary attributes 

#Include type hints and validation for each field 

`#  create an Employee class with name, age and salary attributes 

#Include type hints and validation for each field 
class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value`

You can now see these to be generated

![alt text](image-3.png)
Then add this comment

`Create an employee instance and print the name, age and salary`

Let's add one more method   for  processing stock data
`
#create a function that processes stock market data
    #calculate moving averages, volatility and trading signals
    #handle missing data and outliers
    def process_stock_data(self,data:pd.DataFrame) ->pd.DataFrame:

        #calculate moving averages
        data['SMA_50']= data['Close'].rolling(window=50).mean()
        data['SMA_200']= data['Close'].rolling(window=200).mean()

        #calculate volatility
        data['daily_return']= data['Close'].pct_change()
        data['volatility']= data['daily_return'].rolling(window=21).std()`
We will end up with this

![alt text](image-4.png)

Let's test the main.py file now using test_main.py

