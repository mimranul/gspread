import gspread


class DeliverySheet:
    secret_file = "C:\\Users\\rowsh\\Downloads\\pythonspreadsheet-304613-097ebc49384e.json"
    gc = gspread.service_account(filename=secret_file)
    # Select
    spread_sheet_file_name = "Project Aam"
    spread_sheet_delivery_sheet = "Delivery Sheet"

    spread_sheet_file = gc.open(spread_sheet_file_name)

    try:
        delivery_sheet = spread_sheet_file.worksheet(spread_sheet_delivery_sheet)

    except gspread.WorksheetNotFound:
        delivery_sheet = spread_sheet_file.add_worksheet(title=spread_sheet_delivery_sheet)
