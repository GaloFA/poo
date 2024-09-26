# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import
""" Imports """
from flask import Flask, redirect, url_for, render_template, request
from reservation_system import ReservationSystem
from room_management import RoomManagement

app = Flask(__name__)

def create_system():
    """ Crear el sistema """
    reservation_system = ReservationSystem()
    room_management = RoomManagement()
    room1 = room_management.add_room("Sala 1", 10)
    room2 = room_management.add_room("Sala 2", 20)
    room3 = room_management.add_room("Sala 3", 30)
    return reservation_system

reservation_system = create_system()

@app.route('/',methods=['GET','POST'])
def home():
    """ Index """
    if request.method=='POST':
        return render_template('index.html')

    listado_reservas = reservation_system.list_reservations()

    reservas = []
    for sala in listado_reservas:
        for reserva in listado_reservas[sala]:
            reservas.append((sala, reserva.inicio, reserva.fin))

    return render_template('index.html', reservas=reservas)

@app.route('/reservar', methods=['GET', 'POST'])
def reservar():
    pass

@app.route('/cancelar', methods=['GET', 'POST'])
def cancelar():
    pass

if __name__ == '__main__':
    app.run(port=5000,debug=True)