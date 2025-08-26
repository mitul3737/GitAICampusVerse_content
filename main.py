# Create an Employee class with name, age and salary attributes 
import pandas as pd

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
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 18:
            raise ValueError("Age must be at least 18")
        if value > 100:
            raise ValueError("Age must be reasonable (<= 100)")
        self._age = value

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary must be positive")
        self._salary = float(value)
    
    def process_stock_data(self, data: pd.DataFrame) -> pd.DataFrame:
        if data.empty:
            raise ValueError("DataFrame cannot be empty")
        
        if 'Close' not in data.columns:
            raise ValueError("DataFrame must contain 'Close' column")

        # calculate moving averages
        data['SMA_50'] = data['Close'].rolling(window=50).mean()
        data['SMA_200'] = data['Close'].rolling(window=200).mean()

        # calculate volatility
        data['daily_return'] = data['Close'].pct_change()
        data['volatility'] = data['daily_return'].rolling(window=21).std()

        # generate trading signals
        data['signals'] = 0
        data.loc[data['SMA_50'] > data['SMA_200'], 'signals'] = 1
        data.loc[data['SMA_50'] < data['SMA_200'], 'signals'] = -1

        return data

# Create an employee instance and print the name, age and salary
if __name__ == "__main__":
    employee = Employee("John Doe", 30, 50000.0)
    print(employee.name)
    print(employee.age)
    print(employee.salary)