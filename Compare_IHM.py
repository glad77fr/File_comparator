from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import Pmw
#from tkinter.filedialog import *
import tkinter
import pandas as pd
import json
from Compare_code import Compare



class Application(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.comparison = Compare()
        self.title("Comparateur de données")
        self.resizable(width=False, height=False)
        self.load_data()
        self.mainloop()

    def initialize(self):
        self.control_menu = Frame(self)
        self.control_menu.pack()

        self.conf_menu = LabelFrame(self.control_menu, text="1-Configuation", width=430, height=300, labelanchor='n')
        self.conf_menu.grid(row=1, column=1, pady=10, padx=10)

        self.rep_source_affiche = StringVar()
        self.rep_compare = StringVar()
        self.rep_cible_affiche = StringVar()
        self.list_champs_val = StringVar()
        self.mapp = StringVar()

        self.haut = IntVar(value=0)
        self.larg = IntVar(value=0)

        self.entree_label = Label(self.conf_menu, text="Fichier Référence")
        self.entree_label.grid(row=1, column=1, padx=20,sticky=W)

        self.entree = Entry(self.conf_menu, textvariable=self.rep_source_affiche, width=50)
        self.entree.grid(row=1, column=2,sticky=W, padx=0)

        self.imp_Button = Button(self.conf_menu, text="Sélection...", command=self.import_file_source)
        self.imp_Button.grid(row=1, column=3, padx=15, pady=10,sticky=W)

        self.comp_button = Button(self.conf_menu, text="Sélection...", command=self.import_file_compare)
        self.comp_button.grid(row=2, column=3, padx=15, pady=10, sticky=W)

        self.cible_label = Label(self.conf_menu, text="Fichier Comparé")
        self.cible_label.grid(row=2, column=1, padx=20, sticky=W)

        self.compare_entree = Entry(self.conf_menu, textvariable=self.rep_compare, width=50)
        self.compare_entree.grid(row=2, column=2, sticky=W, padx=0)

        self.cible_label = Label(self.conf_menu, text="Destination")
        self.cible_label.grid(row=3,column=1, padx=20,sticky=W)

        self.cible_entree = Entry(self.conf_menu, textvariable=self.rep_cible_affiche, width=50)
        self.cible_entree.grid(row=3, column=2, sticky=W, padx=0)

        self.cible_Button = Button(self.conf_menu, text="Sélection...", command = self.rep_cible)
        self.cible_Button.grid(row=3, column=3, padx=15, pady=10,sticky=W)

        self.mapping_label = Label(self.conf_menu, text="Mapping")
        self.mapping_label.grid(row=4, column=1, padx=20, sticky=W)

        self.mapping_entree = Entry(self.conf_menu, textvariable=self.mapp, width=50)
        self.mapping_entree.grid(row=4, column=2, sticky=W, pady=10)

        self.mapping_Button = Button(self.conf_menu, text="Sélection...", command=self.import_file_mapping)
        self.mapping_Button.grid(row=4, column=3, padx=15, pady=10, sticky=W)

        self.ex_menu = LabelFrame(self.control_menu, text="Chargement", width=430, height=200, labelanchor='n')
        self.ex_menu.grid(row=1, column=2,padx=10, pady=10)

        self.ex_Button = Button(self.ex_menu, text="Charger", command = self.ex_programme,height = 1, width = 18)
        self.ex_Button.grid(row=3, column=1, padx=10, pady=10,sticky=W)

        self.quitButton = Button(self.ex_menu, text="Quitter", command=self.destroy,height = 1, width = 18)
        self.quitButton.grid(row=4, column=1, padx=10, pady=10,sticky=W)

        self.champs_menu = LabelFrame(self.control_menu, text="Champs de comparaison", width=430, height=300,
                                      labelanchor='n')
        self.champs_menu.grid(row=2, column=1, padx=10, pady=10)

        self.list_champs = Listbox(self.champs_menu, listvariable=self.list_champs_val, selectmode="multiple",
                                   height=self.haut.get(), width=self.larg.get())
        self.list_champs.grid(row=1, column=1, padx=20, pady=10)

        self.compare_Button = Button(self.champs_menu, text="Comparer", command=self.compare_files)
        self.compare_Button.grid(row=1, column=2, padx=15, pady=10, sticky=W)

    def import_file_source(self):
        rep = filedialog.askopenfilename(initialdir="/", title="Select file",
                                         filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
        if rep != "":
            self.rep_source_affiche.set(rep)
            try:
                self.save_data["source"] = rep
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)
            except:
                self.save_data.update({"Source": rep})
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)

    def import_file_compare(self):
        rep = filedialog.askopenfilename(initialdir="/", title="Select file",
                                         filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
        if rep != "":
            self.rep_compare.set(rep)
            try:
                self.save_data["Compare"] = rep
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)
            except:
                self.save_data.update({"Compare": rep})
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)

    def import_file_mapping(self):
        rep = filedialog.askopenfilename(initialdir="/", title="Select file",
                                         filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
        if rep != "":
            self.mapp.set(rep)
            try:
                self.save_data["Mapping"] = rep
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)
            except:
                self.save_data.update({"Mapping": rep})
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)

    def rep_cible(self):

        self.rep_cible = filedialog.askdirectory()
        if self.rep_cible != "":
            self.rep_cible_affiche.set(self.rep_cible)

            try:
                self.save_data["cible"] = self.rep_cible
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)
            except:
                self.save_data.update({"Cible": self.rep_cible })
                with open('data.txt', 'w+') as outfile:
                    json.dump(self.save_data, outfile)

    def ex_programme(self):

        if self.rep_source_affiche.get() == "":
            messagebox.showerror("Ficher source non sélectionné", "Veuillez sélectionner un fichier source")
            return

        if self.rep_compare.get() == "":
            messagebox.showerror("Ficher à comparer non sélectionné", "Veuillez sélectionner un fichier à comparer")
            return

        if self.rep_cible_affiche.get() == "":
            messagebox.showerror("Répertoire source non sélectionné", "Veuillez sélectionner un répertoire source")
            return

        if self.mapp.get() != "":
            self.comparison = Compare(pd.read_excel(self.rep_source_affiche.get()), pd.read_excel(self.rep_compare.get()), self.rep_cible_affiche.get(), pd.read_excel(self.mapp.get()))
        else:
            self.comparison = Compare(pd.read_excel(self.rep_source_affiche.get()), pd.read_excel(self.rep_compare.get()), self.rep_cible_affiche.get())
        self.list_champs_val.set(self.comparison.imp_colonne())
        self.haut.set(len(self.comparison.imp_colonne()))
        self.larg.set(len(max(self.comparison.imp_colonne(), key=len)))

    def compare_files(self):
        values = [self.list_champs.get(idx) for idx in self.list_champs.curselection()]
        self.comparison.compare_files(values)

    def load_data(self):
        try:
            with open('data.txt') as json_file:
                self.save_data = json.load(json_file)
            try:
                self.rep_cible_affiche.set(self.save_data["cible"])
            except:
                pass
            try:
                self.rep_source_affiche.set(self.save_data["source"])
            except:
                pass
            try:
                self.rep_compare.set(self.save_data["Compare"])
            except:
                pass
            try:
                self.mapp.set(self.save_data["Mapping"])
            except:
                pass
        except:
            self.save_data={}

toto = Application(None)

toto.mainloop()