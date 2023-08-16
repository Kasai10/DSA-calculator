import customtkinter as tk
import Utility
import Database
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

checkboxes = {}
data = {
    'Fliegen': ['MU', 'IN', 'GE'],
    'Gaukeleien': ['MU', 'CH', 'FF'],
    'Klettern': ['MU', 'GE', 'KK'],
    'Körperbeherrschung': ['GE', 'GE', 'KO'],
    'Kraftakt': ['KO', 'KK', 'KK'],
    'Reiten': ['CH', 'GE', 'KK'],
    'Schwimmen': ['GE', 'KO', 'KK'],
    'Selbstbeherrschung': ['MU', 'MU', 'KO'],
    'Singen': ['KL', 'CH', 'KO'],
    'Sinnesschärfe': ['KL', 'IN', 'IN'],
    'Tanzen': ['KL', 'CH', 'GE'],
    'Taschendiebstahl': ['MU', 'FF', 'GE'],
    'Verbergen': ['MU', 'IN', 'GE'],
    'Zechen': ['KL', 'KO', 'KK'],
    'Bekehren_Überzeugen': ['MU', 'KL', 'CH'],
    'Betören': ['MU', 'CH', 'CH'],
    'Einschüchtern': ['MU', 'IN', 'CH'],
    'Etikette': ['KL', 'IN', 'CH'],
    'Gassenwissen': ['KL', 'IN', 'CH'],
    'Menschenkenntnis': ['KL', 'IN', 'CH'],
    'Überreden': ['MU', 'IN', 'CH'],
    'Verkleiden': ['IN', 'CH', 'GE'],
    'Willenskraft': ['MU', 'IN', 'CH'],
    'Fährtensuchen': ['MU', 'IN', 'GE'],
    'Fesseln': ['KL', 'FF', 'KK'],
    'fischen_angeln': ['FF', 'GE', 'KO'],
    'Orientierung': ['KL', 'IN', 'IN'],
    'Pflanzenkunde': ['KL', 'FF', 'KO'],
    'Tierkunde': ['MU', 'MU', 'CH'],
    'Wildnisleben': ['MU', 'GE', 'KO'],
    'Brett_Glücksspiel': ['KL', 'KL', 'IN'],
    'Geographie': ['KL', 'KL', 'IN'],
    'Geschichtswissen': ['KL', 'KL', 'IN'],
    'Götter_Kulte': ['KL', 'KL', 'IN'],
    'Kriegskunst': ['MU', 'KL', 'IN'],
    'Magiekunde': ['KL', 'KL', 'IN'],
    'Mechanik': ['KL', 'KL', 'FF'],
    'Rechnen': ['KL', 'KL', 'IN'],
    'Rechtskunde': ['KL', 'KL', 'IN'],
    'Sagen_legenden': ['KL', 'KL', 'IN'],
    'Sphärenkunde': ['KL', 'KL', 'IN'],
    'Sternkunde': ['KL', 'KL', 'IN'],
    'Alchimie': ['MU', 'KL', 'FF'],
    'Boote_schiffe': ['FF', 'GE', 'KK'],
    'Fahrzeuge': ['CH', 'FF', 'KO'],
    'Handel': ['KL', 'IN', 'CH'],
    'Heilkunde_Gift': ['MU', 'KL', 'IN'],
    'Heilkunde_Krankheiten': ['MU', 'IN', 'KO'],
    'Heilkunde_Seele': ['IN', 'CH', 'KO'],
    'Heilkunde_Wunden': ['KL', 'FF', 'FF'],
    'Holzbearbeitung': ['FF', 'GE', 'KK'],
    'Kochen': ['IN', 'FF', 'FF'],
    'Lederbearbeitung': ['FF', 'GE', 'KO'],
    'Malen_Zeichnen': ['IN', 'FF', 'FF'],
    'Metallbearbeitung': ['FF', 'KO', 'KK'],
    'Musizieren': ['CH', 'FF', 'KO'],
    'Schlösserknacken': ['IN', 'FF', 'FF'],
    'Steinbearbeitung': ['FF', 'FF', 'KK'],
    'Stoffbearbeitung': ['KL', 'FF', 'FF']
}



