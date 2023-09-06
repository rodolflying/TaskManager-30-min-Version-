import pandas as pd
import datetime
import time
import tkinter as tk
from tkinter import messagebox
import schedule

def read_tasks():
    df = pd.read_csv('tasks.csv', parse_dates=[['date', 'time']])
    return df

def show_alert(task):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    response = messagebox.askyesno("Task Alert", f"Do you want to work on the task \"{task['name']}\" now?")
    if response:
        # Here you can add code to mark the task as completed if it's automated
        pass
    root.destroy()

def execute_tasks():
    tasks = read_tasks()
    tasks = tasks.sort_values(by='date_time')  # Sort tasks by date and time
    now = datetime.datetime.now()
    
    for index, task in tasks.iterrows():
        task_time = task['date_time'].to_pydatetime()
        print("Task time: ", task_time)
        if now <= task_time:
            
            seconds_until_task = (task_time - now).total_seconds()
            print("Waiting for task time...", seconds_until_task, " seconds")
            time.sleep(seconds_until_task)
        print("Executing task...")
        show_alert(task)
        print("Task executed!")

def main():
    # Schedule the task execution
    schedule.every().day.at("01:41:00").do(execute_tasks)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
