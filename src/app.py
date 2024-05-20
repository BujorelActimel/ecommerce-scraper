from ui import create_ui

url = "https://www.laptopsdirect.co.uk/ct/monitors-and-projectors/monitors/curved"

if __name__ == "__main__":
    app = create_ui(url)
    app.mainloop()