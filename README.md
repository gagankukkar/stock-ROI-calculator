# stock-ROI-calculator

The purpose of this program is to help the user quickly determine an optimal selling price for a given stock or other investment. As an investor, the goal is the get the best possible return on investment (ROI). This calculator shows you how to get the most bang for your buck!

As someone learning about investing AND programming, developing this calculator was a great way for me to combine my interests. 

To use the program, simply enter the following details:
- Stock name, also known as “ticker”
- Commission charged by bank per transaction
- Quantity and price of shares for each transaction 

There is no limit on the number of transactions so the program ends when the user wants. The program works best for long term investing (e.g. weeks or months). 

Below is an example to show how the calculator works:
- Bob wants to invest in his favorite tech company, Microsoft (MSFT).
- On day 1, he buys 2 shares at $270 each. 
- He notices the price decreases and wants to increase his investment. On day 2, he buys 5 shares at $250 each. 
- He then gets a big bonus at work and wants to invest in even more MSFT shares. On day 3 he buys 8 shares at $215. 
- He then decides he wants to sell his shares so he can invest in something else. 
- Bob also needs to account for commission fees; every time he bought his shares he was charged a fee of $5 by the bank. When he sells all his shares, he'll be charged another $5.

Bob's ROI can now be calculated:
- Total spent on shares = [2 * 270] + [5 * 250] + [8 * 215] = $3510
- Add 3 buying commissions and 1 selling commission = 3510 + [4 * 5] = $3530
- Divide by total shares = 3530 / 15 = $235.33 per share is the average share price (break-even selling price)
- For a 20% ROI, Bob would have to sell his shares at = 235.33 * 1.20 = $282.40 per share

