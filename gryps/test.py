import datetime
import calendar

def monthly_charge(month, subscription, users):
  """ Computes the monthly charge for a given subscription.
 
  @rtype: int
  @returns: the total monthly bill for the customer in cents, rounded
    to the nearest cent. For example, a bill of $20.00 should return 2000.
    If there are no active users or the subscription is None, returns 0.
 
  @type month: str
  @param month - Always present
    Has the following structure:
    "2022-04"  # April 2022 in YYYY-MM format

  @type subscription: dict
  @param subscription - May be None
    If present, has the following structure:
    {
      'id': 763,
      'customer_id': 328,
      'monthly_price_in_cents': 359  # price per active user per month
    }
 
  @type users: list
  @param users - May be empty, but not None
    Has the following structure:
    [
      {
        'id': 1,
        'name': "Employee #1",
        'customer_id': 1,
    
        # when this user started
        'activated_on': datetime.date(2021, 11, 4),
    
        # last day to bill for user
        # should bill up to and including this date
        # since user had some access on this date
        'deactivated_on': datetime.date(2022, 4, 10)
      },
      {
        'id': 2,
        'name': "Employee #2",
        'customer_id': 1,
    
        # when this user started
        'activated_on': datetime.date(2021, 12, 4),
    
        # hasn't been deactivated yet
        'deactivated_on': None
      },
    ]
  """
  # your code here!
      # Check if subscription is None or there are no active users
  if subscription is None or not users:
    return 0
  
  # Extract year and month from the provided month string
  year, month = map(int, month.split('-'))
  first_day_month =  datetime.date(year, month, 1)
  # Get the last day of the given month
  last_day_month = last_day_of_month( datetime.date(year, month, 1))
  print()
  # Calculate the total monthly charge for all active users
  total_charge = 0
  for user in users:
    print(user['activated_on'], user['deactivated_on'], last_day_month)
    # Check if the user's activated date is before or on the last day of the given month
    if user['activated_on'] <= last_day_month:
      # If the user's deactivated date is not None and is after the last day of the given month, consider the last day of the month as the deactivated date
      if user['deactivated_on'] is not None and user['deactivated_on'] > last_day_month:
        deactivated_on = last_day_month
      else:
        # If deactivated_on is None, assume the current date as the deactivated_on date
        deactivated_on = user['deactivated_on']
       
      if user['deactivated_on'] < first_day_month:
        acton = first_day_month
      else:
        acton = user['deactivated_on']
      # Calculate the number of days the user was active in the given month
      if acton < deactivated_on:
        days_active = (deactivated_on - acton).days + 1
      else:
        days_active = 0
      print(deactivated_on)
      # Calculate the monthly charge for the user for the given month
      user_charge = days_active * subscription['monthly_price_in_cents']
      total_charge += user_charge
  
  # Round the total charge to the nearest cent and return
  return round(total_charge)

#   if subscription is None or not users:
#     return 0
  
#   total_charge = 0
    
#   for user in users:
#     # If the user's deactivated date is not None and is after the last day of the given month, consider the last day of the month as the deactivated date
#     if user['deactivated_on'] is not None:
#       time_difference = user['deactivated_on'] - user['activated_on']
#       total_charge += time_difference.days * subscription['monthly_price_in_cents']
#     else:
#       # If deactivated_on is None, assume the current date as the deactivated_on date
#       end_date = datetime.date.today()
#       time_difference = end_date - user['activated_on']
#       total_charge += time_difference.days * subscription['monthly_price_in_cents']
  
#   # Round the total charge to the nearest cent and return
#   return round(total_charge)

####################
# Helper functions #
####################

def first_day_of_month(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the first day of that month. For example:

  >>> first_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
  datetime.date(2022, 3, 1)                           # Mar  1

  Input type: datetime.date
  Output type: datetime.date
  """
  return date.replace(day=1)

def last_day_of_month(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the last day of that month. For example:

  >>> last_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
  datetime.date(2022, 3, 31)                         # Mar 31

  Input type: datetime.date
  Output type: datetime.date
  """
  last_day = calendar.monthrange(date.year, date.month)[1]
  return date.replace(day=last_day)

def next_day(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the next day. For example:

  >>> next_day(datetime.date(2022, 3, 17))   # Mar 17
  datetime.date(2022, 3, 18)                 # Mar 18

  >>> next_day(datetime.date(2022, 3, 31))  # Mar 31
  datetime.date(2022, 4, 1)                 # Apr  1

  Input type: datetime.date
  Output type: datetime.date
  """
  return date + datetime.timedelta(days=1)
