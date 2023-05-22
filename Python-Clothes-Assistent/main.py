import csv
import random


class Item:
    def __init__(self, category, name, color, temperature, style, weather):
        """
        Initializes an Item object with the given attributes.

        Args:
            category (str): The category of the item (e.g., jacket, shirt, pants, shoes).
            name (str): The name of the item.
            color (str): The color of the item.
            temperature (str): The temperature category of the item (cold, medium, hot).
            style (str): The style category of the item (casual, formal).
            weather (str): The item type of weather (rainy, sunny).
        """
        self.name = name
        self.color = color
        self.temperature = temperature
        self.style = style
        self.category = category
        self.weather = weather

    def __str__(self):
        """
        Returns a string representation of the Item object.

        Returns:
            str: The string representation of the item in the format "name/color".
        """
        return f"{self.name}/{self.color}"


class ItemManager:
    CATEGORY_JACKET = "jacket"
    CATEGORY_SHIRT = "shirt"
    CATEGORY_PANTS = "pants"
    CATEGORY_SHOES = "shoes"

    TEMPERATURE_HOT = "hot"
    TEMPERATURE_MEDIUM = "medium"
    TEMPERATURE_COLD = "cold"

    STYLE_CASUAL = "casual"
    STYLE_FORMAL = "formal"

    def __init__(self, filename):
        """
        Initializes an ItemManager object with the given CSV filename.

        Args:
            filename (str): The filename of the CSV file containing item data.
        """
        self.filename = filename
        self.items = []

    def load_items(self):
        """
        Loads items from the CSV file and creates Item objects.

        The CSV file should have columns: 'category', 'name', 'color', 'temperature', 'style' and 'weather'.
        """
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = Item(
                    row['category'], row['name'], row['color'], row['temperature'], row['style'], row['weather']
                )
                self.items.append(item)

    @staticmethod
    def temperature_check(temperature):
        """
        Determines the temperature category based on the given temperature.

        Args:
            temperature (int): The temperature value.

        Returns:
            str: The temperature category ('hot', 'medium', 'cold').
        """
        if temperature >= 21:
            return ItemManager.TEMPERATURE_HOT
        elif temperature >= 15:
            return ItemManager.TEMPERATURE_MEDIUM
        else:
            return ItemManager.TEMPERATURE_COLD

    def choose_item(self, category, temperature, style):
        """
        Chooses a random item that matches the given category, temperature, and style.

        Args:
            category (str): The category of the item to choose.
            temperature (int): The current temperature.
            style (str): The current style.

        Returns:
            Item or None: The chosen item object or None if no suitable item is found.
        """
        temperature_category = self.temperature_check(temperature)
        valid_items = []
        for item in self.items:
            if (
                item.temperature == temperature_category
                and item.style == style
                and item.category == category
            ):
                valid_items.append(item)

        if valid_items:
            chosen_item = random.choice(valid_items)
            return chosen_item
        else:
            return None

    def add_item(self):
        """
        Adds a new item to the ItemManager and saves it to the CSV file.

        Requires the user to enter the category, name, color, temperature, style, and weather of the item.
        """
        category = input("Enter the category of the item (jacket/shirt/pants/shoes): ")
        name = input("Enter the name of the item: ")
        color = input("Enter the color of the item: ")
        temperature = input("Enter the temperature category of the item (cold/medium/hot): ")
        weather = input("Is this item for rainy or sunny weather (rainy/sunny)? ")
        style = input("Enter the style category of the item (casual/formal): ")

        item = Item(category, name, color, temperature, style, weather)
        self.items.append(item)

        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category, name, color, temperature, style, weather])

        print("Item added successfully.")


item_manager = ItemManager("items.csv")
item_manager.load_items()

while True:
    """
    Giving the user option to chose to find, add or to quit the program

    Determines what is the choice and do expected results

    If the user inputs for weather and temperature are suitable for a jacket, then we will give 
    a combination that includes a jacket, otherwise, it will be just shirt, pants, and shoes.
    """
    action = input("Choose an action (find/add/quit): ").lower()

    if action == "find":
        today_temperature = int(input("What is the temperature today: "))
        today_style = input("What is the style today (casual/formal): ").lower()
        weather = input("Is it rainy or sunny outside? (rainy/sunny): ").lower()

        jacket = item_manager.choose_item(
            ItemManager.CATEGORY_JACKET, today_temperature, today_style
        )
        shirt = item_manager.choose_item(
            ItemManager.CATEGORY_SHIRT, today_temperature, today_style
        )
        pants = item_manager.choose_item(
            ItemManager.CATEGORY_PANTS, today_temperature, today_style
        )
        shoes = item_manager.choose_item(
            ItemManager.CATEGORY_SHOES, today_temperature, today_style
        )

        if weather == "rainy" or item_manager.temperature_check(today_temperature) == ItemManager.TEMPERATURE_COLD:
            print("Today's Outfit:")
            print(f"Jacket: {jacket}" if jacket else "Jacket: Sorry, no suitable jacket")
            print(f"Shirt: {shirt}" if shirt else "Shirt: Sorry, no suitable shirt")
            print(f"Pants: {pants}" if pants else "Pants: Sorry, no suitable pants")
            print(f"Shoes: {shoes}" if shoes else "Shoes: Sorry, no suitable shoes")
        else:
            print("Today's Outfit:")
            print(f"Shirt: {shirt}" if shirt else "Shirt: Sorry, no suitable shirt")
            print(f"Pants: {pants}" if pants else "Pants: Sorry, no suitable pants")
            print(f"Shoes: {shoes}" if shoes else "Shoes: Sorry, no suitable shoes")

    elif action == "add":
        item_manager.add_item()

    elif action == "quit":
        break

    else:
        print("Invalid action. Please choose again.")