df = pd.read_csv("main_stat_data.csv")
is_checked = {}
for key in data.keys():
    is_checked[key] = False

def get_dict(entry, dictionary = None):
    if checkboxes[entry][1] == False:
        if dictionary == None:
            Database.databaseLogic(key = "get_stats_dict", entry = entry)
        else:
            checkboxes[entry][1] = True
            update_show_necessary_stats(dictionary, data, entry, show_necessary_stats, show_necessary_stats.cget("text"))
    else:
        checkboxes[entry][1] = False


def mainWindow(skill_to_test = None, is_open = False, quality = None, has_succeded = None, terrible_roll = None, great_roll = None, items = None, items_count = None):
    if items is None:
        Database.databaseLogic(key= "get_items")
    
    if not is_open:
        tk.set_default_color_theme("green")
        tk.set_appearance_mode("dark")

        global window
        window = tk.CTk()
        window.geometry("1920x1080")
        window.title("DSA Rechner")

        main_frame = tk.CTkScrollableFrame(window)

        header_label = tk.CTkLabel(main_frame, text="DSA Rechner", font=("Arial", 50))
        header_label.pack(pady = 20)

        main_grid = tk.CTkFrame(main_frame)
        main_grid.columnconfigure(0, weight=1)
        main_grid.columnconfigure(1, weight=1)

        sub_main_grid = tk.CTkFrame(main_grid)
        sub_main_grid.columnconfigure(0, weight=1)
        sub_main_grid.columnconfigure(1, weight=1)
        sub_main_grid.columnconfigure(2, weight=1)
        sub_main_grid.columnconfigure(3, weight=1)


        below_main_grid = tk.CTkFrame(main_frame)
        below_header = tk.CTkLabel(below_main_grid, text="Inventar", font=("Arial", 40), pady = 30)
        below_header.grid(column = 2, row = 0, columnspan = 5)

        global below_inventory_frame
        below_inventory_frame = tk.CTkFrame(main_frame)
        below_inventory_frame.columnconfigure(0, weight=1)
        below_inventory_frame.columnconfigure(1, weight=1)

        label1 = tk.CTkLabel(below_main_grid, text="Gegenstand", font=("Arial", 16))
        label2 = tk.CTkLabel(below_main_grid, text="Anzahl", font=("Arial", 16))
        label3 = tk.CTkLabel(below_main_grid, text="Gegenstand", font=("Arial", 16))
        label4 = tk.CTkLabel(below_main_grid, text="Anzahl", font=("Arial", 16))
        label5 = tk.CTkLabel(below_main_grid, text="Gegenstand", font=("Arial", 16))
        label6 = tk.CTkLabel(below_main_grid, text="Anzahl", font=("Arial", 16))
        label7 = tk.CTkLabel(below_main_grid, text="Gegenstand", font=("Arial", 16))
        label8 = tk.CTkLabel(below_main_grid, text="Anzahl", font=("Arial", 16))

        label_list = [label1, label2, label3, label4, label5, label6, label7, label8]

        column = 0
        row = 1
        for label in label_list:
            label.grid(column = column, row = row, padx = 20, sticky = "NSEW")
            column = column + 1

        inventory_list = []
        def make_entrys(row):
            column2 = 0
            for i in range(8):
                entry = tk.CTkEntry(below_main_grid)
                inventory_list.append(entry)
                entry.grid(row = row, column = column2, sticky = "NSEW")
                column2 = column2 + 1

        for i in range(12):
            make_entrys(i + 2)

        
        def show_items(items, items_count, inventory_list):
            j = 0
            for entry in inventory_list:
                if entry.get() == "" and (items_count is not None) and (len(items_count) > 0):
                    if j % 2 == 0:
                        entry.insert(0, items.pop(0))
                    else:
                        entry.insert(0, items_count.pop(0))
                    j = j + 1

        show_items(items, items_count, inventory_list)
                
                



        def save():
            i = 0
            for value in inventory_list:
                if i % 2 == 0 and value.get() != "":
                    items.append(value.get())
                elif i % 2 == 1 and value.get() != "":
                    items_count.append(value.get())
                i = i + 1
            new_list = []
            for i in range(len(items)):
                new_list.append([items[i], items_count[i]])
                

            Database.databaseLogic(key= "inventory" ,items= new_list, destroy= True)






        inventory_button = tk.CTkButton(below_main_grid, text= "Speichern", font = ("Arial", 40), command= save)
        inventory_button.grid(column = 0, row = 0, padx = 15, columnspan = 2)

        right_frame = tk.CTkScrollableFrame(main_grid, bg_color="black", width= 400)

        global text_output_label
        text_output_label = tk.CTkLabel(master=right_frame, font=("Arial", 16), text="")
        text_output_label.grid(row = 0, column = 1)

        global show_necessary_stats
        show_necessary_stats = tk.CTkLabel(master=sub_main_grid, text="Show skills", font=("Arial", 16))
        show_necessary_stats.grid(row = 0, column = 2, rowspan = 4, columnspan = 4, sticky = "NSEW")

        def close_window():
            df.to_csv('main_stat_data.csv', index=False)
            save()
            
        
        window.bind('<Destroy>', lambda event: close_window())
        

        




    


        options = [
            "Körper",
            "Gesellschaft",
            "Natur",
            "Wissen",
            "Handwerk"
        ]

        skill = options[0]


            



        selectedOption = tk.StringVar(main_grid)
        selectedOption.set(options[0])






        main_frame.pack(fill = "both", expand = True)
        main_grid.pack(fill = "both", expand = True)
        right_frame.grid(row = 0, column = 1, rowspan= 5, sticky = "NSEW", columnspan = 5)
        sub_main_grid.grid(row = 3, column = 0)
        below_main_grid.pack(fill = "both", expand = True, padx = 80, side = 'top', anchor='center')
        below_inventory_frame.pack(fill='both', expand=True, padx = 80, pady= 30)



        


    def show_appropriate_skills(skill_parent = None, dictionary_skills = None, dictionary_main_stats = None, skill = None, label = None):

        appropriate_dict = {}
        if skill_parent == "Körper":
            appropriate_dict = Utility.SplitDictionary(data, "Fliegen", "Zechen")
        elif skill_parent == "Gesellschaft":
            appropriate_dict = Utility.SplitDictionary(data, "Bekehren_Überzeugen", "Willenskraft")
        elif skill_parent == "Natur":
            appropriate_dict = Utility.SplitDictionary(data, "Fährtensuchen", "Wildnisleben")
        elif skill_parent == "Wissen":
            appropriate_dict = Utility.SplitDictionary(data, "Brett_Glücksspiel", "Sternkunde")
        elif skill_parent == "Handwerk":
            appropriate_dict = Utility.SplitDictionary(data, "Alchimie", "Stoffbearbeitung")

        column = 0
        row = 5
        for entry in appropriate_dict.keys():
            label = tk.CTkLabel(sub_main_grid, text=entry, font=("Arial", 16), width=5, height=5)
            label.grid(row=row, column=column, padx=10, pady=10, sticky="we")


            column = column + 1

            button = tk.CTkButton(sub_main_grid, text="W", font=("Arial", 16), width=40, height=20, command=lambda entry=entry: calculate_result(entry, below_inventory_frame=below_inventory_frame))
            button.grid(row=row, column=column, padx=10, pady=10)

            column = column + 1

            checkbox = tk.CTkCheckBox(sub_main_grid, text="", font=("Arial", 16), command=lambda entry=entry: get_dict(entry) if checkbox.get() == 0 else None)
            checkbox.grid(row=row, column=column, padx=10, pady=10)

            checkboxes[entry] = [checkbox, False]

            column = column + 1

            if(column >= 4):
                column = 0
                row = row + 1

    def currentSelection(event):
        if drop.get() == "Körper":
            show_appropriate_skills("Körper")
        elif drop.get() == "Gesellschaft":
            show_appropriate_skills("Gesellschaft")
        elif drop.get() == "Natur":
            show_appropriate_skills("Natur")
        elif drop.get() == "Wissen":
            show_appropriate_skills("Wissen")
        elif drop.get() == "Handwerk":
            show_appropriate_skills("Handwerk")
            
    if not is_open:
        is_open = True
        drop = tk.CTkOptionMenu(master=sub_main_grid, values=options, command=currentSelection)
        drop.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = "NSEW", padx = 20)

        currentSelection(options[0])
    
        window.mainloop()
    

    
    update_text_output(text_output_label, quality, has_succeded, terrible_roll, great_roll, prev_text = text_output_label.cget("text"), skill_to_test= skill_to_test)      



