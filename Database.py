import psycopg2
import psycopg2.extras
import Utility
import MainWindow
import MainLogic
import pandas as pd
import matplotlib as plt


skills_list = [
        "MU", "KL", "IN", "CH", "FF", "GE", "KO", "KK",
        "Fliegen",
        "Gaukeleien",
        "Klettern",
        "Körperbeherrschung",
        "Kraftakt",
        "Reiten",
        "Schwimmen",
        "Selbstbeherrschung",
        "Singen",
        "Sinnesschärfe",
        "Tanzen",
        "Taschendiebstahl",
        "Verbergen",
        "Zechen",
        "Bekehren_Überzeugen",
        "Betören",
        "Einschüchtern",
        "Etikette",
        "Gassenwissen",
        "Menschenkenntnis",
        "Überreden",
        "Verkleiden",
        "Willenskraft",
        "Fährtensuchen",
        "Fesseln",
        "Fischen_Angeln",
        "Orientierung",
        "Pflanzenkunde",
        "Tierkunde",
        "Wildnisleben",
        "Brett_Glücksspiel",
        "Geographie",
        "Geschichtswissen",
        "Götter_Kulte",
        "Kriegskunst",
        "Magiekunde",
        "Mechanik",
        "Rechnen",
        "Rechtskunde",
        "Sagen_Legenden",
        "Sphärenkunde",
        "Sternkunde",
        "Alchimie",
        "Boote_Schiffe",
        "Fahrzeuge",
        "Handel",
        "Heilkunde_Gift",
        "Heilkunde_Krankheiten",
        "Heilkunde_Seele",
        "Heilkunde_Wunden",
        "Holzbearbeitung",
        "Kochen",
        "Lederbearbeitung",
        "Malen_Zeichnen",
        "Metallbearbeitung",
        "Musizieren",
        "Schlösserknacken",
        "Steinbearbeitung",
        "Stoffbearbeitung"
    ]

