import xml.etree.ElementTree as ET


class VeganProductsBuilder:
    def __init__(
        self, products, product_name_key="product", category_name="Vegan Products"
    ):
        self._products = products
        self._product_name_key = product_name_key
        self._category_name = category_name

    def build(self, output):
        root = ET.Element("shop")
        category = ET.SubElement(root, "category", {"name": self._category_name})

        for product_data in self._products:
            product_name = product_data.pop(self._product_name_key)

            if not product_name:
                raise KeyError("Product name key doesn't exist")

            product_element = ET.SubElement(category, "product", {"name": product_name})

            for child_key, child_value in product_data.items():
                child_element = ET.SubElement(product_element, child_key)
                child_element.text = str(child_value)

        tree = ET.ElementTree(root)
        tree.write(output, "UTF-8", xml_declaration=True)


vegan_products = [
    {
        "product": "Good Morning Sunshine",
        "type": "cereals",
        "producer": "OpenEDG Testing Service",
        "price": 9.90,
        "currency": "USD",
    },
    {
        "product": "Spaghetti Veganietto",
        "type": "pasta",
        "producer": "Programmers Eat Pasta",
        "price": 15.49,
        "currency": "EUR",
    },
    {
        "product": "Fantastic Almond Milk",
        "type": "beverages",
        "producer": "Drinks4Coders",
        "price": 19.75,
        "currency": "USD",
        "special_price": 15.35,
    },
]

builder = VeganProductsBuilder(vegan_products)
builder.build("./xml_/shop.xml")
