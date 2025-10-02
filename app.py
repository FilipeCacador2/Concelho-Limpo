from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash, get_flashed_messages, jsonify
import mysql.connector, io

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Ligação à Base de Dados
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="coruche_limpo"
    )


@app.route("/")
def index():
    return render_template("index.html")

# Formulário de pedido de recolha
@app.route("/submit_recolha", methods=["POST"])
def submit_recolha():
    telefone = request.form.get("telefone")
    email = request.form.get("email")

    if not telefone and not email:
        flash("Erro: insira pelo menos telefone ou email.", "error")
        return redirect(url_for("index"))

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO form_recolha (nome, nif, morada_recolha, tipo_recolha, telefone, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        request.form["nome"],
        request.form["nif"],
        request.form["morada_recolha"],
        request.form["tipo_recolha"],
        telefone,
        email
    ))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Pedido de recolha submetido com sucesso!", "success")
    return redirect(url_for("index"))



# Formulário de Realatório
@app.route("/submit_report", methods=["POST"])
def submit_report():
    conn = get_db()
    cursor = conn.cursor()
    foto = request.files["foto"].read()
    cursor.execute("INSERT INTO form_report (localizacao, foto) VALUES (%s, %s)",
                   (request.form["localizacao"], foto))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Ocorrência reportada com sucesso!", "success")
    return redirect(url_for("index"))

# Inserção de Imagem
@app.route("/image/<int:report_id>")
def image(report_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT foto FROM form_report WHERE id_report = %s", (report_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row and row[0]:
        return send_file(io.BytesIO(row[0]), mimetype="image/jpeg")
    else:
        return "No image", 404

# Mapa 
@app.route("/map-data")
def map_data():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, tipo, lat, lng FROM ecopontos")
    points = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(points)


# Login Admin
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM funcionarios WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session["user_id"] = user["id_funcionario"]
            session["user_name"] = user["nome"]
            return redirect(url_for("admin"))
        else:
            return "Credenciais inválidas"

    return render_template("login.html")


# Dashboard Admin
@app.route("/admin")
def admin():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM form_recolha")
    recolhas = cursor.fetchall()
    cursor.execute("SELECT id_report, localizacao FROM form_report")
    reports = cursor.fetchall()
    cursor.execute("SELECT * FROM ecopontos")
    ecopontos = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("admin.html", recolhas=recolhas, reports=reports, ecopontos=ecopontos, user=session["user_name"])


@app.route("/delete/<table>/<int:item_id>")
def delete(table, item_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cursor = conn.cursor()
    if table == "form_recolha":
        cursor.execute("DELETE FROM form_recolha WHERE id_form = %s", (item_id,))
    elif table == "form_report":
        cursor.execute("DELETE FROM form_report WHERE id_report = %s", (item_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("admin"))

@app.route("/add-ecoponto", methods=["POST"])
def add_ecoponto():
    if "user_id" not in session:
        return redirect(url_for("login"))

    nome = request.form["nome"]
    tipo = request.form["tipo"]
    lat = request.form["lat"]
    lng = request.form["lng"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ecopontos (nome, tipo, lat, lng)
        VALUES (%s, %s, %s, %s)
    """, (nome, tipo, lat, lng))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Ecoponto adicionado com sucesso!", "success")
    return redirect(url_for("admin"))



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
