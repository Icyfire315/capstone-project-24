# capstone-project-30
<sub>Level 1 Task 30</sub>

## Table of Contents

1. [Introduction](#intro)
2. [Project Description](#description)

   2.1. [How to run the program](#run)
  
3. [What I can do to improve the program](#changes)
4. [Conclusion](#conclusion)
5. [References](#references)

## 1. Introduction <a name = "intro"></a>
This was the final capstone for a previous task. The project is a shoe inventory system, where user can track the number of shoes based on their location, code, product, price and quantity. The inventory.py file was a template and the inventory.txt file was provided for the assignment. 

The language used is Python.

## Project Description <a name = "description"></a>
The assignment was based on a shoe inventory system for a Nike warehouse, to assist store managers with stock-taking. To optimise the delivery time, an inventory system needs to be implemented.
The warehouses store the following information:
    * Country
    * Code
    * Cost
    * Quantity
    * Value

The program also allows store managers to search for the products by code, help them determine which product needs to be restocked by finding out the product with the lowest quantity, find the product with the highest quantity, and calculate the total value of each item in stock.

### 2.1. How to run the program <a name = "run"></a>
When you run the program what you first see is a menu with the following options:
    * r - Read shoe data
    * c - Capture shoe data
    * va - View all shoe data
    * rs - Re-stock shoes
    * s - Search for shoes
    * vi - Value per item
    * h - highest quantity
    * e - exit

First, you will need to read the data of the text file, inventory.txt. The data from the text file will be converted into a list. That list will be used to view data from the shoe warehouse. Once the data from the text file has been read, you can then decide to view the list, add a new shoe product, re-stock shoes, search for shoes, find the value per item, and find the highest quantity. If the user is done, they can exit the program.

If the user wants to capture a new shoe product, they are required to enter the country the shoes will be sold, the code, the name of the shoes, the cost per pair, and the quantity shipped to that country.

The user can also search for the shoes using the code, the first three characters of the code start with SKU and the last five characters are digits. If the code exists the country, code, the name of the shoes, the price of the shoes, and the stock available will be returned.

If the user wishes to re-stock the shoes, the program will find and return the information of the shoes with the lowest quantity. The user will be prompted if they wish to re-stock the shoes. If yes is selected, the user will be required to enter the amount they wish, the information will be updated in the inventory.txt file. If no is entered, the user will be returned to the menu.

To find the value of the shoes in each location, the program will calculate the value of the shoes by creating two lists, one with the quantity of the shoes and the other with their prices. The values from both lists will be multiplied together and appended to a new list. That list will be combined with the shoe list to create a new list with the country, code, product, cost, quantity, and value of the shoes. The new list will be printed.

The program will find the highest quantity by storing the quantity of the shoes in a new list, compare it to the quantity of each product in the original list, and return the product with the highest quantity with the country, code, the name of the product, the of the product, and the quantity.

## 3. How I can improve the program <a name = "changes"></a>
The program can be proven in the following areas:
* In the restock function, I can prevent the user from entering a value lower than the current stock.
* In the menu, in the capture shoe data option, I could have added more to the capture_shoes method. I should have asked the user to enter the last 5 characters of the code and added it to SKU.
* Adding a GUI using Tkinter or some other Python library.
* Maybe use a database instead of a text file.

## 4. Conclusion <a name = "conclusion"></a>
The program aims to make it more convenient and efficient for the shoe warehouse to monitor the stock of their products and to help them optimise delivery time to help stores restock.

## 5. References <a name = "references"></a>
* https://stackoverflow.com/questions/26051749/how-can-i-convert-the-index-of-a-string-to-an-integer-in-python 
* https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
* https://stackoverflow.com/questions/28618342/find-min-and-max-from-text-file-python
* https://stackoverflow.com/questions/45187646/python-how-to-write-to-specific-line-in-existing-txt-file
* https://www.geeksforgeeks.org/python-program-to-replace-specific-line-in-file/
