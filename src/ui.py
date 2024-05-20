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

    folder_selected = ctk.filedialog.askdirectory()

    try:
        export_data(f"{folder_selected}/{entry.get()}", "request-results.csv")
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
        data = show_matrix()
    except FileNotFoundError:
        CTkMessagebox(
            title="Matrix error",
            message="You didn't retrieve the data!",
            icon="cancel", 
            option_1="Ok"
        )
        return
    new_window = ctk.CTkToplevel(window)
    new_window.geometry("400x400")
    new_window.title("Matrix")

    table = Table(new_window, dataframe=data)
    table.show()

def create_ui(url: str):
    main_window = ctk.CTk()
    main_window.geometry("600x500")
    main_window.title("E-Commerce Scraper")
    main_window.minsize(600, 500)

    main_window.protocol("WM_DELETE_WINDOW", lambda: on_close(main_window))

    for i in range(3):
        main_window.grid_columnconfigure(i, weight=1)

    for i in range(5):
        main_window.grid_rowconfigure(i, weight=1)

    title_label = ctk.CTkLabel(main_window, text="E-Commerce Scraper", font=("Arial", 24))
    title_label.grid(row=0, column=1, pady=20)

    request_button = ctk.CTkButton(main_window, text="Retrieve data", command=lambda: retrieve_and_notify(url))
    request_button.grid(row=1, column=1, padx=20, pady=20)

    graph_button = ctk.CTkButton(main_window, text="Show graph", command=show_graph_and_notify)
    graph_button.grid(row=2, column=0, padx=10, pady=20)

    matrix_button = ctk.CTkButton(main_window, text="Show matrix", command=lambda: show_matrix_and_notify(main_window))
    matrix_button.grid(row=2, column=2, padx=10, pady=20)

    export_button = ctk.CTkButton(main_window, text="Export data", command=lambda: export_and_notify(entry))
    export_button.grid(row=3, column=0, padx=20, pady=20)

    entry = ctk.CTkEntry(main_window, placeholder_text="Export file name")
    entry.grid(row=3, column=2, padx=20, pady=20)

    exit_button = ctk.CTkButton(main_window, text="Exit", command=main_window.destroy, fg_color="red", hover=False)
    exit_button.grid(row=4, column=1, padx=20, pady=20)

    return main_window