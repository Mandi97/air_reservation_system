class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

        rows, letters = airplane.get_seating_plan()
        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()

    def _parse_seat(self, seat):
        rows, letters = self.airplane.get_seating_plan()

        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f'Invalid seat letter: {letter}')

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row value: {row_text}')

        if row not in rows:
            raise ValueError(f'Row is out of rows range: {row}')

        return row, letter

    def allocate_passenger(self, seat, passenger):
        row, letter = self._parse_seat(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f'Seat is already occupied: {seat}')

        self.seats[row][letter] = passenger

    def get_empty_seats(self, seat):
        counter = 0

        for row in self.seats:
            if row is not None:
                for value in row.values():
                    if value is None:
                        counter += 1

        return counter
