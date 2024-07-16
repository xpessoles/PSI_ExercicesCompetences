# -*- coding: utf-8 -*-
"""
@author: xpessoles@lamartin.fr
"""

import os
import shutil
import pickle
import codecs


## TODO :
 # Sauvegarder l'historique de compilation a chaque fin de compil
 # Modifier les noms des PDF pour pouvoir les parser
 # Préciser le PC surlquel ont été compilés les fichiers ?
##

PC = "perso"

dico_comp={
    "SYS" : "Analyser et valider les performances d'un système",
    "SYS-01" : "Réaliser une analyse structurelle, flux, effort",
    "SYS-02" : "Analyser une solution technologique",
    "SYS-03" : "Analyser un cahier des charges",
    "SYS-04" : "Valider les performances d'un système vis-à-vis d'un cahier des charges",
    "SYS-05" : "Analyser les résultats d'une simulation ou d'une expérimentation",
    "SYS-06" : "Mesurer et analyser une grandeur physique",
    "GEO" : "Résoudre un problème de géométrie",
    "GEO-01" : "Analyser la géométrie d'un mécanisme, analyser des surfaces de contact, réaliser des constructions géométriques",
    "GEO-02" : "Modéliser un mécanisme en réalisant un schéma cinématique paramétré",
    "GEO-03" : "Résoudre un problème de géométrie : déterminer la trajectoire d'un point ou déterminer une loi Entrée - Sortie",
    "GEO-04" : "Évaluer expérimentalement des grandeurs géométriques",
    "CIN" : "Résoudre un problème de cinématique",
    "CIN-01" : "Analyser un mécanisme, réaliser un graphe de liaison",
    "CIN-02" : "Déterminer un vecteur vitesse, un torseur cinématique, un vecteur accélération",
    "CIN-03" : "Déterminer le rapport de transmission d'un transmetteur",
    "CIN-04" : "Déterminer un loi ES cinématique, utiliser l'hypothèse de RSG",
    "CIN-05" : "Évaluer expérimentalement une grandeur cinématique",
    "STAT" : "Résoudre un problème de statique",
    "STAT-01" : "Analyser un problème en utilisant un graphe de structure",
    "STAT-02" : "Modéliser les actions mécaniques locales, globales, frottement",
    "STAT-03" : "Proposer une démarche de résolution en utilisant le PFS",
    "STAT-04" : "Mettre en œuvre une démarche de résolution",
    "STAT-05" : "Évaluer expérimentalement une action mécanique",
    "CHS" : "Modéliser un mécanisme",
    "CHS-01" : "Analyser un mécanisme en utilisant un graphe de liaisons",
    "CHS-02" : "Simplifier un mécanisme en utilisant une liaison équivalente",
    "CHS-03" : "Évaluer l'hyperstatisme d'un mécanisme",
    "CHS-04" : "Simplifier un mécanisme pour le rendre isostatique",
    "CHS-05" : "Analyser les conséquences de l'hyperstatisme d'un mécanisme",
    "DYN" : "Résoudre un problème de dynamique",
    "DYN-01" : "Analyser un problème, définir une loi de mouvement",
    "DYN-02" : "Analyser un mécanisme en utilisant un graphe de structure",
    "DYN-03" : "Modéliser un solide et déterminer ses caractéristiques inertielles",
    "DYN-04" : "Déterminer un torseur cinétique, un torseur dynamique",
    "DYN-05" : "Proposer une démarche de résolution en utilisant le PFD",
    "DYN-06" : "Mettre en œuvre une démarche de résolution en utilisant le PFD",
    "TEC" : "Résoudre un problème d'énergétique",
    "TEC-01" : "Analyser un mécanisme en utilisant un graphe de structure",
    "TEC-02" : "Déterminer les puissances intérieures",
    "TEC-03" : "Déterminer les puissances extérieures",
    "TEC-04" : "Déterminer l'inertie équivalente, la masse équivalente, l'énergie cinétique, un travail",
    "TEC-05" : "Proposer et mettre en œuvre une démarche de résolution",
    "SLCI" : "Modéliser un SLCI",
    "SLCI-01" : "Analyser un asservissement, proposer une structure d'asservissement",
    "SLCI-02" : "Modéliser un SLCI en utilisant la transformée de Laplace",
    "SLCI-03" : "Modéliser un SLCI en utilisant un schéma-bloc",
    "SLCI-04" : "Modéliser un SLCI en utilisant un modèle polyphysique",
    "SLCI-05" : "Modéliser un SLCI à plusieurs entrées, sous forme matricielle éventuellement",
    "SLCI-06" : "Linéariser un comportement, une équation, simplifier un modèle",
    "SLCI-07" : "Modéliser un système d'ordre 1 et d'ordre 2",
    "SLCI-08" : "Déterminer une FTBO et une FTBF",
    "SLCI-09" : "Identifier des fonctions de transfert (à partir d'un schéma-bloc), mettre sous forme canonique et identifier des constantes",
    "SLCI-10" : "Déterminer et identifier une réponse temporelle",
    "SLCI-11" : "Déterminer, identifier et analyser une réponse fréquentielle",
    "PERF" : "Évaluer les performances d'un SLCI",
    "PERF-01" : "Évaluer la stabilité en utilisant la BF, les pôles de la BF",
    "PERF-02" : "Évaluer la stabilité en utilisant les marges de la BO",
    "PERF-03" : "Évaluer la rapidité de la réponse temporelle",
    "PERF-04" : "Évaluer la rapidité à partir de la réponse fréquentielle de la BO",
    "PERF-05" : "Évaluer la précision à partir du TVF",
    "PERF-06" : "Évaluer la précision en utilisant la classe de la BO",
    "COR" : "Corriger un SLCI",
    "COR-01" : "Analyser un choix de correcteur (compensation de pôles, nombre d'intégrations)",
    "COR-02" : "Régler un correcteur P graphiquement ou analytiquement",
    "COR-03" : "Régler un correcteur PI graphiquement ou analytiquement",
    "COR-04" : "Régler un correcteur à avance de phase",
    "COR-05" : "Modéliser un correcteur numérique",
    "COR-06" : "Implanter un correcteur sur une cible",
    "NL" : "Modélisation des non linéarité d'un système",
    "NL-01" : "Identifier une non linéarité",
    "NL-02" : "Modéliser une non linéarité",
    "SEQ" : "Modéliser un système combinatoire ou séquentiel",
    "SEQ-01" : "Analyser un système séquentiel en utilisant un chronogramme, analyser un système combinatoire en utilisant une table de vérité",
    "SEQ-02" : "Modélisation par équation booléenne",
    "SEQ-03" : "Modélisation par diagramme d'état",
    "NUM" : "Résoudre un problème numériquement",
    "NUM-01" : "Mettre un problème sous forme matricielle",
    "NUM-02" : "Résolution de f(x)=0",
    "NUM-03" : "Résolution d'une équation différentielle",
    "NUM-04" : "Résoudre un problème numériquement",
    "NUM-05" : "Résoudre un problème en utilisant l'apprentissage automatisé"
}

