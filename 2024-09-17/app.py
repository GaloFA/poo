# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import
""" Imports """
from flask import Flask, redirect, url_for, render_template, request
from reservation_system import ReservationSystem
from room_management import RoomManagement
from mydatetime import DateTime
from date import Date

app = Flask(__name__)

def create_system():
    """ Crear el sistema """
    res_system = ReservationSystem()
    room1 = res_system._room_management.add_room("Sala 1", 10)
    room2 = res_system._room_management.add_room("Sala 2", 20)
    room3 = res_system._room_management.add_room("Sala 3", 30)

    res_system.make_reservation("Sala 1", DateTime(20, 9, 2024, 14, 30, 0), DateTime(20, 9, 2024, 15, 30, 0))
    res_system.make_reservation("Sala 1", DateTime(20, 9, 2024, 15, 31, 0), DateTime(20, 9, 2024, 16, 30, 0))
    res_system.make_reservation("Sala 2", DateTime(20, 9, 2024, 16, 30, 0), DateTime(20, 9, 2024, 17, 30, 0))
    res_system.make_reservation("Sala 3", DateTime(20, 9, 2024, 18, 30, 0), DateTime(20, 9, 2024, 19, 30, 0))

    return res_system

reservation_system = create_system()

@app.route('/', methods=['GET', 'POST'])
def home():
    """ Index """
    if request.method == 'POST':
        return render_template('index.html', reservations=reservation_system.reservations)

    reservation_list = reservation_system.list_reservations(Date(20, 9, 2024))

    reservations = []
    for reservation in reservation_list:
        reservations.append((
            reservation.room.name, 
            reservation.start_datetime, 
            reservation.end_datetime
        ))

    return render_template('index.html', reservations=reservations)

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    """ Reservation """
    if request.method == 'POST':
        room_name = request.form['room_name']
        start_day = int(request.form['start_day'])
        start_month = int(request.form['start_month'])
        start_year = int(request.form['start_year'])
        start_hour = int(request.form['start_hour'])
        start_minute = int(request.form['start_minute'])
        start_second = 0

        end_day = int(request.form['end_day'])
        end_month = int(request.form['end_month'])
        end_year = int(request.form['end_year'])
        end_hour = int(request.form['end_hour'])
        end_minute = int(request.form['end_minute'])
        end_second = 0

        start_datetime = DateTime(start_day, start_month, start_year, start_hour, start_minute, start_second)
        end_datetime = DateTime(end_day, end_month, end_year, end_hour, end_minute, end_second)

        try:
            reservation_system.make_reservation(room_name, start_datetime, end_datetime)
            return redirect(url_for('home', message="Reservation created successfully!"))
        except ValueError as e:
            return render_template('reservation.html', error=str(e))

    return render_template('reservation.html', rooms=reservation_system._room_management.rooms)

#@app.route('/cancelar', methods=['GET', 'POST'])
#def cancelar():
#    pass

if __name__ == '__main__':
    app.run(port=5000,debug=True)
