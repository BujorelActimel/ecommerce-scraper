from ui import create_ui

DP_url = "https://www.laptopsdirect.co.uk/ct/monitors-and-projectors/monitors/curved"

if __name__ == "__main__":
    DP_app = create_ui(DP_url)
    DP_app.mainloop()