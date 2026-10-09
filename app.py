from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "undercover-secret-key-change-me"


BANQUE_MOTS = [
    # Animaux
    ("Chien", "Chat"), ("Cheval", "Âne"), ("Lion", "Tigre"),
    ("Dauphin", "Baleine"), ("Aigle", "Faucon"), ("Loup", "Renard"),
    ("Crapaud", "Grenouille"), ("Serpent", "Lézard"), ("Abeille", "Guêpe"),
    ("Papillon", "Mite"), ("Chouette", "Hibou"), ("Crabe", "Homard"),
    ("Moustique", "Mouche"), ("Pingouin", "Manchot"),
    ("Chameau", "Dromadaire"), ("Écureuil", "Hérisson"),
    ("Gorille", "Chimpanzé"), ("Ours", "Panda"), ("Singe", "Lémurien"),
    ("Poule", "Canard"), ("Mouton", "Chèvre"), ("Cochon", "Sanglier"),
    ("Oie", "Cygne"), ("Escargot", "Limace"),

    # Nourriture & Boissons
    ("Pomme", "Poire"), ("Thé", "Café"), ("Pizza", "Tarte"),
    ("Burger", "Kebab"), ("Pâtes", "Riz"), ("Chocolat", "Caramel"),
    ("Fraise", "Framboise"), ("Citron", "Orange"),
    ("Beurre", "Margarine"), ("Pain", "Brioche"), ("Eau", "Soda"),
    ("Bière", "Vin"), ("Crêpe", "Gaufre"), ("Gâteau", "Biscuit"),
    ("Glace", "Sorbet"), ("Lait", "Crème"), ("Miel", "Confiture"),
    ("Poulet", "Dinde"), ("Poisson", "Crevette"), ("Salade", "Soupe"),
    ("Carotte", "Navet"), ("Tomate", "Poivron"), ("Patate", "Frite"),
    ("Oignon", "Ail"), ("Fromage", "Yaourt"), ("Melon", "Pastèque"),
    ("Banane", "Ananas"), ("Pêche", "Abricot"), ("Cassis", "Myrtille"),
    ("Saucisson", "Jambon"), ("Chips", "Pop-corn"), ("Jus", "Sirop"),
    ("Ketchup", "Moutarde"), ("Mayonnaise", "Aïoli"),
    ("Nutella", "Pâte à tartiner"),

    # Objets & Vêtements
    ("Stylo", "Crayon"), ("Chaise", "Tabouret"), ("Table", "Bureau"),
    ("Lit", "Canapé"), ("Miroir", "Vitrage"), ("Porte", "Fenêtre"),
    ("Téléphone", "Tablette"), ("Couteau", "Ciseaux"),
    ("Cuillère", "Fourchette"), ("Verre", "Tasse"), ("Assiette", "Bol"),
    ("Chemise", "T-shirt"), ("Pantalon", "Short"), ("Veste", "Manteau"),
    ("Chaussette", "Collant"), ("Chaussure", "Basket"),
    ("Chapeau", "Casquette"), ("Écharpe", "Foulard"),
    ("Gant", "Mitaine"), ("Sac", "Valise"), ("Montre", "Horloge"),
    ("Lampe", "Bougie"), ("Clé", "Serrure"), ("Parapluie", "Parasol"),
    ("Serviette", "Tapis"), ("Coussin", "Oreiller"),
    ("Savon", "Shampoing"), ("Brosse", "Peigne"), ("Livre", "Cahier"),
    ("Clavier", "Souris"), ("Casque", "Écouteurs"),
    ("Lunettes", "Lentilles"), ("Bouteille", "Gourde"),
    ("Portefeuille", "Porte-monnaie"), ("Bague", "Bracelet"),

    # Transport & Lieux
    ("Avion", "Fusée"), ("Plage", "Piscine"), ("Voiture", "Camion"),
    ("Moto", "Scooter"), ("Vélo", "Trottinette"),
    ("Bateau", "Sous-marin"), ("Train", "Métro"), ("Bus", "Tramway"),
    ("Ville", "Village"), ("Maison", "Appartement"), ("Parc", "Jardin"),
    ("Forêt", "Jungle"), ("Montagne", "Colline"), ("Mer", "Océan"),
    ("Rivière", "Fleuve"), ("Lac", "Étang"), ("Île", "Presqu'île"),
    ("Désert", "Canyon"), ("Cinéma", "Théâtre"), ("Musée", "Galerie"),
    ("Restaurant", "Café"), ("Hôtel", "Auberge"),
    ("École", "Université"), ("Hôpital", "Clinique"),
    ("Banque", "Poste"), ("Gare", "Aéroport"),
    ("Supermarché", "Marché"), ("Boulangerie", "Pâtisserie"),
    ("Château", "Palais"), ("Église", "Cathédrale"),
    ("Stade", "Gymnase"), ("Pont", "Tunnel"),
    ("Camping", "Bungalow"), ("Zoo", "Aquarium"),
    ("Bibliothèque", "Médiathèque"),

    # Métiers & Loisirs
    ("Guitare", "Ukulélé"), ("Piano", "Synthétiseur"),
    ("Violon", "Violoncelle"), ("Batterie", "Tambour"),
    ("Football", "Rugby"), ("Tennis", "Badminton"),
    ("Course", "Marche"), ("Natation", "Plongée"),
    ("Ski", "Snowboard"), ("Médecin", "Infirmier"),
    ("Policier", "Gendarme"), ("Pompier", "Secouriste"),
    ("Professeur", "Instituteur"), ("Cuisinier", "Pâtissier"),
    ("Acteur", "Comédien"), ("Chanteur", "Musicien"),
    ("Peintre", "Sculpteur"), ("Écrivain", "Journaliste"),
    ("Avocat", "Juge"), ("Pilote", "Conducteur"),
    ("Photographe", "Cinéaste"), ("Danse", "Gymnastique"),
    ("Boxe", "Karaté"), ("Échecs", "Dames"),
    ("Jardinage", "Bricolage"), ("Couture", "Tricot"),
    ("Dessin", "Peinture"), ("Magie", "Jonglage"),
    ("Pêche", "Chasse"), ("Randonnée", "Escalade"),
    ("Surf", "Paddle"), ("Judo", "Lutte"),
    ("Vente", "Commerce"), ("Mécanicien", "Électricien"),
    ("Boulanger", "Boucher"),

    # Concepts
    ("Soleil", "Lune"), ("Étoile", "Planète"), ("Pluie", "Neige"),
    ("Vent", "Tempête"), ("Nuage", "Brouillard"), ("Jour", "Nuit"),
    ("Matin", "Soir"), ("Été", "Hiver"), ("Printemps", "Automne"),
    ("Feu", "Électricité"), ("Glace", "Vapeur"), ("Or", "Argent"),
    ("Diamant", "Rubis"), ("Riche", "Célèbre"), ("Rêve", "Cauchemar"),
    ("Rire", "Sourire"), ("Peur", "Angoisse"), ("Amour", "Amitié"),
    ("Guerre", "Combat"), ("Paix", "Silence"), ("Musique", "Chanson"),
    ("Film", "Série"), ("Roman", "Bande dessinée"),
    ("Journal", "Magazine"), ("Photo", "Tableau"),
    ("Histoire", "Légende"), ("Magie", "Sorcellerie"),
    ("Fantôme", "Monstre"), ("Château", "Forteresse"),
    ("Trésor", "Butin"), ("Roi", "Prince"), ("Reine", "Princesse"),
    ("Pirate", "Corsaire"), ("Robot", "Cyborg"),
    ("Espace", "Galaxie"),

    # Célébrités & Figures
    ("Napoléon", "Jules César"), ("Einstein", "Newton"),
    ("Mozart", "Beethoven"), ("Picasso", "Monet"),
    ("Cléopâtre", "Néfertiti"), ("Da Vinci", "Michel-Ange"),
    ("Sherlock Holmes", "Hercule Poirot"), ("Mickey", "Donald"),
    ("Batman", "Superman"), ("Harry Potter", "Frodon"),
    ("Darth Vader", "Voldemort"), ("Mario", "Sonic"),
    ("Shrek", "L'Ogre"), ("Père Noël", "Saint Nicolas"),
    ("Jeanne d'Arc", "Mulan"), ("Louis XIV", "Charlemagne"),
    ("Shakespeare", "Molière"), ("Barbie", "Ken"),
    ("Astérix", "Obélix"), ("Tintin", "Spirou"),
    ("Zorro", "Robin des Bois"), ("Spiderman", "Iron Man"),
    ("James Bond", "Ethan Hunt"), ("Tarzan", "Mowgli"),
    ("Dracula", "Frankenstein"), ("Zeus", "Poséidon"),
    ("Thor", "Loki"), ("Hercule", "Achille"),
    ("Charlie Chaplin", "Mr. Bean"), ("Michael Jackson", "Elvis Presley"),
    ("Elon Musk", "Steve Jobs"), ("Bill Gates", "Mark Zuckerberg"),
    ("Cristiano Ronaldo", "Messi"), ("Kylian Mbappé", "Neymar"),
    ("LeBron James", "Michael Jordan"),

    # Géographie
    ("France", "Italie"), ("Espagne", "Portugal"),
    ("Japon", "Chine"), ("Canada", "États-Unis"),
    ("Brésil", "Argentine"), ("Égypte", "Maroc"),
    ("Angleterre", "Écosse"), ("Australie", "Nouvelle-Zélande"),
    ("Allemagne", "Belgique"), ("Grèce", "Turquie"),
    ("Russie", "Ukraine"), ("Suisse", "Autriche"),
    ("Paris", "Londres"), ("Tokyo", "Pékin"),
    ("New York", "Los Angeles"), ("Rome", "Athènes"),
    ("Madrid", "Barcelone"), ("Berlin", "Vienne"),
    ("Sahara", "Gobi"), ("Everest", "Mont Blanc"),
    ("Amazone", "Nil"), ("Volcan", "Geyser"),
    ("Grotte", "Caverne"), ("Cascade", "Chute d'eau"),
    ("Banquise", "Glacier"), ("Atoll", "Récif"),
    ("Fjord", "Baie"), ("Toundra", "Savane"),
    ("Pôle Nord", "Pôle Sud"), ("Espace", "Cosmos"),

    # Technologie
    ("Ordinateur", "Serveur"), ("Console", "PC Gaming"),
    ("Écran", "Projecteur"), ("Wi-Fi", "Bluetooth"),
    ("Site web", "Application"), ("Réseau social", "Forum"),
    ("Instagram", "TikTok"), ("YouTube", "Twitch"),
    ("Netflix", "Disney+"), ("PlayStation", "Xbox"),
    ("iPhone", "Android"), ("Algorithme", "Code"),
    ("Drone", "Sonde"), ("Casque VR", "Lunettes 3D"),
    ("Batterie", "Pile"), ("USB", "Disque dur"),
    ("Caméra", "Webcam"), ("Jeu vidéo", "Jeu de société"),
    ("Manga", "Comics"), ("Anime", "Dessin animé"),
    ("Podcast", "Radio"), ("Selfie", "Portrait"),
    ("Emoji", "Sticker"), ("Lien", "Fichier"),
    ("Pixel", "Vecteur"), ("Spam", "Virus"),
    ("Hacker", "Gamer"), ("Mème", "Trend"),
    ("Avatar", "Pseudo"), ("Bug", "Glitch"),
    ("Cloud", "Serveur"), ("Laser", "Fibre optique"),
    ("Satellite", "Antenne"), ("Moteur de recherche", "Navigateur"),
    ("Intelligence Artificielle", "Robot"),

    # Corps humain
    ("Œil", "Oreille"), ("Nez", "Bouche"), ("Bras", "Jambe"),
    ("Main", "Pied"), ("Doigt", "Orteil"), ("Cœur", "Poumon"),
    ("Estomac", "Foie"), ("Cerveau", "Crâne"), ("Os", "Muscle"),
    ("Sang", "Salive"), ("Dent", "Langue"), ("Cheveux", "Barbe"),
    ("Ongle", "Griffe"), ("Peau", "Chair"), ("Dos", "Ventre"),
    ("Genou", "Coude"), ("Épaule", "Hanche"), ("Cou", "Gorge"),
    ("Veine", "Artère"), ("Visage", "Tête"), ("Squelette", "Fossile"),
    ("Larme", "Sueur"), ("Voix", "Souffle"), ("Pouls", "Tension"),
    ("Gêne", "ADN"), ("Cils", "Sourcils"), ("Poignet", "Cheville"),
    ("Menton", "Joue"), ("Sourire", "Grimace"), ("Rides", "Cicatrices"),

    # Événements
    ("Noël", "Pâques"), ("Halloween", "Carnaval"),
    ("Anniversaire", "Mariage"), ("Vacances", "Week-end"),
    ("Kermesse", "Festival"), ("Concert", "Spectacle"),
    ("Soirée", "Pyjama party"), ("Boom", "Rave"),
    ("Match", "Tournoi"), ("Cérémonie", "Gala"),
    ("Brocante", "Marché aux puces"), ("Carnaval", "Parade"),
    ("Feu d'artifice", "Pétard"), ("Réveillon", "Nouvel An"),
    ("Éclipse", "Aurore boréale"), ("Marathon", "Sprint"),
    ("Exposition", "Salon"), ("Manifestation", "Grève"),
    ("Conférence", "Réunion"), ("Picnic", "Barbecue"),
    ("Séjour", "Voyage"), ("Rentrée", "Fin d'année"),
    ("Aube", "Crépuscule"), ("Saison", "Époque"),
    ("Sieste", "Nuit blanche"), ("Pause", "Récréation"),
    ("Examen", "Test"), ("Diplôme", "Médaille"),
    ("Victoire", "Trophée"), ("Défilé", "Procession"),
    ("Pèlerinage", "Excursion"), ("Croisière", "Safari"),
    ("Camping", "Bivouac"), ("Bal", "Kermesse"),
    ("Fiesta", "Apéro"),

    # Émotions
    ("Joie", "Bonheur"), ("Tristesse", "Chagrin"),
    ("Colère", "Rage"), ("Chaud", "Froid"), ("Douceur", "Rude"),
    ("Faim", "Soif"), ("Fatigue", "Sommeil"), ("Stress", "Panique"),
    ("Calme", "Sérénité"), ("Doute", "Soupçon"),
    ("Espoir", "Illusion"), ("Jalousie", "Envie"),
    ("Honte", "Culpabilité"), ("Fierté", "Orgueil"),
    ("Courage", "Audace"), ("Lâcheté", "Peur"),
    ("Solitude", "Isolement"), ("Ennui", "Lassitude"),
    ("Surprise", "Étonnement"), ("Désir", "Passion"),
    ("Douleur", "Souffrance"), ("Plaisir", "Régal"),
    ("Lumière", "Clarté"), ("Ombre", "Pénombre"),
    ("Bruit", "Vacarme"), ("Odeur", "Parfum"),
    ("Goût", "Saveur"), ("Lourdeur", "Poids"),
    ("Vitesse", "Allure"), ("Force", "Puissance"),
    ("Faiblesse", "Fragilité"), ("Beauté", "Charme"),
    ("Magie", "Illusion"), ("Vérité", "Mensonge"),
    ("Justice", "Équité"),

    # Réseaux sociaux & Internet
    ("Snapchat", "BeReal"), ("Instagram", "Pinterest"),
    ("Discord", "WhatsApp"), ("Tinder", "Bumble"),
    ("Influenceur", "Youtubeur"), ("Story", "Publication"),
    ("Abonné", "Follower"), ("Vocal", "Message"),
    ("Vlog", "Storytime"), ("Notif", "DM"),
    ("Troll", "Hater"), ("Cringe", "Gênant"),

    # Gaming & culture geek
    ("Fortnite", "Valorant"), ("Minecraft", "Roblox"),
    ("FIFA", "Rocket League"), ("GTA", "Red Dead Redemption"),
    ("Call of Duty", "Battlefield"), ("Tryhard", "Chill"),
    ("Noob", "Débutant"), ("Skin", "Cosmétique"),
    ("Loot", "Récompense"), ("Ranked", "Classé"),
    ("Manette", "Clavier"), ("Speedrun", "Let's Play"),

    # Études & vie étudiante
    ("Partiel", "Contrôle"), ("Amphi", "Salle de classe"),
    ("Alternance", "Stage"), ("BDE", "Association"),
    ("Révisions", "Bachotage"), ("Absence", "Retard"),
    ("Rattrapage", "Seconde chance"), ("Crous", "Restaurant universitaire"),
    ("Coloc", "Résidence étudiante"), ("Prof absent", "Cours annulé"),
    ("Dossier", "Exposé"), ("Diplôme", "Certification"),

    # Soirées & vie sociale
    ("Before", "After"), ("Boîte", "Bar"),
    ("Festival", "Rave"), ("Soirée étudiante", "Soirée privée"),
    ("Karaoké", "Blind test"), ("Flirt", "Crush"),
    ("Date", "Rencard"), ("Plan cul", "Relation"),
    ("Groupe WhatsApp", "Groupe Snapchat"), ("Râteau", "Vu"),
    ("Afterwork", "Apéro"), ("Pote", "Meilleur ami"),

    # Mode & tendances
    ("Nike", "Adidas"), ("Jordan", "Yeezy"),
    ("Hoodie", "Sweat"), ("Oversize", "Slim"),
    ("Vintage", "Streetwear"), ("Sneakers", "Baskets"),
    ("Vinted", "Shein"), ("Drip", "Swag"),
    ("Coiffeur", "Barbier"), ("Parfum", "Déodorant"),
    ("Maquillage", "Skincare"), ("Outfit", "Look"),

    # Fast-food & consommation
    ("McDonald's", "Burger King"), ("KFC", "O'Tacos"),
    ("Tacos", "Kebab"), ("Starbucks", "Café du coin"),
    ("Red Bull", "Monster"), ("Uber Eats", "Deliveroo"),
    ("Sushi", "Poké bowl"), ("Bubble tea", "Milkshake"),
    ("Drive", "Livraison"), ("Menu Maxi", "Menu Best Of"),
    ("Cookie", "Brownie"), ("Nutella", "Oreo"),

    # Argot & expressions
    ("Wesh", "Wallah"), ("Banger", "Masterclass"),
    ("GOAT", "Légende"), ("Charo", "Forceur"),
    ("Boloss", "Kéké"), ("Zinzin", "Fou"),
    ("Flemme", "Fatigue"), ("Seum", "Dégoût"),
    ("Gênant", "Malaisant"), ("Sus", "Lou­che"),
    ("Miskine", "Dommage"), ("Ratio", "Clash"),

    # Culture pop & divertissement
    ("One Piece", "Naruto"), ("Jujutsu Kaisen", "Demon Slayer"),
    ("Stranger Things", "Wednesday"), ("Euphoria", "Elite"),
    ("The Walking Dead", "The Last of Us"), ("Marvel", "DC Comics"),
    ("Drake", "The Weeknd"), ("Jul", "Ninho"),
    ("Aya Nakamura", "Niska"), ("Squeezie", "Inoxtag"),
    ("Amixem", "Michou"), ("Werenoi", "Gazo"),

    # Argent & quotidien
    ("Virement", "Prélèvement"), ("PayPal", "Wero"),
    ("Carte bleue", "Espèces"), ("Économiser", "Dépenser"),
    ("Job étudiant", "Intérim"), ("Loyer", "Facture"),
    ("Radin", "Flambeur"), ("Salaire", "Argent de poche"),
    ("Black Friday", "Soldes"), ("Code promo", "Réduction"),
    
    # Anime
    ("Genki Dama", "Haki des Rois"), ("Zoro", "Sanji"),
    ("Grand Terrassement", "Séisme"), ("Eren", "Mikasa"),
    ("Titan Colossal", "Titan Charrette"), ("Shanks", "Mihawk"),
    ("Rasengan", "Chidori"), ("Extension du Territoire", "Grand Remplacement"),
    ("One for All", "All for One"), ("Death Note", "Geass"),
    ("Tanjiro", "Nezuko"), ("Mach 20", "Supervitesse"),
    
    # Films
    ("Titanic", "Pearl Harbor"), ("Jurassic Park", "King Kong"),
    ("Harry Potter", "Le Seigneur des Anneaux"), ("Ça", "Chucky"),
    ("Narnia", "Poudlard"), ("Shrek", "Monstre & Cie"),
    ("Taxi", "Le Transporteur"), ("La Reine des Neiges", "Raiponce"),
    ("Jack Sparrow", "Indiana Jones"), ("Astérix", "Obélix"),
    ("Fast and Furious", "Need For Speed"), ("Dobby", "Gollum"),
    
    # Séries
    ("Breaking Bad", "Prison Break"), ("The Walking Dead", "The Last of Us"),
    ("Sex Education", "365 jours"), ("Walter White", "Gus Fring"),
    ("Mercredi", "La Famille Addams"), ("The 100", "Le Labyrinthe"),
    ("Friends", "How I Met Your Mother"), ("Malcolm", "Ma Famille d'abord"),
    ("Ted", "Ted 2"), ("Plus Belle la vie", "Demain nous appartient"),
    ("Ahsoka", "Obi-Wan Kenobi"), ("Cobra Kai", "Karate Kid"),
    
    # Jeux vidéo
    ("FIFA", "EA FC"), ("Valorant", "Counter-Strike"),
    ("Fortnite", "Roblox"), ("AWP", "SSG 08"),
    ("Diamant", "Netherite"), ("Subnautica", "Raft"),
    ("F1", "Gran Turismo"), ("GTA V", "GTA VI"),
    ("Mario", "Sonic"), ("Pikachu", "Évoli"),
    ("Clash Royale", "Clash of Clans"), ("Skin", "Emote"),
]

