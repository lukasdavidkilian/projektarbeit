from food_class import Food

nutrition_set_1 = []
nutrition_set_2 = []
nutrition_set_5 = []
nutrition_set_4 = []
nutrition_set_3 = []

rinderhackfleisch = Food("Rinderhackfleisch", 25, 9, 0, 100, "g", [2.5, 3, 3.5, 4])
rindertartar = Food("Rindertartar", 21, 3, 0, 100, "g", [2.5, 3, 3.5, 4])
rinderfilet = Food("Rinderfilet", 29.7, 4.3, 0, 100, "g", [2, 2.5])
rinderleber = Food("Rinderleber", 19.2, 3.7, 5.3, 100, "g", [2, 3])
haehnchenbrust = Food("Hähnchenbrust", 30, 0, 0, 100, "g", [2.5, 3, 3.5, 4])
huehnerherzen = Food("Hühnerherzen", 16, 5, 0, 100, "g", [2])
putenbrust = Food("Putenbrust", 30, 1, 0, 100, "g", [2.5, 3, 3.5, 4])
bauernschinken = Food("Bauernschinken", 26.3, 6.8, 1.1, 100, "g", [0.75, 1])
bacon = Food("Bacon", 14, 28, 0.5, 100, "g", [0.5, 0.75])
salami = Food("Salami", 19, 33, 3, 100, "g", [0.7])
lachs = Food("Lachs", 20, 13, 0, 100, "g", [1.25, 2.5])
seelachs = Food("Seelachs", 17, 0.6, 0, 100, "g", [2])
forelle = Food("Forelle", 20, 3, 0, 100, "g", [2])
garnelen = Food("Garnelen", 18.6, 1.4, 0, 100, "g", [1.25, 2.5])
eier = Food("Eier", 7.5, 6.5, 1, 1, "", [3, 4, 5])
milch = Food("Milch", 3.3, 4, 4.8, 100, "ml", [2.5, 3, 3.5, 4])
kaese = Food("Käse", 30, 23, 0.1, 100, "g", [0.75, 1])
gouda = Food("Gouda", 22, 30.8, 0, 100, "g", [0.75, 1])
feta = Food("Feta", 17, 22, 0.5, 100, "g", [0.5, 1])
joghurt = Food("Naturjoghurt 3,5%", 4.4, 3.5, 5.1, 100, "g", [2, 2.5])
skyr = Food("Skyr", 11, 0.2, 4, 100, "g", [5])
magerquark = Food("Magerquark", 12, 0.2, 4, 100, "g", [2.5, 5])
parmesan = Food("Parmesan", 32.3, 35, 0, 100, "g", [0.75, 1])
roteLinsen = Food("Rote Linsen", 26.7, 1.5, 57.8, 100, "g", [1, 2, 3])
kichererbsen = Food("Kichererbsen", 20, 7, 45, 100, "g", [1, 2, 3])
kidneybohnen = Food("Kidneybohnen", 21, 1, 36.5, 100, "g", [0.75, 1])
isoclear = Food("ESN Isoclear Whey Isolate", 85, 0, 1, 100, "g", [0.3, 0.4])

