# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import, protected-access, arguments-out-of-order
""" Módulo que contiene la aplicación Flask para el sistema de reservas """

from flask import Flask, redirect, url_for, render_template, request
from business.reservation_system import ReservationSystem
from business.mydatetime import DateTime
from configuration.configuration_parser import ConfigurationParser

app = Flask(__name__)

config = ConfigurationParser()
reservation_system = ReservationSystem(config)

@app.route('/', methods=['GET'])
def home():
    """ Home """
    reservations = reservation_system.list_all_reservations()
    rooms = reservation_system._room_manager.rooms

    reservation_data = []
    for res in reservations:
        room_name = res.room if isinstance(res.room, str) else res.room.name
        reservation_data.append((
            room_name,
            res.start_datetime,
            res.end_datetime
        ))

    room_data = []
    for rm in rooms:
        room_data.append((
            rm.name,
            rm._capacity
        ))

    return render_template('index.html', reservations=reservation_data, rooms = room_data)


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
            reservation_system.make_reservation(
                room_name, start_datetime, end_datetime)
            return redirect(url_for('home'))
        except ValueError as e:
            return render_template('reservation.html', rooms=reservation_system._room_manager.rooms, error=str(e))

    return render_template('reservation.html', rooms=reservation_system._room_manager.rooms)


@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    """ Cancel reservation """
    if request.method == 'POST':
        room_name = str(request.form.get('room_name'))
        start_datetime_str = str(request.form.get('start_datetime'))

        try:
            date_str, time_str = start_datetime_str.split(' ')
            year, month, day = [int(x) for x in date_str.split('/')]
            hour, minute, second = [int(x) for x in time_str.split(':')]
            start_datetime = DateTime(year, month, day, hour, minute, second)

            reservation_system.cancel_reservation(room_name, start_datetime)
            return redirect(url_for('home'))
        except ValueError as e:
            reservations = reservation_system.list_all_reservations()
            reservation_data = [
                (res.room.name, res.start_datetime, res.end_datetime) for res in reservations]
            return render_template('cancel.html', error=str(e), reservations=reservation_data)

    reservations = reservation_system.list_all_reservations()
    reservation_data = [(res.room.name, res.start_datetime,
                         res.end_datetime) for res in reservations]
    return render_template('cancel.html', reservations=reservation_data)


@app.route('/add_room', methods=['GET', 'POST'])
def add_room():
    """ Add room """
    if request.method == 'POST':
        room_name = request.form['room_name']
        capacity = int(request.form['capacity'])
        reservation_system._room_manager.add_room(room_name, capacity)
        return redirect(url_for('home'))

    return render_template('add_room.html')


@app.route('/remove_room', methods=['GET', 'POST'])
def remove_room():
    """ Remove room and its reservations """
    if request.method == 'POST':
        room_name = request.form['room_name']

        room = next(
            (room for room in reservation_system._room_manager.rooms if room.name == room_name), None)

        if room is not None:
            reservations_to_remove = reservation_system.reservations.copy()
            for res in reservations_to_remove:
                if res.room.name == room_name:
                    reservation_system.cancel_reservation(
                        res.room.name, res.start_datetime)

            reservation_system._room_manager.remove_room(room_name)
            return redirect(url_for('home'))
        else:
            return render_template('remove_room.html', rooms=reservation_system._room_manager.rooms, error="Room not found")

    rooms = reservation_system._room_manager.rooms
    return render_template('remove_room.html', rooms=rooms)


if __name__ == '__main__':
    app.run(port=5000, debug=True, threaded=False)
