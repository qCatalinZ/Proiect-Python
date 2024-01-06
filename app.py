from flask import render_template
from flask import Flask, redirect, url_for
from firebase import firebase

firebase = firebase.FirebaseApplication('https://catalinz-default-rtdb.europe-west1.firebasedatabase.app/', None)


app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html") # randam o pagina web facuta in html

@app.route("/pistols")
def Pistols():
    data = get_weapon_data('pistols')
    return render_template("weapon_name_list.html", name='pistols', data=data)


@app.route("/assault_rifles")
def Assault_Rifles():
    data = get_weapon_data('assault_rifles')
    return render_template("weapon_name_list.html", name='assault_rifles', data=data)


@app.route("/smgs")
def SMGs():
    data = get_weapon_data('smgs')
    return render_template("weapon_name_list.html", name='smgs', data=data)


@app.route("/shotguns")
def Shotguns():
    data = get_weapon_data('shotguns')
    return render_template("weapon_name_list.html", name='shotguns', data=data)


@app.route("/sniper_rifles")
def Sniper_Rifles():
    data = get_weapon_data('sniper_rifles')
    return render_template("weapon_name_list.html", name='sniper_rifles', data=data)


@app.route("/rocket_launchers")
def Rocket_Launchers():
    data = get_weapon_data('rocket_launchers')
    return render_template("weapon_name_list.html", name='rocket_launchers', data=data)


@app.route("/<type>/<id>") # type e tipul armei, id e numele din firebase
def weapon_details(type, id):
    data = get_weapon_data2(type, id) # data este un dictionar cu datele armei din id
    return render_template('weapons_template.html', id=id, type=type, data=data)

def get_weapon_data(name): # name e tipul de arme din care vrei sa fie luat datele
    weapon_data = firebase.get('/'+name, None)
    return weapon_data

def get_weapon_data2(type, id): # name e tipul armei, id e numele armei
    weapon_data = firebase.get('/'+type+'/'+id, None)
    return weapon_data


# functiile sunt pagini web iar daca vom folosi in interiorul functei noastre "return redirect(url_for("numele_paginii"))"
# ne v-a duce catre pagina respectiva. ex: return redirect(url_for("Shotguns"))













def main():
    app.run() #app.run(debug=True)

if __name__ == '__main__':
    main()