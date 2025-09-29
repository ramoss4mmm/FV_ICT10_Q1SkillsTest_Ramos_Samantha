from pyscript import document, display

#This gets the input from the form
def order(event):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number").value

#This gets the total of the prices
    total = 0
    if document.getElementById("matcha").checked:
        total += 200
    if document.getElementById("latte").checked:
        total += 170
    if document.getElementById("americano").checked:
        total += 160
    if document.getElementById("espresso").checked:
        total += 120
    if document.getElementById("frappe").checked:
        total += 160
    if document.getElementById("cookie").checked:
        total += 120

    #This shows the order summary the message
    result = f"""
    Order Confirmation
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️
    Order for   : {name}
    Adress    : {address}
    Phone number : {number}
    Total : ₱ {total}
    """

    #This shows the result
    document.getElementById("order1").innerText = result
