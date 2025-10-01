## Impact des logements sur les émissions de CO₂ en France

### 1. Introduction

Les bâtiments résidentiels constituent un secteur clé de la transition énergétique en France. Ils représentent une part significative des émissions de gaz à effet de serre (GES), principalement liées au chauffage, à l’eau chaude sanitaire et à la consommation énergétique globale. Comprendre les déterminants structurels et socio-énergétiques des émissions constitue une étape essentielle pour orienter les politiques publiques, améliorer l’efficacité énergétique et réduire les inégalités environnementales.

Ce projet propose une analyse statistique et économétrique des diagnostics de performance énergétique (DPE), en mettant en évidence les relations entre caractéristiques du logement (surface, année de construction, énergie de chauffage) et émissions de CO₂. L’approche combine méthodes descriptives, économétrie et apprentissage automatique, et débouche sur un dashboard interactif permettant une exploitation pédagogique et opérationnelle des résultats.

### 2. Données et méthodologie

Les données proviennent des bases publiques du Ministère de la Transition Écologique / ADEME (DPE logements). Après une phase de nettoyage et d’harmonisation, l’échantillon utilisé comprend ≈ 5 000 logements représentatifs de différents types de bâtiments et de zones géographiques.

La méthodologie s’articule en plusieurs étapes :

- Exploration descriptive : distribution des surfaces, types d’énergies, émissions par logement.

- Visualisation cartographique : émissions agrégées par commune, mise en évidence des contrastes territoriaux.

- Économétrie : régression OLS pour estimer les déterminants des émissions totales et spécifiques (chauffage, ECS, éclairage).

- Analyse de variance (ANOVA) : comparaison des émissions selon le type d’énergie.

- Clustering (K-means) : segmentation des logements en profils homogènes d’émissions.

- Dashboard Streamlit : interface interactive permettant d’explorer dynamiquement les données, les résultats économétriques et les prédictions.

### 3. Résultats principaux

#### 3.1 Déterminants structurels

La régression OLS montre que :

- La surface habitable est le déterminant le plus puissant des émissions (+26 kgCO₂/m² en moyenne).

- L’année de construction indique une rupture nette : les logements antérieurs à 1948 sont beaucoup plus émissifs que ceux construits après 2000.

- Le type d’énergie joue un rôle majeur : fioul et charbon génèrent les émissions les plus élevées, alors que l’électricité et les sources renouvelables apparaissent beaucoup moins carbonées.

#### 3.2 Hétérogénéités énergétiques

L’ANOVA confirme que les différences d’émissions selon l’énergie de chauffage sont hautement significatives (p < 0.001). Ces écarts traduisent à la fois des caractéristiques technologiques (rendements énergétiques) et des choix historiques d’équipements.

#### 3.3 Segmentation des logements

Le clustering K-means identifie trois profils dominants :

- Cluster 1 : petits appartements électriques → faibles émissions.

- Cluster 2 : maisons anciennes au fioul → très fortes émissions.

- Cluster 3 : logements récents au gaz/chauffage urbain → émissions intermédiaires.

Ces résultats ouvrent la voie à une réflexion sur des politiques différenciées, ciblant prioritairement les logements les plus émissifs et les plus anciens.

### 4. Outil interactif (à venir)

Le dashboard Streamlit constitue la valorisation opérationnelle du projet :

- Exploration interactive des données (filtres dynamiques par commune, énergie, période).

- Visualisation cartographique des émissions moyennes.

- Accès direct aux résultats économétriques (régressions, ANOVA).

- Module de simulation prédictive permettant d’estimer les émissions d’un logement selon ses caractéristiques.

Cet outil est pensé comme un support d’aide à la décision pour chercheurs, collectivités et décideurs publics.


### 5. Discussion et perspectives


Ce projet met en évidence l’importance des caractéristiques structurelles et énergétiques dans la détermination des émissions résidentielles. Les résultats confirment la nécessité d’accélérer :

- la rénovation énergétique des logements anciens,

le remplacement des chauffages fioul/charbon par des solutions bas-carbone,

- la prise en compte des inégalités environnementales (logements anciens et polluants étant souvent corrélés à une moindre capacité d’investissement des ménages).

Perspectives :

- Intégration des données socio-économiques INSEE pour analyser les inégalités environnementales.

- Extension à d’autres sources (pollution atmosphérique, vagues de chaleur).

- Déploiement cloud du dashboard pour un accès élargi.

- Approfondissement par des modèles économétriques spatiaux pour mieux saisir les interdépendances territoriales.


### 6. Conclusion

L’étude fournit une base empirique solide pour comprendre les émissions liées aux logements et ouvre la voie à des politiques énergétiques ciblées. Elle illustre la puissance d’une approche combinant statistiques descriptives, économétrie et machine learning dans l’analyse des enjeux climatiques.


#### Cloner le repo
git clone https://github.com/psndao/logement-emissions-co2.git
cd logement-emissions-co2

#### Créer l'environnement
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

#### Installer les dépendances
pip install -r requirements.txt

#### Lancer le dashboard
streamlit run app.py



![CI](https://github.com/psndao/logement-emissions-co2/actions/workflows/ci.yml/badge.svg)