# ---------------------------------------------------------
# OUTILS
# ---------------------------------------------------------

def generer_joueurs(noms, nb_civ, nb_und, nb_whi):
    mot_civil, mot_undercover = random.choice(BANQUE_MOTS)

    if random.choice((True, False)):
        mot_civil, mot_undercover = mot_undercover, mot_civil

    roles = (
        ["Civil"] * nb_civ
        + ["Undercover"] * nb_und
        + ["Mr. White"] * nb_whi
    )

    random.shuffle(roles)

    joueurs = []

    for nom, role in zip(noms, roles):
        if role == "Civil":
            mot = mot_civil
        elif role == "Undercover":
            mot = mot_undercover
        else:
            mot = "Tu es Mr. White !"

        joueurs.append({
            "nom": nom,
            "role": role,
            "mot": mot,
            "en_vie": True
        })

    return joueurs, mot_civil, mot_undercover


def verifier_victoire():
    joueurs = session["joueurs"]

    vivants = [j for j in joueurs if j["en_vie"]]

    civils = [j for j in vivants if j["role"] == "Civil"]

    imposteurs = [
        j for j in vivants
        if j["role"] in ["Undercover", "Mr. White"]
    ]

    if not imposteurs:
        return "civils"

    if len(civils) <= 1 and imposteurs:
        return "imposteurs"

    return None


