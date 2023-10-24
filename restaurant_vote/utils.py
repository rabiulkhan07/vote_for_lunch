from datetime import date, timedelta
from .models import Restaurant, Menu,Vote

def calculate_daily_winner():
    today = date.today()

    # Get the menus for the current day
    menus_today = Menu.objects.filter(date=today)

    # Initialize a dictionary to store vote counts for each restaurant
    vote_counts = {}

    # Calculate the total vote count for each restaurant
    for menu in menus_today:
        votes = Vote.objects.filter(menu=menu)
        for vote in votes:
            restaurant_id = menu.restaurant.id
            if restaurant_id not in vote_counts:
                vote_counts[restaurant_id] = 1
            else:
                vote_counts[restaurant_id] += 1

    # Find the restaurant with the most votes for the current day
    winner_id = max(vote_counts, key=vote_counts.get)
    winner = Restaurant.objects.get(pk=winner_id)

    return winner