# -*- coding: utf-8 -*-
"""movie_theatre_booking_system.ipynb


Original file is located at
    https://colab.research.google.com/drive/1e6Dbmm6vqIILU_1vxZoJmgF5zGWIUJG3

Problem: Build a booking system for a 350-seat theatre that validates age restrictions (12+ only) and seat availability.

Rules:

Theatre capacity: 350 seats (fixed)
Each booking: 1-15 tickets only
Age restriction: 12 years or above
Stop when: Theatre full OR user enters 0
Input: Repeatedly ask for the number of tickets (0 to exit), then the age of each person for valid bookings.

Output: Print booking status for each attempt, then final report showing total bookings, tickets sold, rejected bookings, and remaining seats.

Sample:

Input: 5, then ages: 15, 14, 13, 12, 11 → Output: BOOKING REJECTED - Age restriction

Input: 3, then ages: 20, 18, 16 → Output: BOOKING CONFIRMED - 3 tickets

Input: 0 → Final Report: Total Bookings: 1, Total Tickets Sold: 3, Rejected Bookings: 1, Remaining Seats: 347

Requirements: Use a while loop (main booking), continue statement (skip invalid tickets), for loop (check ages), and break statements (exit loops when needed).
"""

theatre_capacity = 350
max_tickets_per_booking = 15
min_age_required = 12

total_tickets_sold = 0
total_bookings = 0
rejected_bookings = 0

print("Welcome to the Theatre Booking System!")
print(f"Theatre capacity: {theatre_capacity} seats")
print("Each booking: 1-15 tickets")
print(f"Age restriction: {min_age_required}+ only\n")

while total_tickets_sold < theatre_capacity:
    remaining_seats = theatre_capacity - total_tickets_sold
    print(f"Remaining seats: {remaining_seats}")

    num_tickets_str = input("Enter number of tickets (0 to exit): ")
    if not num_tickets_str.isdigit():
        print("Invalid input. Please enter a non-negative whole number.\n")
        rejected_bookings += 1
        continue
    num_tickets = int(num_tickets_str)

    if num_tickets == 0:
        print("Exiting booking system.\n")
        break

    if not (1 <= num_tickets <= max_tickets_per_booking):
        print(f"BOOKING REJECTED - Number of tickets must be between 1 and {max_tickets_per_booking}.\n")
        rejected_bookings += 1
        continue

    if num_tickets > remaining_seats:
        print(f"BOOKING REJECTED - Not enough seats available. Only {remaining_seats} seats left.\n")
        rejected_bookings += 1
        continue

    ages = []
    age_rejection = False
    print(f"Please enter the age for each of the {num_tickets} people:")
    for i in range(num_tickets):
        age_str = input(f"Enter age for person {i + 1}: ")
        if not age_str.isdigit():
            print("Invalid age input. Please enter a non-negative whole number.")
            age_rejection = True
            break
        age = int(age_str)
        if age < min_age_required:
            print(f"Person {i + 1} is {age} years old. Age restriction is {min_age_required}+.")
            age_rejection = True
            break
        ages.append(age)

    if age_rejection:
        print("BOOKING REJECTED - Age restriction (or invalid age input).\n")
        rejected_bookings += 1
        continue

    total_tickets_sold += num_tickets
    total_bookings += 1
    print(f"BOOKING CONFIRMED - {num_tickets} tickets.\n")

    if total_tickets_sold == theatre_capacity:
        print("Theatre is now full! No more bookings can be made.\n")

# Final Report
print("=== FINAL BOOKING REPORT ===")
print(f"Total Bookings Confirmed: {total_bookings}")
print(f"Total Tickets Sold: {total_tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {theatre_capacity - total_tickets_sold}")