# On fait la liste des .tex d'un dossier.
# On crée pour chaque .tex un dictionnaire :
# {fichier:str, time : os.path.getmtime
chemins = ["../SYS-01"]
def make_tex_list(chemins:[str]):
    """
    Réalisation de la liste de tous les fichier tex.
    REnvoie une liste de dictionnaires :
    dico = {'fichier':file,'last_modif':modif:....}
    """
    tex_liste=[]
    for path in chemins :
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".tex"):
                    if verif(root,file) :
                        dico = make_dico_from_tex_file(root, file)
                        tex_liste.append(dico)


    return tex_liste

def make_pdf_list(chemins:[str]):
    """
    Réalisation de la liste de tous les fichier tex.
    REnvoie une liste de dictionnaires :
    dico = {'fichier':file,'last_modif':modif:....}
    """
    pdf_liste=[]
    for path in chemins :
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".pdf"):
                    if verif(root,file) :
                        #print(file)
                        #dico = make_dico_from_tex_file(root, file)
                        #dico = {}
                        #dico["chemin"]=root
                        #dico["fichier"]=file
                        #dico["last_modif"] = os.path.getmtime(os.path.join(root, file))
                        pdf_liste.append(file)
    return pdf_liste

def make_dico_from_tex_file(root, file):
    """
    Réalise un dictionnaire à partir d'un fichier tex

    Clés du dico :
     - full_chemin : chemin relatif + nom de fichier.tex par rapport au dossier de ce script
     - last_modif : dernière modification
     - chmein : chemin relatif du dossier
     - fichier : fichier.tex
     % "{'classe':(''),'chapitre':'','type':(''),'titre':'', 'source':' ','comp':(None),'corrige':True}"
    """
    fich = os.path.join(root, file)
    fich = fich.replace("\\","/")
    root = root.replace("\\","/")
    modif = os.path.getmtime(fich)

    dico = {
    'full_chemin':fich,
    'last_modif':modif,
    "chemin":root,
    "fichier":file,
    "type":['exo_comp'],
    "depot":'PSU_ExercicesCompetences',
    'chemin_git':'https://github.com/xpessoles/PSI_ExercicesCompetences/tree/main/'+root[27:]
    }

    comp = root.split("/")[-2]
    comp = comp.split("_")[0]
    dico["comp"]=comp
    #print(comp)
    #print(root)

    # Recherche de corrigé
    fid = open(fich,'r',encoding="utf8")
    data = fid.readlines()
    fid.close()
    cor = False
    for line in data :
        if "\correctiontrue" in line:
            cor = True
    #print(cor)
    dico['corrige'] = cor
    #fid = open(fich,'r', encoding="utf8")
    #line = fid.readline()
    #fid.close()
    dico['raw_sujet']="https://xpessoles-cpge.fr/pdf/"+dico['comp']+"_"+dico['fichier'][:-4]+'_Sujet.pdf'
    dico['raw_corrige']="https://xpessoles-cpge.fr/pdf/"+dico['comp']+"_"+dico['fichier'][:-4]+'_Corrige.pdf'

    dico['blob_sujet']="https://xpessoles-cpge.fr/pdf/"+dico['comp']+"_"+dico['fichier'][:-4]+'_Sujet.pdf'
    dico['blob_corrige']="https://xpessoles-cpge.fr/pdf/"+dico['comp']+"_"+dico['fichier'][:-4]+'_Corrige.pdf'
    #print(dico)
    return dico

