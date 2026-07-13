# Chessboard Coin Doubling Problem ♟️

## Description

This Python project demonstrates the concept of **exponential growth** using the famous Chessboard Coin Doubling problem.

According to the problem:

* A chessboard contains 64 squares.
* The first square contains 1 coin.
* Every next square contains double the coins of the previous square.
* The program calculates the number of coins placed on each square.

## Concept Used

This project demonstrates:

* Variables
* Input and Output
* For Loop
* Mathematical calculations
* Exponential growth
* Number updating using loops

## Logic

The number of coins on each square follows this pattern:

```
Square 1 = 1
Square 2 = 2
Square 3 = 4
Square 4 = 8

The program starts with:

```
coins = 1
```

After every square:

```
coins = coins * 2
```

## Example Output

```
Enter number of squares: 10

Square 1 = 1
Square 2 = 2
Square 3 = 4
Square 4 = 8
Square 5 = 16
Square 6 = 32
Square 7 = 64
Square 8 = 128
Square 9 = 256
Square 10 = 512
```

## 64th Square Result

The number of coins on the 64th square is:

```
9,223,372,036,854,775,808
```

## Technologies Used

* Python 3

## How to Run

1. Clone the repository:

```
git clone <repository-url>
```

2. Open the project folder:

```
cd Python-Learning
```

3. Run the Python file:

```
python chessboard_coin.py
```

## Learning Outcome

Through this project, I learned how loops can be used to solve mathematical problems and how small changes can create extremely large values through exponential growth.
