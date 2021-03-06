# Python-challenge
This project analyzed financial record of sample company called PyBank and vote-counting using Python.

## PyBank

In this challenge, my task is to create a Python script for analyzing the financial records of PyBank. I was given a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 

I created a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The average of the changes in "Profit/Losses" over the entire period

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in losses (date and amount) over the entire period

This is the result after running the script.
```
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

Python script is saved here (Pybank/main.py) : https://github.com/kanamoore/python-challenge/blob/master/PyBank/main.py

## PyPoll
Vote-Counting

In this challenge, my task is to help a small, rural town modernize its vote-counting process. 

I was given a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. My task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

This is the result after running a script.
```
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
```
Python script is saved here (PyPoll/main.py) : https://github.com/kanamoore/python-challenge/blob/master/PyPoll/main.py