def verif(root,file):
    """
    Exclusion de fichiers
    """
    test = [
    # "STOCK",
    #     "../../ExercicesCompetences/Outils",
    #     "GPS_PPM_Colle_",
    #     "ALL_EXOS",
    #     "500_Vierge",
    #     "1100_Pneumatique",
    #     "B2_13_04_RR",
    #     "B2_13_05_RT",
    #     "Exerc_test_Sujet",
    #     "test"
    #
    ]
    for t in test :
        if (t in root) or (t in file) :
            return False
    return True

def compte_activite(comp,tex_liste):
    cpt = 0
    for d in tex_liste :
        if d['comp'] == comp.replace('-','_') :
            cpt = cpt+1
    return cpt


def compile_file(dict):

    # Compilation du sujet
    # On copie la base
    dest = dict["fichier"] # fichier.tex
    dest = dict['comp']+"_"+dest[:-4]+"_Sujet.tex"
    shutil.copy("base.tex",dest)
    print("==================================")
    print(dest)


    # On complete la base
    fid = open(dest,"a")
    fid.write("\\renewcommand{\\repExo}{"+dict["chemin"]+"} \n")
    fid.write("\\graphicspath{{\\repStyle/png}{\\repExo/images}}")
    fid.write("\\input{"+dict["full_chemin"]+"}\n \n")
    fid.write("\\end{document}")
    fid.close()

    # On compile
    os.system("pdflatex --shell-escape "+dest)
    os.system("pdflatex --shell-escape "+dest)

    src = dest[:-4]+".pdf"
    dest = "../PDF/"+src
    # On stocke
    shutil.copy(src,dest)
    # On efface tout les fichiers de compil
    src = src[:-4]
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.startswith(src):

                try :
                    os.remove(file)
                except :
                    print(file)


    #################################
    # Compilation du corrigé
    # On copie la base
    dest = dict["fichier"] # fichier.tex
    dest = dict['comp']+"_"+dest[:-4]+"_Corrige.tex"
    shutil.copy("base.tex",dest)
    print("==================================")
    print(dest)


    # On complete la base
    fid = open(dest,"a")
    fid.write("\\proftrue \n")
    fid.write("\\renewcommand{\\repExo}{"+dict["chemin"]+"} \n")
    fid.write("\\graphicspath{{\\repStyle/png}{\\repExo/images}}")
    fid.write("\\input{"+dict["full_chemin"]+"}\n \n")
    fid.write("\\end{document}")
    fid.close()

    # On compile
    os.system("pdflatex --shell-escape "+dest)
    os.system("pdflatex --shell-escape "+dest)

    src = dest[:-4]+".pdf"
    dest = "../PDF/"+src
    # On stocke
    shutil.copy(src,dest)
    # On efface tout les fichiers de compil
    src = src[:-4]
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.startswith(src):

                try :
                    os.remove(file)
                except :
                    print(file)