reis = Food("Basmati Reis", 8.8, 1, 75, 100, "g", [0.75, 1])
reisflocken = Food("Reisflocken", 8.8, 1, 75, 100, "g", [0.5, 0.75, 1])
haferflocken = Food("Haferflocken", 14, 7, 56, 100, "g", [1])
cornflakes = Food("Cornflakes, ungezuckert", 7.3, 1.2, 82, 100, "g", [1, 1.5])
milchreis = Food("Milchreis ohne Milch", 8.8, 1, 75, 100, "g", [0.75, 1])
pirincreis = Food("Pirinc Reis", 7.9, 1.2, 77.8, 100, "g", [0.75, 1])
kartoffeln = Food("Kartoffeln", 2, 0, 17, 100, "g", [4, 5, 6])
suesskartoffeln = Food("Süßkartoffeln", 1.6, 0.6, 24, 100, "g", [4, 5, 6])
buchweizen = Food("Buchweizen", 10, 2, 70, 100, "g", [0.5, 1])
honig = Food("Honig", 0, 0, 80, 100, "g", [0.2, 0.3, 0.4])
banane = Food("Banane", 1.1, 0.3, 22.8, 100, "g", [1, 2])
apfel = Food("Apfel", 0.3, 0.2, 14, 100, "g", [1.5])
blaubeeren = Food("Blaubeeren", 0.6, 0.6, 7.4, 100, "g", [1, 1.5, 2])
mango = Food("Mango", 2, 0.2, 13, 100, "g", [2, 2.5])
maracuja = Food("Maracuja", 2.2, 0.5, 11.8, 100, "g", [0.8])
reiswaffeln = Food("Reiswaffeln", 8, 3.6, 80.2, 100, "g", [0.15, 0.3, 0.45])
spinat = Food("Spinat", 2.8, 0.3, 0.6, 100, "g", [1, 1.5, 2])
blumenkohl = Food("Blumenkohl", 1.9, 0, 2, 100, "g", [1, 1.5, 2])
paprikarot = Food("Rote Paprika", 1.3, 0.5, 6.4, 100, "g", [1, 2, 3])
paprikagelb = Food("Gelbe Paprika", 1, 0, 5, 100, "g", [1, 2, 3])
paprikagrün = Food("Grüne Paprika", 1, 0, 2, 100, "g", [1, 2, 3])
karotte = Food("Karotte", 1, 0.2, 4.8, 100, "g", [0.8])
tomate = Food("Tomate", 0.7, 3.5, 0.1, 100, "g", [0.5, 1])
gurke = Food("Gurke", 0.6, 0.2, 1.8, 100, "g", [0.5, 1])
beerenmischung = Food("Beerenmischung TK", 1.4, 0.6, 12.1, 100, "g", [0.5, 1, 1.5])
mandarine = Food("Mandarine", 0.7, 0.2, 10, 100, "g", [1, 2, 3])
orange = Food("Orange", 1, 0.2, 8.2, 100, "g", [1.5, 3])
birne = Food("Mandarine", 1, 0.2, 11, 100, "g", [1, 2, 3])
ananas = Food("Ananas", 0.5, 0.2, 12.4, 100, "g", [1, 2, 3])
dattel = Food("Dattel getrocknet", 1.85, 0.5, 65, 100, "g", [0.1, 0.2, 0.3])
ketchup = Food("Ketchup", 2, 0.3, 24, 100, "g", [0.15, 0.3])
sriracha = Food("Sriracha", 1.8, 1.3, 23, 100, "g", [0.15, 0.3])
sojasauce = Food("Sojasauce glutenfrei", 10, 0, 2, 100, "g", [0.2, 0.4])
gehackteTomaten = Food("Tomaten gehackt", 1.1, 0.1, 3, 100, "g", [2, 3, 4])
raeuchertofu = Food("Räuchertofu", 19, 9, 2.8, 100, "g", [1, 2])
nudeln = Food("Nudeln", 12.5, 1.5, 71.7, 100, "g", [1, 1.5])

nusskernmischung = Food("Nusskernmischung", 21, 56, 11, 100, "g", [0.3])
walnuesse = Food("Walnüsse", 16, 71, 6, 100, "g", [0.3])
avocado = Food("Avocado", 2, 15, 9, 100, "g", [1.5, 2])
olivenoel = Food("Olivenöl", 0, 100, 0.2, 100, "g", [0.15, 0.3, 0.45])
butterschmalz = Food("Butterschmalz", 0.3, 100, 0, 100, "g", [0.15])
butter = Food("Butter", 0.7, 83.2, 0.7, 100, "g", [0.15])
hummus = Food("Hummus", 7.9, 9.6, 14.3, 100, "g", [0.25, 0.5, 0.75])
mandelmus = Food("Mandelmus", 21, 52, 19, 100, "g", [0.15, 0.3])

nutrition_set_1 = [rinderhackfleisch, haehnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch, kaese,
                   reis, kartoffeln, suesskartoffeln, buchweizen, honig, banane, apfel, nusskernmischung]
nutrition_set_2 = [rinderhackfleisch, haehnchenbrust, putenbrust, bauernschinken, eier, milch, kaese, reis, kartoffeln,
                   suesskartoffeln, honig, banane, apfel, nusskernmischung]
nutrition_set_3 = [rinderhackfleisch, haehnchenbrust, rinderfilet, putenbrust, eier, milch, kaese, reis, kartoffeln,
                   suesskartoffeln, honig, banane, apfel, walnuesse, avocado]
nutrition_set_4 = [rinderhackfleisch, haehnchenbrust, putenbrust, seelachs, milch, kaese, joghurt, reis, nudeln, banane,
                   honig, reis, nudeln, nusskernmischung]
nutrition_set_5 = [joghurt, rinderhackfleisch, haehnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch,
                   kaese, reis, kartoffeln, suesskartoffeln, honig, banane, apfel, nusskernmischung, avocado, olivenoel,
                   mandelmus]

food_lists = {
    "1": nutrition_set_1,
    "2": nutrition_set_2,
    "3": nutrition_set_3,
    "4": nutrition_set_4,
    "5": nutrition_set_5
}

food_count_per_set = {}

food_names_per_set = {}

for set_name, food_set in food_lists.items():
    food_count = len(food_set)

    food_names = [food.name for food in food_set]

    food_count_per_set[set_name] = food_count
    food_names_per_set[set_name] = food_names

for set_name, count in food_count_per_set.items():
    print(f"Anzahl der Lebensmittel im Set '{set_name}': {count}")

for set_name, names in food_names_per_set.items():
    print(f"Lebensmittel im Set '{set_name}': {', '.join(names)}")
