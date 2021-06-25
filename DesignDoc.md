# Budget Bugger Design Doc.

This app (Budget Bugger) is intended to function as a budgeting app that goes off of a
rolling daily total amount, rather than the traditional monthly, weekly, or bi-weekly
budgets, often segmented into categories, that we normally see.  With this app, users
will be able to see a simple number representing how much they have to spend on
miscellaneous stuff for the day, as well as a (smaller, slightly less significant)
number representing the total amount of money that has been thrown aside into savings.
Both of these numbers roll into the next day, simplifying the budgeting experience,
and potentially even making day-to-day finances a little less stressful for those who
find such activities to be stressful.

## The Logic Behind It

Budget Bugger will have to be able to assign different accounts to different users.
When a user's account is initially setup, they will go through a process by which
they manually enter all of the variables needed for the app to make all of the
calculations on the back end.  These variables include:

- Assets
  - Cash on hand
  - Total(s) in checking account(s)
  - Total(s) in savings account(s)
  - etc.  
- Bills
  - Mortgage/rent
  - Auto insurance
  -   
- Income(s)