def save_liste_tex(data,machine) :
    # Sauver la liste des fichiers tex
    nom_fichier = 'activites_tex_liste_'+machine+'.save'
    file = open(nom_fichier, 'wb')
    pickle.dump(data, file)
    file.close()

def load_liste_tex(machine) :
    # Charger la liste des fichiers tex
    nom_fichier = 'activites_tex_liste_'+machine+'.save'
    file = open(nom_fichier, 'rb')
    data = pickle.load(file)
    return data


def go(machine):
    # compilation UNIQUEMENT des fichiers modifiés
    old_tex_file = load_liste_tex(machine)
    new_tex_file = make_tex_list(chemins,machine)
    i=0
    for d_new in new_tex_file :
        # On cherche si le fichier existe dans le fichier_sauvegarder

        if d_new not in old_tex_file :

            compile_file(d_new)
        ### AREVOIR SAUVEGARDE A CHAQUE ITeRATION CI DESSOUS CA MARCHE PAS

        #On sauve la liste à chaque itération ### TEST ####
        save_liste_tex(new_tex_file[:i])
        old_tex_file = load_liste_tex()
        i=i+1

def diff_tex_file(machine):
    # affichage des fichiers modifiés
    old_tex_file = load_liste_tex(machine)
    new_tex_file = make_tex_list(chemins)
    i=0
    for d_new in new_tex_file :
        # On cherche si le fichier existe dans le fichier_sauvegarder
        if d_new not in old_tex_file :
            print(d_new)


def make_all_pdf():
    # Création de tous les PDF
    tex_liste = make_tex_list(chemins)


    for d in tex_liste :
        liste_pdf = make_pdf_list(['../PDF'])
        f_pdf_1 = d['comp']+"_"+d['fichier'][:-4]+'_Sujet.pdf'
        f_pdf_2 = d['comp']+"_"+d['fichier'][:-4]+'_Corrige.pdf'
        print(f_pdf_1,f_pdf_2)
        #return f_pdf,liste_pdf
        if (f_pdf_1 not in liste_pdf) and (f_pdf_2 not in liste_pdf) :
            #pass
            compile_file(d)


def make_nav(dico):
    # RENVOIE LA LISTE DES CHAPITRE
    # On crée la nav du site
    chap = []
    for d in dico :
        c = d['comp'].replace('_','-')
        if c not in chap :
            chap.append(c)

        # Vérif que les fichiers ont un chapitre
        if d['comp'] == '':
            print(d['fichier'])
            print(d['chapitre'])

    """
    Création du fichier du paragraphe de nav à ajouter dans mkdocs.yml
    """
    chap.sort()

    fid = open("nav_activites.yml","w",encoding = 'utf8')
    fid.write('- Activités SII: \n')
    fid.write('    - activites/index.md \n')

    for c in chap:
        ## On ne met que les comp ou il y a des exos
        if compte_activite(c,tex_liste)>0 :
            fid.write('    - '+c+' : activites/'+c+'.md\n')
    fid.close()

    print("Modifier le fichier mkdocs.yml")
    return chap




