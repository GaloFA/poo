# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import, protected-access
""" Imports """

from flask import Flask, redirect, url_for, render_template, request
from reservation_system import ReservationSystem
from mydatetime import DateTime, Date

app = Flask(__name__)

def create_system():
    """ Create system """
    res_system = ReservationSystem()
    res_system._room_management.add_room("Sala 1", 10)
    res_system._room_management.add_room("Sala 2", 20)
    res_system._room_management.add_room("Sala 3", 30)

    res_system.make_reservation("Sala 1", DateTime(2024, 9, 20, 14, 30, 0), DateTime(2024, 9, 20, 15, 30, 0))
    res_system.make_reservation("Sala 1", DateTime(2024, 9, 20, 15, 31, 0), DateTime(2024, 9, 20, 16, 30, 0))
    res_system.make_reservation("Sala 2", DateTime(2024, 9, 20, 16, 30, 0), DateTime(2024, 9, 20, 17, 30, 0))
    res_system.make_reservation("Sala 3", DateTime(2024, 9, 20, 18, 30, 0), DateTime(2024, 9, 20, 19, 30, 0))

    return res_system

reservation_system = create_system()

@app.route('/', methods=['GET'])
def home():
    """ Home """
    reservations = reservation_system.list_reservations(Date(2024, 9, 20))

    reservation_data = []
    for res in reservations:
        reservation_data.append((
            res.room.name,
            res.start_datetime,
            res.end_datetime
        ))

    return render_template('index.html', reservations=reservation_data)


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
        start_second = int(request.form['start_second'])

        end_day = int(request.form['end_day'])
        end_month = int(request.form['end_month'])
        end_year = int(request.form['end_year'])
        end_hour = int(request.form['end_hour'])
        end_minute = int(request.form['end_minute'])
        end_second = int(request.form['end_second'])

        start_datetime = DateTime(start_year, start_month, start_day, start_hour, start_minute, start_second)
        end_datetime = DateTime(end_year, end_month, end_day, end_hour, end_minute, end_second)

        try:
            reservation_system.make_reservation(room_name, start_datetime, end_datetime)
            return redirect(url_for('home'))
        except ValueError as e:
            return render_template('reservation.html', rooms=reservation_system._room_management.rooms, error=str(e))

    return render_template('reservation.html', rooms=reservation_system._room_management.rooms)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
