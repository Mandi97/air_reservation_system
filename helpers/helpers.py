from pprint import pprint as pp

from flight.flight import Flight
from planes.airbusa380 import AirbusA380
from planes.boeing737max import Boeing737Max


def make_flight():
    b = Boeing737Max()
    a = AirbusA380()
    f = Flight('BA120', b)
    # print(f.get_airline())
    # print(f.get_number())
    # print(b.get_airplane_model())
    # print(f.get_model())


    f.allocate_passenger('12C', 'Andrzej D')
    f.allocate_passenger('1D', 'Pawel J')
    f.allocate_passenger('25E', 'Antoni M')
    pp(f.seats)
