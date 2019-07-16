import pandas as pd


class Compare():

    def __init__(self, source=None, compare=None, dest=None, mapp=None):
        self.dest = dest
        self.mapp = mapp
        self.source = source
        self.compare = compare
        self.notinb = pd.DataFrame
        self.notinA = pd.DataFrame
        self.mapp = mapp

        try:
            self.mapp = self.mapp.astype(str)
        except AttributeError:
            pass

    def imp_colonne(self):
        col_source = self.source.columns
        col_compare = self.compare.columns
        col_newsource = []
        col_newcompare = []

        try:
            for i, val in enumerate(col_source):
                if col_source[i] not in list(self.mapp.iloc[:,1]):
                    col_newsource.append(col_source[i])
                else:
                    filter = self.mapp.iloc[:,1] == val
                    ind_value = self.mapp.index[filter].tolist()
                    col_newsource.append(self.mapp.iloc[ind_value[0],0])

            for i, val in enumerate(col_compare):
                if col_compare[i] not in list(self.mapp.iloc[:,2]):
                    col_newcompare.append(col_compare[i])
                else:
                    filter = self.mapp.iloc[:,2] == val
                    ind_value = self.mapp.index[filter].tolist()
                    col_newcompare.append(self.mapp.iloc[ind_value[0],0])
            col_shared = [x for x in col_newsource if x in col_newcompare]

        except:
            col_shared = [x for x in col_source if x in col_compare]

        return col_shared

    def compare_files(self, list_col):
        for i, val in enumerate(list_col):
            if i == 0 :
                if val in self.source.columns:
                    self.source["Key"] = self.source[val].astype(str)
                else:
                    print(self.source[self.mapp.iloc[1][self.mapp.iloc[0]==val]][0])
                    self.source["Key"] = self.source[self.mapp.iloc[1][self.mapp.iloc[0]==val]][0]

            else: # Cas où l'on utilise la table de mapping, le champs n'existe pas dans le fichier source sous le même nom
               if val in self.source.columns:
                   self.source["Key"] = self.source["Key"].astype(str) + self.source[val].astype(str)
               else:
                  print(list(self.mapp.iloc[:,1][self.mapp.iloc[:,0] == val])[0])
                  self.source["Key"] = self.source["Key"] + self.source[list((self.mapp.iloc[:,1][self.mapp.iloc[:,0] == val]))[0]].astype(str) # Récupère la valeur correspondate dans la table de mapping
                  #print(self.source[self.mapp.iloc[1][self.mapp.iloc[0] == val]][0])
                  #self.source["Key"] = self.source[self.mapp.iloc[1][self.mapp.iloc[0] == val]][0]

        print(self.source)