# ---------------------------------------------------------
# ACCUEIL / CONFIGURATION
# ---------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/configuration", methods=["POST"])
def configuration():
    try:
        nb_tot = int(request.form["nb_joueurs"])
        nb_und = int(request.form["nb_undercover"])
        nb_whi = int(request.form["nb_white"])
    except (ValueError, KeyError):
        return render_template(
            "index.html",
            erreur="Veuillez entrer des nombres valides."
        )

    if nb_tot < 3:
        return render_template(
            "index.html",
            erreur="Il faut au moins 3 joueurs."
        )

    if nb_und < 0 or nb_whi < 0:
        return render_template(
            "index.html",
            erreur="Le nombre d'imposteurs ne peut pas être négatif."
        )

    if nb_tot == 3 and nb_und + nb_whi != 1:
        return render_template(
            "index.html",
            erreur="À 3 joueurs, choisissez 1 Undercover ou 1 Mr. White pour garder 2 civils."
        )

    if nb_und + nb_whi == 0:
        return render_template(
            "index.html",
            erreur="Il faut au moins un Undercover ou un Mr. White."
        )

    if nb_tot - nb_und - nb_whi < 2:
        return render_template(
            "index.html",
            erreur="Il faut au moins 2 civils."
        )

    session["configuration"] = {
        "nb_tot": nb_tot,
        "nb_und": nb_und,
        "nb_whi": nb_whi,
        "nb_civ": nb_tot - nb_und - nb_whi
    }

    return redirect(url_for("prenoms"))


