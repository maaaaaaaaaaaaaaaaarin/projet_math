

# Notes sur 5
notes = [i/10 for i in range(51)]

# TODO: Ajouter des catégories / taggs pour recommender les objets
# comparer des profils d'utilisateurs, etc

personnes = {

  "John" : {
    "recemment_achete" : [
      {"nom": "A", "note":4.8},
      {"nom": "B", "note":4.5},
      {"nom": "C", "note":4.5}
      ]
  },
  "Johnson": {
    "recemment_achete" : [
      {"nom": "A", "note":4.7},
      {"nom": "B", "note":4.4},
      {"nom": "C", "note":5},
      {"nom": "D", "note":4.3}
    ]

  }
}
liste_prenoms = list(personnes)

compteurMatch = 0

personne1 = personnes[liste_prenoms[0]]
personne2 = personnes[liste_prenoms[1]]

# On prévoit la recommendation du point de vue de personne1
for i in personne1["recemment_achete"]:
  produit = i["nom"]
  produits_personne2 = map(lambda x: x["nom"] ,personne2["recemment_achete"])

  if produit in produits_personne2:
    produit2 = list(filter(lambda x: x["nom"]==produit, personne2["recemment_achete"]))[0]

    if (i["note"] == produit2["note"]) or (i["note"] == produit2["note"]+0.1) or (i["note"] == produit2["note"]-0.1):
    #if i["note"]+0.1 <= produit2["note"] or i["note"]-0.1 >= produit2["note"]:
      #print("Produit '"+produit+"', note: "+"\t Produit (per.2) "+str(produit2["nom"])+", note: "+str(produit2["note"])))
      print("Produit '{}', note: {} \t Produit (per.2) '{}', note: {}".format(produit, i["note"], produit2["nom"], produit2["note"]))
      compteurMatch +=1

print("{} objets ont des notes similaires entre Personne 1, et Personne 2.".format(compteurMatch))

if compteurMatch >= 2: 
  # Recuperer les objets a recommander
  # (on exclus les objets présent dans pers1 et pers 2)

  p1 = map(lambda x: x["nom"], personne1["recemment_achete"])
  p2 = map(lambda x: x["nom"], personne2["recemment_achete"])

  recommendations = list(set(list(p2)).difference(set(list(p1))))
  produits_filtrés = list(filter(lambda x: x["nom"] in recommendations, personne2["recemment_achete"]))
  print(produits_filtrés)
  articles_selectionnés = []

  moyenne = sum(list(map(lambda x: x["note"], personne1["recemment_achete"])))/len(list(map(lambda x: x["note"], personne1["recemment_achete"])))
  print("Moyenne des notes de Personne 1: {}".format(moyenne))
  for i in produits_filtrés:
    if i["note"] > moyenne:
      articles_selectionnés.append(i)

  articles_selectionnés = map(lambda x: x["nom"], articles_selectionnés)
  print("Les clients ayant acheté certains de vos articles ont également regardé: {}".format(", ".join(articles_selectionnés)))