def databaseLogic(key = None, skill_entry_dict= None, name_entry= None, password_entry= None, skill_to_test=None, entry = None, items = None, destroy = False, df=None, below_inventory_frame=None, select_string=None):
    global current_id
    current_user_id = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="DSA",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


        #insert logic for skills and main stats
        if key == "character":
            insert_into_skills = ('''
            INSERT INTO skills (
                id, fliegen, gaukeleien, klettern, körperbeherrschung, kraftakt, reiten, schwimmen, selbstbeherrschung, singen, sinnesschärfe, tanzen, taschendiebstahl, verbergen, zechen, bekehren_überzeugen, betören, einschüchtern, etikette, gassenwissen, menschenkenntnis, überreden, verkleiden, willenskraft, fährtensuchen, fesseln, fischen_angeln, orientierung, pflanzenkunde, tierkunde, wildnisleben, brett_glücksspiel, geographie, geschichtswissen, götter_kulte, kriegskunst, magiekunde, mechanik, rechnen, rechtskunde, sagen_legenden, sphärenkunde, sternkunde, alchimie, boote_schiffe, fahrzeuge, handel, heilkunde_gift, heilkunde_krankheiten, heilkunde_seele, heilkunde_wunden, holzbearbeitung, kochen, lederbearbeitung, malen_zeichnen, metallbearbeitung, musizieren, schlösserknacken, steinbearbeitung, stoffbearbeitung
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''')

            insert_into_main_stats = ('''
                INSERT INTO main_stats(id, mu,	kl,	inteligence,ch,	ff,	ge,	ko,	kk)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''')


            cursor.execute('SELECT id FROM skills ORDER BY id DESC LIMIT 1')
            row = cursor.fetchone()

            if row is None:
                biggest_id = 1
            else:
                biggest_id = row[0] + 1
            
            current_id = biggest_id

            insert_value_skills = [biggest_id]
            insert_value_main_stats = [biggest_id]


            
            for item in Utility.SplitDictionary(skill_entry_dict, "Fliegen", "Stoffbearbeitung").keys():
                insert_value_skills.append(skill_entry_dict[item])

            for item in Utility.SplitDictionary(skill_entry_dict, "MU", "KK").keys():
                insert_value_main_stats.append(skill_entry_dict[item])

            cursor.execute(insert_into_skills, tuple(insert_value_skills))
            cursor.execute(insert_into_main_stats, tuple(insert_value_main_stats))


            #insert logic for name and password
            insert_character = ('''
            INSERT INTO character (id, name, password)
            VALUES(%s, %s, %s)
            ''')
            insert_character_values = (biggest_id, name_entry, password_entry)

            cursor.execute(insert_character, insert_character_values)
            connection.commit()
            MainWindow.mainWindow()
        
        elif key == "login":
            cursor.execute('''SELECT id FROM character''')
            ids = Utility.RemoveInnerList(cursor.fetchall())


            select_name_pw = '''SELECT name, password FROM character WHERE id = %s'''
            for id in ids:
                cursor.execute(select_name_pw, (id,))
                name_pw = cursor.fetchone()
                if name_pw == [name_entry, password_entry]:
                    current_id = id

            MainWindow.mainWindow()
            
        elif key == "calculate":
            if select_string == None:
                test_values = None
                for item in skill_entry_dict.keys():
                    if item == skill_to_test:
                        test_values = skill_entry_dict[item]
                
                select_string = ""
                for value in test_values:
                    df.loc[df['Key'] == value, 'Value'] += 1
                    df.to_csv('main_stat_data.csv', index=False)
                    if value.lower() == "in":
                        select_string = select_string + "inteligence" + ","
                        continue
                    select_string = select_string + value.lower() + ","
                
                select_string = select_string + skill_to_test.lower()
                MainWindow.calculate_result(skill_to_test=skill_to_test, below_inventory_frame=below_inventory_frame,select_string=select_string)
                
            select_main_stats_statement = '''
            SELECT {} FROM main_stats, skills WHERE main_stats.id = %s AND skills.id = %s
            '''.format(select_string)
            cursor.execute(select_main_stats_statement, (current_id, current_id))
            values = cursor.fetchall() 
            connection.commit()
            MainLogic.mainLogic(values, skill_to_test= skill_to_test)
        
        elif key == "get_stats_dict":
            stats_dictionary = {}
            for stat in skills_list[:8]:
                if stat == "IN":
                    cursor.execute("""
                    SELECT inteligence FROM main_stats WHERE id = {}""".format(current_id))
                    stats_dictionary[stat] = cursor.fetchone()[0]
                else:
                    cursor.execute("""
                    SELECT {} FROM main_stats WHERE id = {}""".format(stat.lower(), current_id))
                    stats_dictionary[stat] = cursor.fetchone()[0]
            for stat in skills_list[8:]: 
                cursor.execute("""
                SELECT {} FROM skills WHERE id = {}""".format(stat.lower(), current_id))
                stats_dictionary[stat] = cursor.fetchone()[0]
            connection.commit()
            MainWindow.get_dict(dictionary= stats_dictionary, entry= entry)
        

        elif key == "inventory":
            insert_statement = """INSERT INTO inventory (id, item, quantity) VALUES(%s, %s, %s)"""
            update_statement = """UPDATE inventory SET quantity = {} WHERE item = '{}' AND id = {}"""
            current_items_in_db = []
            for item in items:
                print(item)
                cursor.execute("SELECT item, quantity FROM inventory WHERE id = {}".format(current_id))
                everything = cursor.fetchall()
                item[1] = int(item[1])
                if item not in everything and item[0] not in current_items_in_db:
                    item.insert(0, current_id)
                    cursor.execute(insert_statement, item)
                else:
                    cursor.execute(update_statement.format(item[1], item[0], current_id))
                current_items_in_db.append(item[0])
            connection.commit()
            if destroy:
                MainWindow.window.destroy()
        
        elif key == "get_items":
            cursor.execute("""SELECT item, quantity FROM inventory WHERE id = {}""".format(current_id))
            item_and_item_count = cursor.fetchall()
            item2 = []
            items_count = []
            for value in item_and_item_count:
                item2.append(value[0])
                items_count.append(value[1])
            connection.commit()

            MainWindow.mainWindow(items= item2, items_count= items_count)
            


            



        
            









    



        connection.commit()
    except psycopg2.Error as error:
        print("Error connecting to PostgreSQL database:", error)

