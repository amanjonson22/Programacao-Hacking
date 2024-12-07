import phonenumbers as pn

from phonenumbers import geocoder
from phonenumbers import carrier


def location(number):
    ch_number = pn.parse(number, "CH")
    return geocoder.description_for_number(ch_number, "en")

def service_provider(number):
    service_number = pn.parse(number, "RO")
    return carrier.name_for_number(service_number, "en")

phone_number = input("Informe o numero de telefone: ").strip()
print(f"Origem: {location(phone_number)}")
print(f"Provedor de serviço: {service_provider(phone_number)}")
