import datetime
import time
import os

def display_current_time_counting():
    """Displays the current time, updating every second."""
    try:
        while True:
            # Get the current time
            now = datetime.datetime.now()
            
            # Format the time as HH:MM:SS
            current_time_str = now.strftime("%H:%M:%S")
            
            # Clear the console (for a cleaner display)
            # 'cls' for Windows, 'clear' for Unix-like systems
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Print the formatted time
            print(f"Current Time: {current_time_str}")
            
            # Wait for 1 second before updating again
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTime display stopped.")

if __name__ == "__main__":
    display_current_time_counting()