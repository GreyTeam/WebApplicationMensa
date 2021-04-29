"""

███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗  
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝  
██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░  
██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░  
██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░  
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░  

██████╗░░█████╗░██╗░░░██╗██╗██████╗░███████╗
██╔══██╗██╔══██╗██║░░░██║██║██╔══██╗██╔════╝
██║░░██║███████║╚██╗░██╔╝██║██║░░██║█████╗░░
██║░░██║██╔══██║░╚████╔╝░██║██║░░██║██╔══╝░░
██████╔╝██║░░██║░░╚██╔╝░░██║██████╔╝███████╗
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚══════╝

░█████╗░███╗░░██╗██████╗░██████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░██╗
██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██║
███████║██╔██╗██║██║░░██║██████╔╝█████╗░░██║░░██║██║░░░░░██║░░░░░██║
██╔══██║██║╚████║██║░░██║██╔══██╗██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║
██║░░██║██║░╚███║██████╔╝██║░░██║███████╗╚█████╔╝███████╗███████╗██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝╚══════╝╚═╝


"""

def missing_element_response(header):
    return {
        "result": "ERROR",
        "missing_header": header,
        "message": f"Error with request: missing arguments ({header})"
    }

def invalid_date_response():
    return {
        "result": "ERROR",
        "message": "The date provided is invalid"
    }

def key_doesnt_exist():
    return {
        "result": "ERROR",
        "message": "Key doesn't exist on the server"
    }

def reservation_already_registered(date):
    return {
        "result": "ERROR",
        "message": f"A reservation for the date {date} is already registered",
        "date": date
    }

