# Budget Bugger Design Doc.

This app (Budget Bugger) is intended to function as a budgeting app that goes off of a
rolling daily total amount, rather than the traditional monthly, weekly, or bi-weekly
budgets, often segmented into categories, that we normally see.  With this app, users
will be able to see a simple number representing how much they have to spend on
miscellaneous stuff for the day, as well as a (smaller, slightly less significant)
number representing the total amount of money that has been thrown aside into savings.
Both of these numbers roll into the next day, simplifying the budgeting experience,
and potentially even making day-to-day finances a little less stressful for those who
find such activities to be stressful.  I have built essentially this app before in a
CLI, but now I will be recreating (and completely re-writing) a simple GUI version.
This is not because I would like this- oh, no, I loath GUI applications.  If my fingers
leave the keys, I'm a sad panda.  No, this is primarily because my fiancée likes the
CLI version of my app.  So now I'm making her a version that she could use, and I'll
probably just host it off of a Raspberry Pi 4 or something.  And the code will of course
remain available here if you yourself decide to host this app for yourself.

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
  - Phone
  - Internet
  - Monthly ADA investments
  - etc.  
- Income(s)

## The Math Behind It

Initially, Budget Bugger will take the totality of all of the user's assets (let's
call this variable `assets`) and subtract one month's worth of `bills`.  This is to
ensure that the user has, from the start, thrown one month's worth of expenses away
from the get-go.  Think of it more of an additional safety measure to ensure that
the user does not end up not being able to pay a bill on time, or something to this
effect.

So, so far we've got:
`assets - bills = new_assets`,
as we will be calling the current assets the user has.  From here, the user can
choose whether they want to save any money, or just have the running total just be
literally all of the money they could possibly spend before not having enough to
cover a month's worth of bills (which is the goal of this app, to always keep you
above one month's worth of expenses in spare cash outside of savings).

Once we have the `new_assets` variable determined, Budget Bugger will then take the
totality of the monthly bills due and divide them into days.