# ---------------------------------------------------------
# PRÉNOMS
# ---------------------------------------------------------

@app.route("/prenoms")
def prenoms():
    config = session.get("configuration")

    if not config:
        return redirect(url_for("index"))

    return render_template(
        "prenoms.html",
        nombre=config["nb_tot"]
    )


@app.route("/lancer", methods=["POST"])
def lancer():
    config = session.get("configuration")

    if not config:
        return redirect(url_for("index"))

    noms = []

    for i in range(config["nb_tot"]):
        nom = request.form.get(f"joueur_{i}", "").strip()

        if not nom:
            nom = f"Joueur {i + 1}"

        noms.append(nom)

    joueurs, mot_civil, mot_undercover = generer_joueurs(
        noms,
        config["nb_civ"],
        config["nb_und"],
        config["nb_whi"]
    )

    session["joueurs"] = joueurs
    session["mot_civil"] = mot_civil
    session["mot_undercover"] = mot_undercover
    session["index_decouverte"] = 0
    ordre_decouverte = list(range(len(joueurs)))
    random.shuffle(ordre_decouverte)
    session["ordre_decouverte"] = ordre_decouverte
    session.pop("ordre_vote", None)

    return redirect(url_for("decouverte"))


# ---------------------------------------------------------
# DISTRIBUTION DES MOTS
# ---------------------------------------------------------

