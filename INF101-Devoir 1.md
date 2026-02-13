# INF101 - Introduction aux outils informatiques (3 Crédits)
**Devoir #1**
**Hiver 2026**

## Consignes générales
* Ce travail se fait en équipe de 2 étudiants au maximum.
* Il est fortement conseillé de se mettre en équipe avec des personnes qui habitent la même localité que vous, afin de faciliter les échanges conduisant à la réalisation du travail.
* Le travail doit être remis sur Moodle AU PLUS TARD LE 21 FÉVRIER 2026. Pour cela, il faut rentrer sur le site du cours et déposer le fichier en utilisant l’option « Remise du travail ».
* Ce travail sera noté sur 20 pour une pondération 10 % de la note finale du cours. Il doit être rédigé en français.

---

## Exercice # 1 (2 points)
Nommer tous les composants que l'on trouve dans une tour d'ordinateur de bureau.

**Réponse :**
Les principaux composants que l'on trouve dans une tour d'ordinateur de bureau sont :
1.  **La carte mère (Motherboard) :** Le circuit imprimé principal qui connecte tous les composants.
2.  **Le processeur (CPU) :** Le cerveau de l'ordinateur qui exécute les instructions.
3.  **La mémoire vive (RAM) :** Stocke temporairement les données en cours d'utilisation.
4.  **Le disque dur (HDD) ou disque SSD :** Pour le stockage permanent des données et du système d'exploitation.
5.  **Le bloc d'alimentation (Power Supply Unit - PSU) :** Fournit l'électricité aux composants.
6.  **La carte graphique (GPU) :** (Peut être intégrée au CPU ou dédiée) Gère l'affichage à l'écran.
7.  **Le système de refroidissement :** Ventilateurs et dissipateurs thermiques pour le processeur et le boîtier.
8.  **Le lecteur optique (CD/DVD/Blu-ray) :** (Optionnel, de plus en plus rare).
9.  **La carte réseau / Carte Wi-Fi :** (Souvent intégrée à la carte mère) Pour la connexion réseau.
10. **La carte son :** (Souvent intégrée à la carte mère).

## Exercice # 2 (3 points)
Un étudiant de l’ISTEAH utilise l’un des ordinateurs de la salle informatique pour travailler sur un devoir. Il allume l’ordinateur et ouvre Microsoft Word afin de rédiger son travail. Il saisit son texte à l’aide du clavier et utilise la souris pour corriger certaines parties. Pendant qu’il travaille, il se rend compte qu’il ne comprend pas bien une notion vue en classe. Il regarde alors une capsule vidéo du cours sur Moodle. Pour ne pas déranger les autres étudiants dans la salle, il met ses écouteurs. Une fois la notion comprise, il reprend son travail, enregistre le document, puis copie la partie déjà réalisée du devoir sur une clé USB afin de pouvoir continuer à travailler chez lui sur son ordinateur personnel. Avant de quitter la salle, il imprime la partie déjà faite de son devoir.

À partir de ce scénario, quels sont les périphériques utilisés par l’étudiant ? Précisez le type de chacun.

**Réponse :**
Basé sur le scénario, voici les périphériques utilisés et leurs types :

| Périphérique | Type | Justification dans le texte |
| :--- | :--- | :--- |
| **Clavier** | Entrée | "Il saisit son texte à l’aide du clavier" |
| **Souris** | Entrée | "utilise la souris pour corriger certaines parties" |
| **Écran** | Sortie | "Il regarde alors une capsule vidéo" (Impliqué) |
| **Écouteurs** | Sortie | "il met ses écouteurs" |
| **Clé USB** | Entrée / Sortie (Stockage) | "copie la partie déjà réalisée du devoir sur une clé USB" |
| **Imprimante** | Sortie | "il imprime la partie déjà faite de son devoir" |

## Exercice # 3 (3 points)
En vous appuyant sur la figure ci-dessous (Note: Image non extraite), définissez et explicitez les rôles des composants numériques suivants dans l’architecture de base d’un ordinateur :

**Réponse :**

*   **Compteur de programme (Program Counter - PC) :**
    *   C'est un registre qui contient l'adresse mémoire de la *prochaine* instruction à exécuter par le processeur. Il est incrémenté automatiquement après chaque lecture d'instruction.

*   **Registre de données (Memory Data Register - MDR) :**
    *   Ce registre stocke temporairement les données qui viennent d'être lues de la mémoire ou celles qui sont prêtes à être écrites dans la mémoire. Il agit comme un tampon entre le processeur et la mémoire centrale.

*   **Accumulateur (Accumulator - AC) :**
    *   C'est un registre spécial de l'unité arithmétique et logique (UAL) utilisé pour stocker les résultats intermédiaires des opérations arithmétiques et logiques.

*   **Registre d’instructions (Instruction Register - IR) :**
    *   Ce registre contient l'instruction qui est *actuellement* en cours d'exécution. Le processeur décode le contenu de ce registre pour savoir quelle opération effectuer.

*   **Registre tampon (Buffer Register) :**
    *   Un registre utilisé pour stocker temporairement des données lors de leur transfert entre deux unités fonctionnelles fonctionnant à des vitesses différentes (par exemple, entre le processeur et un périphérique).

*   **Registre de sortie (Output Register - OUTR) :**
    *   Ce registre conserve les données traitées par le processeur avant qu'elles ne soient envoyées vers un périphérique de sortie (comme un écran ou une imprimante).

*   **Registre d’entrée (Input Register - INPR) :**
    *   Ce registre reçoit et stocke temporairement les données provenant d'un périphérique d'entrée (comme un clavier) avant qu'elles ne soient traitées par le processeur.

*   **Registre d’adresse (Memory Address Register - MAR) :**
    *   Ce registre contient l'adresse de l'emplacement mémoire auquel le processeur veut accéder, que ce soit pour lire une instruction/donnée ou pour écrire une donnée.

## Exercice # 4 (1.5 points)
Convertissez les nombres décimaux suivants en bases indiquées :
a. 265 en binaire
b. 839 à octal
c. 572 en hexadécimal

## Exercice # 5 (2.5 points)
Décrivez un cycle d’instruction en l’illustrant à l’aide de la représentation interne de l’information dans les registres suivants : registre d’adresse, registre mémoire, registre d’instruction, registre de données, registre du processeur.

## Exercice # 6 (1 point)
Explicitez le mécanisme de conversion du décimal 41.6875 en binaire 101001.1011.

## Exercice # 7 (4 points)
* Étant donné un nombre N en base r ayant n chiffres. Le complément à (r - 1) de N est défini par (rn - 1) - N.
* Pour les nombres décimaux r = 10 et r - 1 = 9. Le complément à 9 de N est (10n - 1) - N.
* Pour les nombres binaires r = 2 et r - 1 = 1. Le complément à 1 de N est donc (2n - 1) – N.
* Le complément à 9 d'un nombre décimal est obtenu en soustrayant chaque chiffre de 9.
  * Exemple : Le complément à 9 de 546700 est 999999 – 546700 = 453299
* Le complément à 1 d'un nombre binaire est formé en changeant les 1 en 0 et les 0 en 1.
  * Exemple : le complément à 1 de 1011001 est 0100110

En vous inspirant de ce qui précède et grâce à une illustration de votre choix, expliquez comment obtenir le complément à (r – 1) d’un nombre octal, et le complément à (r – 1) d’un nombre hexadécimal.

## Exercice # 8 (3 points)
Explicitez la configuration en RAM et en ROM de la carte d’adresse mémoire décrite à travers le schéma ci-dessous (Note: Image non extraite).

---
**Bon travail !**
