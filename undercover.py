import random
import customtkinter as ctk

# Configuration du thème
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

BANQUE_MOTS = [
    # Animaux
    ("Chien", "Chat"), ("Cheval", "Âne"), ("Lion", "Tigre"), ("Dauphin", "Baleine"),
    ("Aigle", "Faucon"), ("Loup", "Renard"), ("Crapaud", "Grenouille"), ("Serpent", "Lézard"),
    ("Abeille", "Guêpe"), ("Papillon", "Mite"), ("Chouette", "Hibou"), ("Crabe", "Homard"),
    ("Moustique", "Mouche"), ("Pingouin", "Manchot"), ("Chameau", "Dromadaire"), ("Écureuil", "Hérisson"),
    ("Gorille", "Chimpanzé"), ("Ours", "Panda"), ("Singe", "Lémurien"), ("Poule", "Canard"),
    ("Mouton", "Chèvre"), ("Cochon", "Sanglier"), ("Oie", "Cygne"), ("Escargot", "Limace"),
    # Nourriture & Boissons
    ("Pomme", "Poire"), ("Thé", "Café"), ("Pizza", "Tarte"), ("Burger", "Kebab"),
    ("Pâtes", "Riz"), ("Chocolat", "Caramel"), ("Fraise", "Framboise"), ("Citron", "Orange"),
    ("Beurre", "Margarine"), ("Pain", "Brioche"), ("Eau", "Soda"), ("Bière", "Vin"),
    ("Crêpe", "Gaufre"), ("Gâteau", "Biscuit"), ("Glace", "Sorbet"), ("Lait", "Crème"),
    ("Miel", "Confiture"), ("Poulet", "Dinde"), ("Poisson", "Crevette"), ("Salade", "Soupe"),
    ("Carotte", "Navet"), ("Tomate", "Poivron"), ("Patate", "Frite"), ("Oignon", "Ail"),
    ("Fromage", "Yaourt"), ("Melon", "Pastèque"), ("Banane", "Ananas"), ("Pêche", "Abricot"),
    ("Cassis", "Myrtille"), ("Saucisson", "Jambon"), ("Chips", "Pop-corn"), ("Jus", "Sirop"),
    ("Ketchup", "Moutarde"), ("Mayonnaise", "Aïoli"), ("Nutella", "Pâte à tartiner"),
    # Objets & Vêtements
    ("Stylo", "Crayon"), ("Chaise", "Tabouret"), ("Table", "Bureau"), ("Lit", "Canapé"),
    ("Miroir", "Vitrage"), ("Porte", "Fenêtre"), ("Téléphone", "Tablette"), ("Couteau", "Ciseaux"),
    ("Cuillère", "Fourchette"), ("Verre", "Tasse"), ("Assiette", "Bol"), ("Chemise", "T-shirt"),
    ("Pantalon", "Short"), ("Veste", "Manteau"), ("Chaussette", "Collant"), ("Chaussure", "Basket"),
    ("Chapeau", "Casquette"), ("Écharpe", "Foulard"), ("Gant", "Mitaine"), ("Sac", "Valise"),
    ("Montre", "Horloge"), ("Lampe", "Bougie"), ("Clé", "Serrure"), ("Parapluie", "Parasol"),
    ("Serviette", "Tapis"), ("Coussin", "Oreiller"), ("Savon", "Shampoing"), ("Brosse", "Peigne"),
    ("Livre", "Cahier"), ("Clavier", "Souris"), ("Casque", "Écouteurs"), ("Lunettes", "Lentilles"),
    ("Bouteille", "Gourde"), ("Portefeuille", "Porte-monnaie"), ("Bague", "Bracelet"),
    # Transport & Lieux
    ("Avion", "Fusée"), ("Plage", "Piscine"), ("Voiture", "Camion"), ("Moto", "Scooter"),
    ("Vélo", "Trottinette"), ("Bâteau", "Sous-marin"), ("Train", "Métro"), ("Bus", "Tramway"),
    ("Ville", "Village"), ("Maison", "Appartement"), ("Parc", "Jardin"), ("Forêt", "Jungle"),
    ("Montagne", "Colline"), ("Mer", "Océan"), ("Rivière", "Fleuve"), ("Lac", "Étang"),
    ("Île", "Presqu'île"), ("Désert", "Canyon"), ("Cinéma", "Théâtre"), ("Musée", "Galerie"),
    ("Restaurant", "Café"), ("Hôtel", "Auberge"), ("École", "Université"), ("Hôpital", "Clinique"),
    ("Banque", "Poste"), ("Gare", "Aéroport"), ("Supermarché", "Marché"), ("Boulangerie", "Pâtisserie"),
    ("Château", "Palais"), ("Église", "Cathédrale"), ("Stade", "Gymnase"), ("Pont", "Tunnel"),
    ("Camping", "Bungalow"), ("Zoo", "Aquarium"), ("Bibliothèque", "Médiathèque"),
    # Métiers & Loisirs
    ("Guitare", "Ukulélé"), ("Piano", "Synthétiseur"), ("Violon", "Violoncelle"), ("Batterie", "Tambour"),
    ("Football", "Rugby"), ("Tennis", "Badminton"), ("Course", "Marche"), ("Natation", "Plongée"),
    ("Ski", "Snowboard"), ("Médecin", "Infirmier"), ("Policier", "Gendarme"), ("Pompier", "Secouriste"),
    ("Professeur", "Instituteur"), ("Cuisinier", "Pâtissier"), ("Acteur", "Comédien"), ("Chanteur", "Musicien"),
    ("Peintre", "Sculpteur"), ("Écrivain", "Journaliste"), ("Avocat", "Juge"), ("Pilote", "Conducteur"),
    ("Photographe", "Cinéaste"), ("Danse", "Gymnastique"), ("Boxe", "Karaté"), ("Échecs", "Dames"),
    ("Jardinage", "Bricolage"), ("Couture", "Tricot"), ("Dessin", "Peinture"), ("Magie", "Jonglage"),
    ("Pêche", "Chasse"), ("Randonnée", "Escalade"), ("Surf", "Paddle"), ("Judo", "Lutte"),
    ("Vente", "Commerce"), ("Mécanicien", "Électricien"), ("Boulanger", "Boucher"),
    # Concepts & Divers
    ("Soleil", "Lune"), ("Étoile", "Planète"), ("Pluie", "Neige"), ("Vent", "Tempête"),
    ("Nuage", "Brouillard"), ("Jour", "Nuit"), ("Matin", "Soir"), ("Été", "Hiver"),
    ("Printemps", "Automne"), ("Feu", "Électricité"), ("Glace", "Vapeur"), ("Or", "Argent"),
    ("Diamant", "Rubis"), ("Riche", "Célèbre"), ("Rêve", "Cauchemar"), ("Rire", "Sourire"),
    ("Peur", "Angoisse"), ("Amour", "Amitié"), ("Guerre", "Combat"), ("Paix", "Silence"),
    ("Musique", "Chanson"), ("Film", "Série"), ("Roman", "Bande dessinée"), ("Journal", "Magazine"),
    ("Photo", "Tableau"), ("Histoire", "Légende"), ("Magie", "Sorcellerie"), ("Fantôme", "Monstre"),
    ("Château", "Forteresse"), ("Trésor", "Butin"), ("Roi", "Prince"), ("Reine", "Princesse"),
    ("Pirate", "Corsaire"), ("Robot", "Cyborg"), ("Espace", "Galaxie"),
    # Célébrités & Figures Historiques
    ("Napoléon", "Jules César"), ("Einstein", "Newton"), ("Mozart", "Beethoven"),
    ("Picasso", "Monet"), ("Cleopâtre", "Nefertiti"), ("Da Vinci", "Michel-Ange"),
    ("Sherlock Holmes", "Hercule Poirot"), ("Mickey", "Donald"), ("Batman", "Superman"),
    ("Harry Potter", "Frodon"), ("Darth Vader", "Voldemort"), ("Mario", "Sonic"),
    ("Shrek", "L'Ogre"), ("Père Noël", "Saint Nicolas"), ("Jeanne d'Arc", "Mulan"),
    ("Louis XIV", "Charlemagne"), ("Shakespeare", "Molière"), ("Barbie", "Ken"),
    ("Asterix", "Obelix"), ("Tintin", "Spirou"), ("Zorro", "Robin des Bois"),
    ("Spiderman", "Iron Man"), ("James Bond", "Ethan Hunt"), ("Tarzan", "Mowgli"),
    ("Dracula", "Frankenstein"), ("Zeus", "Poséidon"), ("Thor", "Loki"),
    ("Hercule", "Achille"), ("Charly Chaplin", "Mr. Bean"), ("Michael Jackson", "Elvis Presley"),
    ("Elon Musk", "Steve Jobs"), ("Bill Gates", "Mark Zuckerberg"), ("Cristiano Ronaldo", "Messi"),
    ("Kylian Mbappé", "Neymar"), ("Le Bron James", "Michael Jordan"),
    # Geographie & Pays
    ("France", "Italie"), ("Espagne", "Portugal"), ("Japon", "Chine"),
    ("Canada", "États-Unis"), ("Brésil", "Argentine"), ("Égypte", "Maroc"),
    ("Angleterre", "Écosse"), ("Australie", "Nouvelle-Zélande"), ("Allemagne", "Belgique"),
    ("Grèce", "Turquie"), ("Russie", "Ukraine"), ("Suisse", "Autriche"),
    ("Paris", "Londres"), ("Tokyo", "Pékin"), ("New York", "Los Angeles"),
    ("Rome", "Athènes"), ("Madrid", "Barcelone"), ("Berlin", "Vienne"),
    ("Sahara", "Gobi"), ("Everest", "Mont Blanc"), ("Amazone", "NIL"),
    ("Volcan", "Geyser"), ("Grotte", "Caverne"), ("Cascade", "Chute d'eau"),
    ("Banquise", "Glacier"), ("Atoll", "Récif"), ("Fjord", "Baie"),
    ("Toundra", "Savane"), ("Pôle Nord", "Pôle Sud"), ("Espace", "Cosmos"),
    # Technologie & Pop Culture
    ("Ordinateur", "Serveur"), ("Console", "PC Gaming"), ("Écran", "Projecteur"),
    ("Wi-Fi", "Bluetooth"), ("Site web", "Application"), ("Réseau social", "Forum"),
    ("Instagram", "TikTok"), ("YouTube", "Twitch"), ("Netflix", "Disney+"),
    ("PlayStation", "Xbox"), ("iPhone", "Android"), ("Algorithme", "Code"),
    ("Drone", "Sonde"), ("Casque VR", "Lunettes 3D"), ("Batterie", "Pile"),
    ("USB", "Disque dur"), ("Caméra", "Webcam"), ("Jeu vidéo", "Jeu de société"),
    ("Manga", "Comics"), ("Anime", "Dessin animé"), ("Podcast", "Radio"),
    ("Selfie", "Portrait"), ("Emoji", "Sticker"), ("Lien", "Fichier"),
    ("Pixel", "Vecteur"), ("Spam", "Virus"), ("Hacker", "Gamer"),
    ("Mème", "Trend"), ("Avatar", "Pseudo"), ("Bug", "Glitch"),
    ("Cloud", "Serveur"), ("Laser", "Fibre optique"), ("Satellite", "Antenne"),
    ("Moteur de recherche", "Navigateur"), ("Intelligence Artificielle", "Robot"),
    # Anatomie & Corps Humain
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
    # Événements, Fêtes & Moments
    ("Noël", "Pâques"), ("Halloween", "Carnaval"), ("Anniversaire", "Mariage"),
    ("Vacances", "Week-end"), ("Kermesse", "Festival"), ("Concert", "Spectacle"),
    ("Soirée", "Pyjama party"), ("Boom", "Rave"), ("Match", "Tournoi"),
    ("Cérémonie", "Gala"), ("Brocante", "Marché aux puces"), ("Carnaval", "Parade"),
    ("Feu d'artifice", "Pétard"), ("Réveillon", "Nouvel An"), ("Éclipse", "Aurore boréale"),
    ("Marathon", "Sprint"), ("Exposition", "Salon"), ("Manifestation", "Grève"),
    ("Conférence", "Réunion"), ("Picnic", "Barbecue"), ("Séjour", "Voyage"),
    ("Rentrée", "Fin d'année"), ("Aube", "Crépuscule"), ("Saison", "Époque"),
    ("Sieste", "Nuit blanche"), ("Pause", "Récréation"), ("Examen", "Test"),
    ("Diplôme", "Médaille"), ("Victoire", "Trophée"), ("Défilé", "Procession"),
    ("Pèlerinage", "Excursion"), ("Croisière", "Safari"), ("Camping", "Bivouac"),
    ("Bal", "Kermesse"), ("Fiesta", "Apéro"),
    # Sensations, Émotions & États
    ("Joie", "Bonheur"), ("Tristesse", "Chagrin"), ("Colère", "Rage"),
    ("Chaud", "Froid"), ("Douceur", "Rude"), ("Faim", "Soif"),
    ("Fatigue", "Sommeil"), ("Stress", "Panique"), ("Calme", "Sérénité"),
    ("Doute", "Soupçon"), ("Espoir", "Illusion"), ("Jalousie", "Envie"),
    ("Honte", "Culpabilité"), ("Fierté", "Orgueil"), ("Courage", "Audace"),
    ("Lâcheté", "Peur"), ("Solitude", "Isolement"), ("Ennui", "Lassitude"),
    ("Surprise", "Étonnement"), ("Désir", "Passions"), ("Douleur", "Souffrance"),
    ("Plaisir", "Régale"), ("Lumière", "Clarté"), ("Ombre", "Pénombre"),
    ("Bruit", "Vacarme"), ("Odeur", "Parfum"), ("Goût", "Saveur"),
    ("Lourdeur", "Poids"), ("Vitesse", "Allure"), ("Force", "Puissance"),
    ("Faiblesse", "Fragilité"), ("Beauté", "Charme"), ("Magie", "Illusion"),
    ("Vérité", "Mensonge"), ("Justice", "Équité")
]

class UndercoverApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Undercover - Jeu de Déduction")
        self.geometry("550x650")
        self.resizable(False, False)

        self.joueurs = []
        self.mot_civil = ""
        self.mot_undercover = ""
        self.index_decouverte = 0

        self.afficher_ecran_config()

    def nettoyer_ecran(self):
        for widget in self.winfo_children():
            widget.destroy()

    # --- ÉCRAN 1 : CONFIGURATION ---
    def afficher_ecran_config(self):
        self.nettoyer_ecran()

        titre = ctk.CTkLabel(self, text="UNDERCOVER", font=("Helvetica", 32, "bold"))
        titre.pack(pady=20)

        # Entrées numériques
        frame_inputs = ctk.CTkFrame(self)
        frame_inputs.pack(pady=10, padx=20, fill="x")

        self.entree_nb_joueurs = self.creer_champ_num(frame_inputs, "Nombre total de joueurs :", "4")
        self.entree_nb_undercover = self.creer_champ_num(frame_inputs, "Nombre d'Undercovers :", "1")
        self.entree_nb_white = self.creer_champ_num(frame_inputs, "Nombre de Mr. White :", "0")

        btn_valider = ctk.CTkButton(self, text="Saisir les prénoms", command=self.valider_config, font=("Helvetica", 16, "bold"))
        btn_valider.pack(pady=20)

        self.lbl_erreur = ctk.CTkLabel(self, text="", text_color="red", font=("Helvetica", 12))
        self.lbl_erreur.pack()

    def creer_champ_num(self, parent, label_text, default_val):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(pady=5, fill="x", padx=10)
        lbl = ctk.CTkLabel(frame, text=label_text, font=("Helvetica", 14))
        lbl.pack(side="left")
        entry = ctk.CTkEntry(frame, width=60)
        entry.insert(0, default_val)
        entry.pack(side="right")
        return entry

    def valider_config(self):
        try:
            nb_tot = int(self.entree_nb_joueurs.get())
            nb_und = int(self.entree_nb_undercover.get())
            nb_whi = int(self.entree_nb_white.get())
        except ValueError:
            self.lbl_erreur.configure(text="Veuillez entrer des nombres valides.")
            return

        nb_civ = nb_tot - nb_und - nb_whi
        if nb_civ <= 0:
            self.lbl_erreur.configure(text="Il faut au moins 1 Civil !")
            return

        self.nb_tot, self.nb_und, self.nb_whi, self.nb_civ = nb_tot, nb_und, nb_whi, nb_civ
        self.afficher_ecran_prenoms()

    # --- ÉCRAN 2 : PRÉNOMS ---
    def afficher_ecran_prenoms(self):
        self.nettoyer_ecran()

        lbl = ctk.CTkLabel(self, text="Prénoms des joueurs", font=("Helvetica", 24, "bold"))
        lbl.pack(pady=15)

        scroll = ctk.CTkScrollableFrame(self, width=450, height=400)
        scroll.pack(pady=10)

        self.champs_prenoms = []
        for i in range(self.nb_tot):
            e = ctk.CTkEntry(scroll, placeholder_text=f"Joueur {i+1}", width=350)
            e.pack(pady=8)
            self.champs_prenoms.append(e)

        btn = ctk.CTkButton(self, text="Lancer la partie", command=self.lancer_partie, font=("Helvetica", 16, "bold"))
        btn.pack(pady=15)

    def lancer_partie(self):
        noms = [e.get().strip() or f"Joueur {i+1}" for i, e in enumerate(self.champs_prenoms)]
        
        self.mot_civil, self.mot_undercover = random.choice(BANQUE_MOTS)
        roles = (["Civil"] * self.nb_civ) + (["Undercover"] * self.nb_und) + (["Mr. White"] * self.nb_whi)
        random.shuffle(roles)

        self.joueurs = []
        for i, nom in enumerate(noms):
            role = roles[i]
            mot = self.mot_civil if role == "Civil" else (self.mot_undercover if role == "Undercover" else "Tu es Mr. White !")
            self.joueurs.append({"nom": nom, "role": role, "mot": mot, "en_vie": True})

        self.index_decouverte = 0
        self.afficher_decouverte_mot()

    # --- ÉCRAN 3 : DISTRIBUTION SECRÈTE ---
    def afficher_decouverte_mot(self):
        self.nettoyer_ecran()

        if self.index_decouverte >= len(self.joueurs):
            self.afficher_ecran_jeu()
            return

        j = self.joueurs[self.index_decouverte]

        lbl_titre = ctk.CTkLabel(self, text=f"Tour de : {j['nom']}", font=("Helvetica", 26, "bold"))
        lbl_titre.pack(pady=40)

        lbl_inst = ctk.CTkLabel(self, text="Passe l'appareil à ce joueur.\nAppuie ci-dessous pour afficher le mot secret.", font=("Helvetica", 14))
        lbl_inst.pack(pady=10)

        self.lbl_mot = ctk.CTkLabel(self, text="???", font=("Helvetica", 28, "bold"), text_color="yellow")
        self.lbl_mot.pack(pady=40)

        self.btn_reveler = ctk.CTkButton(self, text="Révéler mon mot", command=lambda: self.lbl_mot.configure(text=j["mot"]))
        self.btn_reveler.pack(pady=10)

        btn_suivant = ctk.CTkButton(self, text="Cacher et passer au suivant", command=self.suivant_decouverte, fg_color="green", hover_color="darkgreen")
        btn_suivant.pack(pady=20)

    def suivant_decouverte(self):
        self.index_decouverte += 1
        self.afficher_decouverte_mot()

    # --- ÉCRAN 4 : PLATEAU DE JEU (VOTES) ---
    def afficher_ecran_jeu(self):
        self.nettoyer_ecran()

        # Vérification victoire
        vivants = [j for j in self.joueurs if j["en_vie"]]
        civils = [j for j in vivants if j["role"] == "Civil"]
        imposteurs = [j for j in vivants if j["role"] in ["Undercover", "Mr. White"]]

        if not imposteurs:
            self.afficher_fin("VICTOIRE DES CIVILS !")
            return
        if len(civils) <= 1 and imposteurs:
            self.afficher_fin("VICTOIRE DES IMPOSTEURS !")
            return

        lbl = ctk.CTkLabel(self, text="Phase de Vote", font=("Helvetica", 26, "bold"))
        lbl.pack(pady=15)

        lbl_sub = ctk.CTkLabel(self, text="Après débat, cliquez sur le joueur éliminé par le groupe :", font=("Helvetica", 13))
        lbl_sub.pack(pady=5)

        frame_liste = ctk.CTkFrame(self)
        frame_liste.pack(pady=20, padx=20, fill="both", expand=True)

        for j in self.joueurs:
            if j["en_vie"]:
                btn_j = ctk.CTkButton(
                    frame_liste, 
                    text=f"Éliminer {j['nom']}", 
                    command=lambda joueur=j: self.eliminer_joueur(joueur),
                    fg_color="#D32F2F", 
                    hover_color="#9A0007",
                    font=("Helvetica", 14)
                )
                btn_j.pack(pady=6, padx=20, fill="x")

    def eliminer_joueur(self, joueur):
        joueur["en_vie"] = False

        if joueur["role"] == "Mr. White":
            self.afficher_devinette_white(joueur)
        else:
            self.afficher_popup_elimination(joueur)

    def afficher_popup_elimination(self, joueur):
        self.nettoyer_ecran()
        
        lbl = ctk.CTkLabel(self, text=f"{joueur['nom']} a été éliminé !", font=("Helvetica", 24, "bold"))
        lbl.pack(pady=40)

        lbl_role = ctk.CTkLabel(self, text=f"Rôle : {joueur['role']}", font=("Helvetica", 20), text_color="orange")
        lbl_role.pack(pady=20)

        btn = ctk.CTkButton(self, text="Continuer la partie", command=self.afficher_ecran_jeu, font=("Helvetica", 16))
        btn.pack(pady=30)

    # --- ÉCRAN 5 : CHANCE MR. WHITE ---
    def afficher_devinette_white(self, joueur):
        self.nettoyer_ecran()

        self.white_elimine = joueur

        lbl = ctk.CTkLabel(
            self,
            text=f"{joueur['nom']} était Mr. White !",
            font=("Helvetica", 24, "bold"),
            text_color="orange"
        )
        lbl.pack(pady=20)

        lbl_inst = ctk.CTkLabel(
            self,
            text="Mr. White a une chance de deviner le mot des Civils pour gagner :",
            font=("Helvetica", 13)
        )
        lbl_inst.pack(pady=10)

        self.entree_devinette = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Proposer un mot..."
        )
        self.entree_devinette.pack(pady=20)

        btn = ctk.CTkButton(
            self,
            text="Valider la devinette",
            command=self.verifier_devinette_white
        )
        btn.pack(pady=10)

    def verifier_devinette_white(self):
        proposition = self.entree_devinette.get().strip().lower()

        if proposition == self.mot_civil.lower():
            self.afficher_fin(
                f"MR. WHITE A DEVINÉ LE MOT "
                f"('{self.mot_civil}') ET GAGNE LA PARTIE !"
            )
        else:
            self.afficher_popup_elimination(self.white_elimine)

    # --- ÉCRAN FIN ---
    def afficher_fin(self, message):
        self.nettoyer_ecran()

        lbl_victoire = ctk.CTkLabel(
            self,
            text=message,
            font=("Helvetica", 22, "bold"),
            text_color="green",
            wraplength=450
        )
        lbl_victoire.pack(pady=25)

        lbl_recap = ctk.CTkLabel(
            self,
            text=f"Mot Civil : {self.mot_civil}\nMot Undercover : {self.mot_undercover}",
            font=("Helvetica", 16)
        )
        lbl_recap.pack(pady=15)

        frame_boutons = ctk.CTkFrame(self, fg_color="transparent")
        frame_boutons.pack(pady=20, padx=30, fill="x")

        # Rejouer avec les mêmes joueurs
        btn_rejouer_memes = ctk.CTkButton(
            frame_boutons,
            text="🔄 Rejouer avec les mêmes joueurs",
            command=self.rejouer_memes_joueurs,
            font=("Helvetica", 15, "bold"),
            fg_color="#1F6AA5"
        )
        btn_rejouer_memes.pack(pady=8, fill="x")

        # Nouvelle partie avec possibilité de changer les joueurs
        btn_nouvelle_partie = ctk.CTkButton(
            frame_boutons,
            text="👥 Nouvelle partie",
            command=self.nouvelle_partie,
            font=("Helvetica", 15, "bold"),
            fg_color="#2E7D32",
            hover_color="#1B5E20"
        )
        btn_nouvelle_partie.pack(pady=8, fill="x")

        # Retour au menu de configuration
        btn_recommencer = ctk.CTkButton(
            frame_boutons,
            text="⚙️ Changer la configuration",
            command=self.afficher_ecran_config,
            font=("Helvetica", 14),
            fg_color="gray",
            hover_color="#555555"
        )
        btn_recommencer.pack(pady=8, fill="x")
        
    def rejouer_memes_joueurs(self):
        # On extrait la liste des prénoms existants
        noms = [j["nom"] for j in self.joueurs]

        # Tirage d'une nouvelle paire de mots
        self.mot_civil, self.mot_undercover = random.choice(BANQUE_MOTS)

        # Réattribution aléatoire des rôles
        roles = (
            ["Civil"] * self.nb_civ
            + ["Undercover"] * self.nb_und
            + ["Mr. White"] * self.nb_whi
        )
        random.shuffle(roles)

        # Réinitialisation de la structure des joueurs
        self.joueurs = []

        for i, nom in enumerate(noms):
            role = roles[i]

            if role == "Civil":
                mot = self.mot_civil
            elif role == "Undercover":
                mot = self.mot_undercover
            else:
                mot = "Tu es Mr. White !"

            self.joueurs.append({
                "nom": nom,
                "role": role,
                "mot": mot,
                "en_vie": True
            })

        # Relance du cycle
        self.index_decouverte = 0
        self.afficher_decouverte_mot()


    def nouvelle_partie(self):
        """
        Recommence une partie en permettant de modifier
        les joueurs, leurs prénoms et la configuration.
        """

        # Réinitialisation
        self.joueurs = []
        self.mot_civil = ""
        self.mot_undercover = ""
        self.index_decouverte = 0

        # Retour à la configuration
        self.afficher_ecran_config()


if __name__ == "__main__":
    app = UndercoverApp()
    app.mainloop()