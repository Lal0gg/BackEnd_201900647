from flask import Flask, jsonify, request
from flask_cors import CORS
from Usuario import Usuario
import json
Usuarios = []
app = Flask(__name__)
CORS(app)
Usuarios.append(Usuario("Abner Cardona","M", "Admin", "admin@ipc1.com", "admin@ipc1"))


#Metodo para mostar usuarios
@app.route('/Usuarios',methods =['GET'])
def mostrarUsers():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        objeto = {
            'name':usuario.getName(),
            'gender':usuario.getGender(),
            'username':usuario.getUsername(),
            'email':usuario.getEmail(),
            'password':usuario.getPassword()
        } 
        Datos.append(objeto)
    return(jsonify(Datos)) 

#Login usuario
@app.route('/Login',methods =['GET'])
def obtenerUnUsuario():
    global Usuarios
    envios = []
    for usuario in Usuarios:
        if(usuario.getUsername() == request.json['username'] and usuario.getPassword() == request.json['password'] ):
            unEnvio = {
                'name':usuario.getName(),
                'gender':usuario.getGender(),
                'username':usuario.getUsername(),
                'email':usuario.getEmail(),
                'password':usuario.getPassword()
            } 
            envios.append(unEnvio)
    respuesta = jsonify(envios)   
    return respuesta

#Metodo para encontrar usuario
@app.route('/Usuarios/<string:nombre>', methods=['GET'])
def obtenerUsuario(nombre):
    global Usuarios
    for usuario in Usuarios:
        if usuario.getName() == nombre:
            objeto={
            'name':usuario.getName(),
            'gender':usuario.getGender(),
            'username':usuario.getUsername(),
            'email':usuario.getEmail(),
            'password':usuario.getPassword()
            }
            return(jsonify(objeto))    
    salida = {
        "Mensaje":"No existe el usuario con ese nombre"
    }
    return(jsonify(salida))

#Metodo para aregar usuario
@app.route('/Usuarios',methods=['POST'])
def agregarUsuario():
    global Usuarios
    name = request.json['name']
    gender = request.json['gender']
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    nuevo = Usuario(name,gender,username,email,password)
    Usuarios.append(nuevo)
    return jsonify({
        'mensaje': 'Se agrego el usuario exitosamente'
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port =3000,debug=True)