import customtkinter as ctk

from CTkMessagebox import CTkMessagebox
from pandastable import Table
from service import retrieve_data, export_data, show_graph, show_matrix, on_close

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")  

def retrieve_and_notify(url: str):
    retrieve_data(url)
    CTkMessagebox(
        title="request info",
        message="Data was retrieved successfully!",
        icon="check", 
        option_1="Thanks"
    )

def export_and_notify(entry: ctk.CTkEntry):
    if not entry.get():
        CTkMessagebox(
            title="Export error",
            message="Please enter a file name!",
            icon="cancel", 
            option_1="Ok"
        )
        return

    DP_folder_selected = ctk.filedialog.askdirectory()

    try:
        export_data(f"{DP_folder_selected}/{entry.get()}", "request-results.csv")
    except FileNotFoundError:
        CTkMessagebox(
            title="Export error",
            message="You didn't retrieve the data!",
            icon="cancel", 
            option_1="Ok"
        )
        return
    except PermissionError:
        return

    CTkMessagebox(
        title="Export info",
        message="Data was exported successfully!",
        icon="check", 
        option_1="Thanks"
    )

def show_graph_and_notify():
    try:
        show_graph()
    except FileNotFoundError:
        CTkMessagebox(
            title="Graph error",
            message="You didn't retrieve the data!",
            icon="cancel", 
            option_1="Ok"
        )
        return
    
def show_matrix_and_notify(window: ctk.CTk):
    try:
        DP_data = show_matrix()
    except FileNotFoundError:
        CTkMessagebox(
            title="Matrix error",
            message="You didn't retrieve the data!",
            icon="cancel", 
            option_1="Ok"
        )
        return
    DP_new_window = ctk.CTkToplevel(window)
    DP_new_window.geometry("400x400")
    DP_new_window.title("Matrix")

    DP_table = Table(DP_new_window, dataframe=DP_data)
    DP_table.show()

def create_ui(url: str):
    DP_main_window = ctk.CTk()
    DP_main_window.geometry("600x500")
    DP_main_window.title("E-Commerce Scraper")
    DP_main_window.minsize(600, 500)

    DP_main_window.protocol("WM_DELETE_WINDOW", lambda: on_close(DP_main_window))

    for i in range(3):
        DP_main_window.grid_columnconfigure(i, weight=1)

    for i in range(5):
        DP_main_window.grid_rowconfigure(i, weight=1)

    DP_title_label = ctk.CTkLabel(DP_main_window, text="E-Commerce Scraper", font=("Arial", 24))
    DP_title_label.grid(row=0, column=1, pady=20)

    DP_request_button = ctk.CTkButton(DP_main_window, text="Retrieve data", command=lambda: retrieve_and_notify(url))
    DP_request_button.grid(row=1, column=1, padx=20, pady=20)

    DP_graph_button = ctk.CTkButton(DP_main_window, text="Show graph", command=show_graph_and_notify)
    DP_graph_button.grid(row=2, column=0, padx=10, pady=20)

    DP_matrix_button = ctk.CTkButton(DP_main_window, text="Show matrix", command=lambda: show_matrix_and_notify(DP_main_window))
    DP_matrix_button.grid(row=2, column=2, padx=10, pady=20)

    DP_export_button = ctk.CTkButton(DP_main_window, text="Export data", command=lambda: export_and_notify(entry))
    DP_export_button.grid(row=3, column=0, padx=20, pady=20)

    DP_entry = ctk.CTkEntry(DP_main_window, placeholder_text="Export file name")
    DP_entry.grid(row=3, column=2, padx=20, pady=20)

    DP_exit_button = ctk.CTkButton(DP_main_window, text="Exit", command=DP_main_window.destroy, fg_color="red", hover=False)
    DP_exit_button.grid(row=4, column=1, padx=20, pady=20)

    return DP_main_window