def update_text_output(label, quality = None, has_succeded = None, terrible_roll = None, great_roll = None, prev_text = "", skill_to_test = None):
    success_df = pd.read_csv('success.csv')
    plt.pie(success_df.Value, colors=['green', 'red'], autopct='%1.1f%%')
    plt.legend(['Erfolg', 'Misserfolg'])
    plt.axis('equal')
    plt.title('Erfolgsquote')
    below_inventory = FigureCanvasTkAgg(plt.gcf(), master=below_inventory_frame)
    below_inventory_widget = below_inventory.get_tk_widget()
    below_inventory_widget.grid(column=1, row=0,sticky = "NSEW", padx=30)
    plt.close()
    if great_roll == True:
        label.configure(text= prev_text + "\n \nTeste die Fähigkeit: {}".format(skill_to_test) + "\n Du hast eine 1 gewürfelt und grandios bestanden!")
    elif terrible_roll == True:
        label.configure(text = prev_text + "\n \nTeste die Fähigkeit: {}".format(skill_to_test) + "\n Du hast eine 20 gewürfelt. Etwas schlimmes wird passieren!")
    elif has_succeded == True:
        label.configure(text= prev_text + "\n\nTeste die Fähigkeit: {}".format(skill_to_test) + "\n Test bestanden! Dein qualitätslevel beträgt: {}".format(quality))
    elif has_succeded == False:
        label.configure(text= prev_text + "\n\nTeste die Fähigkeit: {}".format(skill_to_test) + "\n Leider hast du nicht bestanden!")