@app.route("/decouverte")
def decouverte():
    joueurs = session.get("joueurs")

    if not joueurs:
        return redirect(url_for("index"))

    ordre_decouverte = session.get("ordre_decouverte")
    if not ordre_decouverte or len(ordre_decouverte) != len(joueurs):
        ordre_decouverte = list(range(len(joueurs)))
        random.shuffle(ordre_decouverte)
        session["ordre_decouverte"] = ordre_decouverte

    index = session.get("index_decouverte", 0)

    if index >= len(ordre_decouverte):
        return redirect(url_for("jeu"))

    joueur = joueurs[ordre_decouverte[index]]

    return render_template(
        "decouverte.html",
        joueur=joueur,
        index=index,
        total=len(joueurs)
    )


@app.route("/decouverte/suivant", methods=["POST"])
def decouverte_suivant():
    session["index_decouverte"] = session.get(
        "index_decouverte", 0
    ) + 1

    return redirect(url_for("decouverte"))


# ---------------------------------------------------------
# JEU / VOTE
# ---------------------------------------------------------

@app.route("/jeu")
def jeu():
    joueurs = session.get("joueurs")

    if not joueurs:
        return redirect(url_for("index"))

    victoire = verifier_victoire()

    if victoire:
        return redirect(url_for("fin"))

    indices_vivants = [
        index for index, joueur in enumerate(joueurs)
        if joueur["en_vie"]
    ]
    ordre_vote = session.get("ordre_vote")

    if ordre_vote is None or set(ordre_vote) != set(indices_vivants):
        random.shuffle(indices_vivants)
        ordre_vote = indices_vivants
        session["ordre_vote"] = ordre_vote

    vivants = [(index, joueurs[index]) for index in ordre_vote]

    return render_template(
        "jeu.html",
        joueurs=vivants
    )


