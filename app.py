from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_key"

# Каталог товаров
PRODUCTS = {
    1: {"name": "Фигурка Симки", "price": 890, "desc": "Яркая фигурка главной героини"},
    2: {"name": "Фигурка Нолика", "price": 890, "desc": "Любимец детей, светящиеся детали"},
    3: {"name": "Набор 'Фиксики'", "price": 2490, "desc": "5 фигурок + домик-помогатор"},
    4: {"name": "Пазл 'Тыдыщ!'", "price": 450, "desc": "Пазл на 120 деталей"},
}

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)

@app.route("/add/<int:pid>")
def add_to_cart(pid):
    cart = session.get("cart", {})
    cart[str(pid)] = cart.get(str(pid), 0) + 1
    session["cart"] = cart
    return redirect(url_for("index"))

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    items = []
    total = 0
    for pid, qty in cart.items():
        p = PRODUCTS[int(pid)]
        subtotal = p["price"] * qty
        total += subtotal
        items.append({**p, "qty": qty, "subtotal": subtotal})
    return render_template("cart.html", items=items, total=total)

@app.route("/clear")
def clear():
    session.pop("cart", None)
    return redirect(url_for("cart"))

if __name__ == "__main__":
    app.run(debug=True)