def creation_fichiers_activites(chap_comp,liste_dico_act):
    """
    Création de fichiers correspondants aux activités
    """
    print("Creation d'un fichier md par compétence.")

    for comp in chap_comp :
        fid = open("C:\\GitHub\\xpessoles.github.io\\docs\\activites\\"+comp+".md","w",encoding = 'utf8')
        id_comp = comp

        titre_comp = dico_comp[comp]


        ## Titre de la page & Tags
        fid.write('---\n')
        fid.write('title: '+titre_comp+" \n")
        fid.write("tags:\n")
        fid.write('  - '+comp+"\n")
        fid.write('---\n')

        fid.write('[comment]: <> (Généré automatiquement par make_all_activitess.py, creation_fichiers_activites)\n\n')


        fid.write("##"+titre_comp +" \n")
        # On cherche toutes les activités
        liste_act = []
        for file in liste_dico_act :

            if file['comp'].replace("_","-") == id_comp :
                liste_act.append(file)


        fid.write("| Activités | Sujet | Corrigé | Sources  | \n")
        fid.write("| :-------------- | :---: | :-----: | :------: | \n")
        for act in liste_act :
            fid.write("| "+act['fichier'][:-4]+ " | ")
            fid.write("[:fontawesome-solid-file-pdf:]("+act['blob_sujet']+") | ")
            if act['corrige'] :
                fid.write("[:fontawesome-solid-file-pdf:]("+act['blob_corrige']+") |")
            else:
                fid.write("[:fontawesome-regular-file-pdf:]("+act['blob_corrige']+") | ")


            fid.write("[:material-github:]("+act['chemin_git']+") |  \n")

        fid.write("\n")
        fid.close()


def make_full_pdf(chemins,dico_comp):
    # Créér le fichier tex avec toutes les activités
    # Compiler les sujets
    # TODO : ajouter les corrigés
    tex_liste = make_tex_list(chemins)

    fid = codecs.open("../FULL_PDF/all_tex.tex","w","utf-8")

    chap_ordre = ["SYS","GEO","CIN","STAT","CHS","DYN","TEC","SLCI","PERF","COR","NL","SEQ","NUM"]

    for chap in chap_ordre :
        fid.write("\\setchapterpreamble[u]{\\margintoc} \n")
        fid.write("\chapter{"+dico_comp[chap]+"} \n")
        for comp in dico_comp :

            if (chap in comp) and ("-" in comp) :
                fid.write("\\section{"+dico_comp[comp]+"} \n")

                for file in tex_liste :
                    if file['comp'] == comp :
                        print(file)
                        print(file['full_chemin'])
                        chemin_image = file['chemin']+"/images/"
                        fid.write("\\graphicspath{{\\repStyle/png/}{"+chemin_image+"}} \n")
                        fid.write("\\input{"+file['full_chemin']+"} \n \n")

    fid.close()
    os.chdir("../FULL_PDF")
    os.system("pdflatex --shell-escape FULL_PDF_ExercicesCompetences.tex")
    os.system("pdflatex --shell-escape FULL_PDF_ExercicesCompetences.tex")
    os.chdir("../scripts")

make_full_pdf(chemins,dico_comp)






tex_liste = make_tex_list(chemins)
#make_all_pdf()
#
# tex_liste = make_tex_list(chemins)
# #save_liste_tex(tex_liste,PC)
# nav = make_nav(tex_liste)
#
# creation_fichiers_activites(nav,tex_liste)
#
#
# for k,v in dico_comp.items():
#     cc = compte_activite(k,tex_liste)
#     if cc>0 :
#         print("| "+k+" | "+v+" | __"+str(cc)+"__ |")