@app.route("/mot/<int:index>")
def voir_mot(index):
    joueurs = session.get("joueurs")

    if not joueurs:
        return redirect(url_for("index"))

    if index < 0 or index >= len(joueurs) or not joueurs[index]["en_vie"]:
        return redirect(url_for("jeu"))

    return render_template("mot.html", joueur=joueurs[index])


@app.route("/eliminer/<int:index>", methods=["POST"])
def eliminer(index):
    joueurs = session.get("joueurs")

    if not joueurs:
        return redirect(url_for("index"))

    if index < 0 or index >= len(joueurs):
        return redirect(url_for("jeu"))

    joueur = joueurs[index]

    if not joueur["en_vie"]:
        return redirect(url_for("jeu"))

    joueur["en_vie"] = False

    session["joueurs"] = joueurs
    session["joueur_elimine"] = joueur

    if joueur["role"] == "Mr. White":
        return redirect(url_for("white"))

    return redirect(url_for("elimination"))


# ---------------------------------------------------------
# ÉLIMINATION
# ---------------------------------------------------------

@app.route("/elimination")
def elimination():
    joueur = session.get("joueur_elimine")

    if not joueur:
        return redirect(url_for("jeu"))

    return render_template(
        "elimination.html",
        joueur=joueur
    )


# ---------------------------------------------------------
# MR WHITE
# ---------------------------------------------------------

