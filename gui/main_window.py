import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from utils.imports import setup_database, save_target, get_target_id, save_recon_data, get_previous_targets
from utils.buttons import get_buttons  # Import the get_buttons function

# Initialize the database
setup_database()

def start_recon():
    """
    Start the reconnaissance process for the selected or new target.
    """
    target_name = target_entry.get()
    if not target_name:
        messagebox.showwarning("Input Error", "Please enter a target.")
        return

    # Save the target if it's new
    save_target(target_name)
    target_id = get_target_id(target_name)

    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, f"Starting reconnaissance on {target_name}...\n")
    messagebox.showinfo("Recon Started", "Reconnaissance process started. Use the buttons below to perform specific scans.")

def load_previous_targets():
    """
    Load and display the list of previous targets.
    """
    previous_targets = get_previous_targets()
    target_combobox['values'] = previous_targets
    if previous_targets:
        target_combobox.current(0)

def on_target_select(event):
    """
    Handle the event when a previous target is selected.
    """
    selected_target = target_combobox.get()
    target_entry.delete(0, tk.END)
    target_entry.insert(0, selected_target)

# GUI setup
app = tk.Tk()
app.title("Recon Tool")

# List Previous Targets
previous_targets_frame = tk.LabelFrame(app, text="List Previous Targets")
previous_targets_frame.pack(pady=10, padx=10, fill="x")

target_combobox = ttk.Combobox(previous_targets_frame, state="readonly")
target_combobox.pack(pady=5, padx=5, fill="x")
target_combobox.bind("<<ComboboxSelected>>", on_target_select)

load_previous_targets()

# New Target
new_target_frame = tk.LabelFrame(app, text="New Target")
new_target_frame.pack(pady=10, padx=10, fill="x")

target_label = tk.Label(new_target_frame, text="Enter Target:")
target_label.pack(pady=5)

target_entry = tk.Entry(new_target_frame, width=50)
target_entry.pack(pady=5)

# Start Recon button
start_button = tk.Button(new_target_frame, text="Start Recon", command=start_recon)
start_button.pack(pady=10)

# Output area
output_text = scrolledtext.ScrolledText(app, width=80, height=20)
output_text.pack(pady=10)

# Additional Functionality Buttons in a Scrollable Frame
additional_functions_frame = tk.LabelFrame(app, text="Additional Functions")
additional_functions_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Create a canvas and a scrollbar
canvas = tk.Canvas(additional_functions_frame)
scrollbar = ttk.Scrollbar(additional_functions_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

# Configure the canvas
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Get the buttons from utils/buttons.py
buttons = get_buttons(target_entry)

# Add buttons to the scrollable frame
row, col = 0, 0
for text, command in buttons:
    button = tk.Button(scrollable_frame, text=text, command=command)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
    col += 1
    if col > 2:  # 3 buttons per row
        col = 0
        row += 1

# Run the application
app.mainloop()