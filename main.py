class Mun:
    def __init__(self, ine_code, sup_km2, den_km2):
        self.ine_code = ine_code
        self.sup_km2 = sup_km2
        self.den_km2 = den_km2

municipio_1 = {
    "codigo_ine": "280006",
    "sup_km2": 5,
    "den_km2": 3.72
}

obj_municipio_1 = Mun("280006", 5, 3.72)

print(type(3))
print(type(obj_municipio_1))

municipio_2 = {
    "codigo_ine": "280007",
    "sup_km2": 3,
    "den_km2": 5.72
}