import tkinter as tk
import subprocess

root = tk.Tk()

root.title("Wifi password generator")
root.geometry("600x300")

extract_data = tk.StringVar()


def extract():
    a = []
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

    for wifi in wifis:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
        
        try:
            a.append(f'{wifi}  ->>  {results[0]}')
        except IndexError:
            a.append(f'Name: {wifi}, password: Cannot found!')
    for i in a:
        password_generate = tk.Label(root, text=i, font = ("calibre",10, "bold"))
        password_generate.pack()




Heading = tk.Label(root, text="Welcome to wifi extracter!!", font = ("calibre",20, "bold"))
Extract_button = tk.Button(root, text="Extract Password!!", command = extract)


Heading.pack()
Extract_button.pack()

root.mainloop()