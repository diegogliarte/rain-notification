import requests
from xml.etree import ElementTree
from datetime import date


def get_rain(url):
    """

    :param url: url from aemet.es with prediction for hours
    :return: dictionary with period : [description, probability of rain]
    """
    response = requests.get(url)
    tree = ElementTree.fromstring(response.content)
    today = date.today()

    stats = {}

    for day in tree.findall(f".//*[@fecha='{today}']/estado_cielo"):
        periodo = day.attrib["periodo"]
        descripcion = day.attrib["descripcion"].lower()
        probabilidad = day.text
        probabilidad = probabilidad.replace("n", "") # This removes the "n" from the probability
        stats[periodo] = [descripcion, probabilidad]

    return stats

if __name__ == "__main__":
    url = "http://www.aemet.es/xml/municipios_h/localidad_h_25120.xml"
    stats = get_rain(url)
    for key, value in stats.items():
        print(f"{key} -> {value}")