counter = [0]
checkboxes_to_deselect = []
def update_show_necessary_stats(dictionary_skills = None, dictionary_main_stats = None, skill = None, label = None, prev_text = ""):
    counter[0] = counter[0] + 1
    if counter[0] > 2:
        new_text = prev_text.split("\n")
        new_text = new_text[1:] 
        text = "".join(new_text).split(":")[0]
        prev_text = "\n".join(new_text)
        checkboxes_to_deselect.append(checkboxes[text][0])
        if  counter[0] > 3:
            checkboxes_to_deselect[0].deselect()
            checkboxes_to_deselect.pop(0)
            checkboxes[text][1] = False

    
    
    temp = []
    values = []
    for entry in dictionary_main_stats:
        if entry == skill:
            temp = dictionary_main_stats[entry]
    
    for main_stat in temp:
        values.append(dictionary_skills[main_stat])
    
    values.append(dictionary_skills[skill])
    temp.append(skill)
    label.configure(text = prev_text + "\n{}:   {}: {}, {}: {}, {}: {}, {}: {}".format(temp[3] ,temp[0], values[0], temp[1], values[1], temp[2], values[2], temp[3], values[3]))

    
        
def calculate_result(skill_to_test, below_inventory_frame, select_string = None):
    df = pd.read_csv("main_stat_data.csv")
    if select_string != None:
        below_inventory = FigureCanvasTkAgg(plt.gcf(), master=below_inventory_frame)
        ax = plt.subplot(1,1,1)
        df = df.sort_values(by='Value', ascending=False)
        plt.bar(df.Key, df.Value, color=['red', 'purple', 'green', 'black', 'yellow', 'blue', 'gray', 'orange'])
        ax.set_xticks(range(len(df.Key)))
        ax.set_xticklabels(df.Key)
        plt.title('Main Stat Nutzung')
        below_inventory_widget = below_inventory.get_tk_widget()
        below_inventory_widget.grid(column=0, row=0,sticky = "NSEW",padx=100)
        plt.close()
    elif select_string == None:
        Database.databaseLogic("calculate", data, skill_to_test=skill_to_test, df=df, select_string=select_string, below_inventory_frame=below_inventory_frame)



    
        