@app.route("/white")
def white():
    joueur = session.get("joueur_elimine")

    if not joueur:
        return redirect(url_for("jeu"))

    return render_template(
        "white.html",
        joueur=joueur
    )


@app.route("/white/verifier", methods=["POST"])
def verifier_white():
    proposition = request.form.get("proposition", "").strip().lower()
    mot_civil = session["mot_civil"].lower()

    if proposition == mot_civil:
        session["white_gagne"] = True
        return redirect(url_for("fin"))

    return redirect(url_for("elimination"))


# ---------------------------------------------------------
# FIN
# ---------------------------------------------------------

@app.route("/fin")
def fin():
    victoire = verifier_victoire()

    white_gagne = session.get("white_gagne", False)

    if white_gagne:
        message = "MR. WHITE A DEVINÉ LE MOT ET GAGNE !"
    elif victoire == "civils":
        message = "VICTOIRE DES CIVILS !"
    elif victoire == "imposteurs":
        message = "VICTOIRE DES IMPOSTEURS !"
    else:
        message = "FIN DE LA PARTIE !"

    return render_template(
        "fin.html",
        message=message,
        mot_civil=session.get("mot_civil", ""),
        mot_undercover=session.get("mot_undercover", ""),
        joueurs=session.get("joueurs", [])
    )

# ---------------------------------------------------------
# REJOUER
# ---------------------------------------------------------

@app.route("/rejouer")
def rejouer():
    joueurs = session.get("joueurs")
    config = session.get("configuration")

    if not joueurs or not config:
        return redirect(url_for("index"))

    noms = [j["nom"] for j in joueurs]

    joueurs, mot_civil, mot_undercover = generer_joueurs(
        noms,
        config["nb_civ"],
        config["nb_und"],
        config["nb_whi"]
    )

    session["joueurs"] = joueurs
    session["mot_civil"] = mot_civil
    session["mot_undercover"] = mot_undercover
    session["index_decouverte"] = 0
    ordre_decouverte = list(range(len(joueurs)))
    random.shuffle(ordre_decouverte)
    session["ordre_decouverte"] = ordre_decouverte
    session.pop("ordre_vote", None)
    session["white_gagne"] = False
    session.pop("joueur_elimine", None)

    return redirect(url_for("decouverte"))


# ---------------------------------------------------------
# NOUVELLE PARTIE
# ---------------------------------------------------------

@app.route("/nouvelle-partie")
def nouvelle_partie():
    session.clear()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )