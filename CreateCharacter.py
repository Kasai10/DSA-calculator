import customtkinter
import Database


def show_character_creation():
    customtkinter.set_default_color_theme("green")
    customtkinter.set_appearance_mode("dark")

    window = customtkinter.CTk()
    window.geometry("1920x1080")
    window.title('DSA Character Creation')


    frame = customtkinter.CTkScrollableFrame(window)
    frame.pack(fill = customtkinter.BOTH, expand = True)

    name_frame = customtkinter.CTkFrame(frame)
    name_frame.columnconfigure(0, weight=1)
    name_frame.columnconfigure(1, weight=1)



    name_entry = customtkinter.CTkEntry(name_frame, placeholder_text="Name", border_color= 'green', width=300, height=50)
    name_entry.grid(row = 0, column=0, padx = 20)

    password_entry = customtkinter.CTkEntry(name_frame, placeholder_text="Password", border_color= 'green', width=300, height=50 )
    password_entry.grid(row = 0, column=1, padx = 50)


    header_frame = customtkinter.CTkFrame(frame)
    header_frame.columnconfigure(0, weight=1)
    header_frame.columnconfigure(1, weight=1)
    header_frame.columnconfigure(2, weight=1)
    header_frame.columnconfigure(3, weight=1)


    label = customtkinter.CTkLabel(header_frame, text='Gib deine Fähigkeiten an: ', font=('Arial', 60))
    label.grid(row= 0, column = 1, columnspan = 2, sticky = customtkinter.W + customtkinter.E + customtkinter.S)

    main_stats_frame = customtkinter.CTkFrame(frame)
    main_stats_frame.columnconfigure(0, weight=1)
    main_stats_frame.columnconfigure(1, weight=1)
    main_stats_frame.columnconfigure(2, weight=1)
    main_stats_frame.columnconfigure(3, weight=1)
    main_stats_frame.columnconfigure(4, weight=1)
    main_stats_frame.columnconfigure(5, weight=1)
    main_stats_frame.columnconfigure(6, weight=1)
    main_stats_frame.columnconfigure(7, weight=1)
    main_stats_frame.columnconfigure(8, weight=1)
    main_stats_frame.columnconfigure(9, weight=1)
    main_stats_frame.columnconfigure(10, weight=1)
    main_stats_frame.columnconfigure(11, weight=1)
    main_stats_frame.columnconfigure(12, weight=1)
    main_stats_frame.columnconfigure(13, weight=1)
    main_stats_frame.columnconfigure(14, weight=1)
    main_stats_frame.columnconfigure(15, weight=1)

    MU = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='MU')
    MU.grid(row = 0, column = 0, sticky = customtkinter.E + customtkinter.W, padx = 20)
    KL = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='KL')
    KL.grid(row = 0, column = 2, sticky = customtkinter.E + customtkinter.W, padx = 20)
    IN = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='IN')
    IN.grid(row = 0, column = 4, sticky = customtkinter.E + customtkinter.W, padx = 20)
    CH = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='CH')
    CH.grid(row = 0, column = 6, sticky = customtkinter.E + customtkinter.W, padx = 20)
    FF = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='FF')
    FF.grid(row = 0, column = 8, sticky = customtkinter.E + customtkinter.W, padx = 20)
    GE = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='GE')
    GE.grid(row = 0, column = 10, sticky = customtkinter.E + customtkinter.W, padx = 20)
    KO = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='KO')
    KO.grid(row = 0, column = 12, sticky = customtkinter.E + customtkinter.W, padx = 20)
    KK = customtkinter.CTkEntry(main_stats_frame, font=("Arial", 18), placeholder_text='KK')
    KK.grid(row = 0, column = 14, sticky = customtkinter.E + customtkinter.W, padx = 20)


    input_frame = customtkinter.CTkFrame(frame)
    input_frame.columnconfigure(0, weight=1)
    input_frame.columnconfigure(1, weight=1)
    input_frame.columnconfigure(2, weight=1)
    input_frame.columnconfigure(3, weight=1)



    label1 = customtkinter.CTkLabel(input_frame, text="Körper", font=('Arial', 25))
    label1.grid(row = 0, column = 0, pady = 20, padx = 40, sticky= "W", columnspan = 2)


    label3 = customtkinter.CTkLabel(input_frame, text="Klettern", font=('Arial', 16))
    label3.grid(row = 1, column = 0, padx = 10, sticky= "EW")

    Klettern = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Klettern.grid(row = 1, column = 1, sticky = 'EW')


    label1 = customtkinter.CTkLabel(input_frame, text="Körperbeherrschung", font=('Arial', 16))
    label1.grid(row = 1, column = 2, padx = 10, sticky= "EW")

    Körperbeherrschung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Körperbeherrschung.grid(row = 1, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Kraftakt", font=('Arial', 16))
    label1.grid(row = 2, column = 0, padx = 10, sticky= "EW")

    Kraftakt = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Kraftakt.grid(row = 2, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Reiten", font=('Arial', 16))
    label2.grid(row = 2, column = 2, padx = 10, sticky= "EW")

    Reiten = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Reiten.grid(row = 2, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Schwimmen", font=('Arial', 16))
    label3.grid(row = 3, column = 0, padx = 10, sticky= "EW")

    Schwimmen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Schwimmen.grid(row = 3, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Selbstbeherrschung", font=('Arial', 16))
    label4.grid(row = 3, column = 2, padx = 10, sticky= "EW")

    Selbstbeherrschung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Selbstbeherrschung.grid(row = 3, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Singen", font=('Arial', 16))
    label1.grid(row = 4, column = 0, padx = 10, sticky= "EW")

    Singen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Singen.grid(row = 4, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Sinnesschärfe", font=('Arial', 16))
    label2.grid(row = 4, column = 2, padx = 10, sticky= "EW")

    Sinnesschärfe = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Sinnesschärfe.grid(row = 4, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Tanzen", font=('Arial', 16))
    label3.grid(row = 5, column = 0, padx = 10, sticky= "EW")

    Tanzen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Tanzen.grid(row = 5, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Taschendiebstahl", font=('Arial', 16))
    label4.grid(row = 5, column = 2, padx = 10, sticky= "EW")

    Taschendiebstahl = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Taschendiebstahl.grid(row = 5, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Verbergen", font=('Arial', 16))
    label1.grid(row = 6, column = 0, padx = 10, sticky= "EW")

    Verbergen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Verbergen.grid(row = 6, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Zechen", font=('Arial', 16))
    label2.grid(row = 6, column = 2, padx = 10, sticky= "EW")

    Zechen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Zechen.grid(row = 6, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Fliegen", font=('Arial', 16))
    label3.grid(row = 7, column = 0, padx = 10, sticky= "EW")

    Fliegen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Fliegen.grid(row = 7, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Gaukeleien", font=('Arial', 16))
    label4.grid(row = 7, column = 2, padx = 10, sticky= "EW")

    Gaukeleien = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Gaukeleien.grid(row = 7, column = 3, sticky = 'EW')



    #Gesellschaft
    label1 = customtkinter.CTkLabel(input_frame, text="Gesellschaft", font=('Arial', 25))
    label1.grid(row = 8, column = 0, pady = 20, padx = 40, sticky= "W", columnspan = 2)

    label3 = customtkinter.CTkLabel(input_frame, text="Bekehren & Überzeugen", font=('Arial', 16))
    label3.grid(row = 9, column = 0, padx = 10, sticky= "EW")

    Bekehren_Überzeugen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Bekehren_Überzeugen.grid(row = 9, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Betören", font=('Arial', 16))
    label4.grid(row = 9, column = 2, padx = 10, sticky= "EW")

    Betören = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Betören.grid(row = 9, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Einschüchtern", font=('Arial', 16))
    label1.grid(row = 10, column = 0, padx = 10, sticky= "EW")

    Einschüchtern = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Einschüchtern.grid(row = 10, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Etikette", font=('Arial', 16))
    label2.grid(row = 10, column = 2, padx = 10, sticky= "EW")

    Etikette = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Etikette.grid(row = 10, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Gassenwissen", font=('Arial', 16))
    label3.grid(row = 11, column = 0, padx = 10, sticky= "EW")

    Gassenwissen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Gassenwissen.grid(row = 11, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Menschenkenntnis", font=('Arial', 16))
    label4.grid(row = 11, column = 2, padx = 10, sticky= "EW")

    Menschenkenntnis = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Menschenkenntnis.grid(row = 11, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Überreden", font=('Arial', 16))
    label1.grid(row = 12, column = 0, padx = 10, sticky= "EW")

    Überreden = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Überreden.grid(row = 12, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Verkleiden", font=('Arial', 16))
    label2.grid(row = 12, column = 2, padx = 10, sticky= "EW")

    Verkleiden = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Verkleiden.grid(row = 12, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Willenskraft", font=('Arial', 16))
    label3.grid(row = 13, column = 0, padx = 10, sticky= "EW")

    Willenskraft = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Willenskraft.grid(row = 13, column = 1, sticky = 'EW')



    #Natur
    label1 = customtkinter.CTkLabel(input_frame, text="Natur", font=('Arial', 25))
    label1.grid(row = 14, column = 0, pady = 20, padx = 40, sticky= "W", columnspan = 2)

    label3 = customtkinter.CTkLabel(input_frame, text="Fährtensuchen", font=('Arial', 16))
    label3.grid(row = 15, column = 0, padx = 10, sticky= "EW")

    Fährtensuchen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Fährtensuchen.grid(row = 15, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Fesseln", font=('Arial', 16))
    label4.grid(row = 15, column = 2, padx = 10, sticky= "EW")

    Fesseln = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Fesseln.grid(row = 15, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Fischen & Angeln", font=('Arial', 16))
    label1.grid(row = 16, column = 0, padx = 10, sticky= "EW")

    Fischen_Angeln = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Fischen_Angeln.grid(row = 16, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Orientierung", font=('Arial', 16))
    label2.grid(row = 16, column = 2, padx = 10, sticky= "EW")

    Orientierung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Orientierung.grid(row = 16, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Pflanzenkunde", font=('Arial', 16))
    label3.grid(row = 17, column = 0, padx = 10, sticky= "EW")

    Pflanzenkunde = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Pflanzenkunde.grid(row = 17, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Tierkunde", font=('Arial', 16))
    label4.grid(row = 17, column = 2, padx = 10, sticky= "EW")

    Tierkunde = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Tierkunde.grid(row = 17, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Wildnisleben", font=('Arial', 16))
    label1.grid(row = 18, column = 0, padx = 10, sticky= "EW")

    Wildnisleben = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Wildnisleben.grid(row = 18, column = 1, sticky = 'EW')



    #Wissen
    label1 = customtkinter.CTkLabel(input_frame, text="Wissen", font=('Arial', 25))
    label1.grid(row = 19, column = 0, pady = 20, padx = 40, sticky= "W", columnspan = 2)


    label3 = customtkinter.CTkLabel(input_frame, text="Brett- & Glücksspiel", font=('Arial', 16))
    label3.grid(row = 20, column = 0, padx = 10, sticky= "EW")

    Brett_Glücksspiel = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Brett_Glücksspiel.grid(row = 20, column = 1, sticky = 'EW')


    label1 = customtkinter.CTkLabel(input_frame, text="Geographie", font=('Arial', 16))
    label1.grid(row = 20, column = 2, padx = 10, sticky= "EW")

    Geographie = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Geographie.grid(row = 20, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Geschichtswissen", font=('Arial', 16))
    label1.grid(row = 21, column = 0, padx = 10, sticky= "EW")

    Geschichtswissen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Geschichtswissen.grid(row = 21, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Götter & Kulte", font=('Arial', 16))
    label2.grid(row = 21, column = 2, padx = 10, sticky= "EW")

    Götter_Kulte = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Götter_Kulte.grid(row = 21, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Kriegskunst", font=('Arial', 16))
    label3.grid(row = 22, column = 0, padx = 10, sticky= "EW")

    Kriegskunst = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Kriegskunst.grid(row = 22, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Magiekunde", font=('Arial', 16))
    label4.grid(row = 22, column = 2, padx = 10, sticky= "EW")

    Magiekunde = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Magiekunde.grid(row = 22, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Mechanik", font=('Arial', 16))
    label1.grid(row = 23, column = 0, padx = 10, sticky= "EW")

    Mechanik = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Mechanik.grid(row = 23, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Rechnen", font=('Arial', 16))
    label2.grid(row = 23, column = 2, padx = 10, sticky= "EW")

    Rechnen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Rechnen.grid(row = 23, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Rechtskunde", font=('Arial', 16))
    label3.grid(row = 24, column = 0, padx = 10, sticky= "EW")

    Rechtskunde = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Rechtskunde.grid(row = 24, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Sagen & Legenden", font=('Arial', 16))
    label4.grid(row = 24, column = 2, padx = 10, sticky= "EW")

    Sagen_Legenden = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Sagen_Legenden.grid(row = 24, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Sphärenkunde", font=('Arial', 16))
    label1.grid(row = 25, column = 0, padx = 10, sticky= "EW")

    Sphärenkunde = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Sphärenkunde.grid(row = 25, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Sternkunde", font=('Arial', 16))
    label2.grid(row = 25, column = 2, padx = 10, sticky= "EW")

    Sternkunde = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Sternkunde.grid(row = 25, column = 3, sticky = 'EW')



    #Handwerk
    label1 = customtkinter.CTkLabel(input_frame, text="Handwerk", font=('Arial', 25))
    label1.grid(row = 26, column = 0, pady = 20, padx = 40, sticky= "W", columnspan = 2)


    label3 = customtkinter.CTkLabel(input_frame, text="Boote & Schiffe", font=('Arial', 16))
    label3.grid(row = 27, column = 0, padx = 10, sticky= "EW")

    Boote_Schiffe = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Boote_Schiffe.grid(row = 27, column = 1, sticky = 'EW')


    label1 = customtkinter.CTkLabel(input_frame, text="Fahrzeuge", font=('Arial', 16))
    label1.grid(row = 27, column = 2, padx = 10, sticky= "EW")

    Fahrzeuge = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Fahrzeuge.grid(row = 27, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Handel", font=('Arial', 16))
    label1.grid(row = 28, column = 0, padx = 10, sticky= "EW")

    Handel = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Handel.grid(row = 28, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Heilkunde Gift", font=('Arial', 16))
    label2.grid(row = 28, column = 2, padx = 10, sticky= "EW")

    Heilkunde_Gift = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Heilkunde_Gift.grid(row = 28, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Heilkunde Krankheiten", font=('Arial', 16))
    label3.grid(row = 29, column = 0, padx = 10, sticky= "EW")

    Heilkunde_Krankheiten = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Heilkunde_Krankheiten.grid(row = 29, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Heilkunde Seele", font=('Arial', 16))
    label4.grid(row = 29, column = 2, padx = 10, sticky= "EW")

    Heilkunde_Seele = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Heilkunde_Seele.grid(row = 29, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Heilkunde Wunden", font=('Arial', 16))
    label1.grid(row = 30, column = 0, padx = 10, sticky= "EW")

    Heilkunde_Wunden = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Heilkunde_Wunden.grid(row = 30, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Holzbearbeitung", font=('Arial', 16))
    label2.grid(row = 30, column = 2, padx = 10, sticky= "EW")

    Holzbearbeitung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Holzbearbeitung.grid(row = 30, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Kochen", font=('Arial', 16))
    label3.grid(row = 31, column = 0, padx = 10, sticky= "EW")

    Kochen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Kochen.grid(row = 31, column = 1, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Lederbearbeitung", font=('Arial', 16))
    label4.grid(row = 31, column = 2, padx = 10, sticky= "EW")

    Lederbearbeitung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Lederbearbeitung.grid(row = 31, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Malen & Zeichnen", font=('Arial', 16))
    label1.grid(row = 32, column = 0, padx = 10, sticky= "EW")

    Malen_Zeichnen = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Malen_Zeichnen.grid(row = 32, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Metallbearbeitung", font=('Arial', 16))
    label2.grid(row = 32, column = 2, padx = 10, sticky= "EW")

    Metallbearbeitung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Metallbearbeitung.grid(row = 32, column = 3, sticky = 'EW')

    label4 = customtkinter.CTkLabel(input_frame, text="Musizieren", font=('Arial', 16))
    label4.grid(row = 33, column = 2, padx = 10, sticky= "EW")

    Musizieren = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Musizieren.grid(row = 33, column = 3, sticky = 'EW')

    label1 = customtkinter.CTkLabel(input_frame, text="Schlösserknacken", font=('Arial', 16))
    label1.grid(row = 33, column = 0, padx = 10, sticky= "EW")

    Schlösserknacken = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Schlösserknacken.grid(row = 33, column = 1, sticky = 'EW')

    label2 = customtkinter.CTkLabel(input_frame, text="Steinbearbeitung", font=('Arial', 16))
    label2.grid(row = 34, column = 2, padx = 10, sticky= "EW")

    Steinbearbeitung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Steinbearbeitung.grid(row = 34, column = 3, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Stoffbearbeitung", font=('Arial', 16))
    label3.grid(row = 34, column = 0, padx = 10, sticky= "EW")

    Stoffbearbeitung = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Stoffbearbeitung.grid(row = 34, column = 1, sticky = 'EW')

    label3 = customtkinter.CTkLabel(input_frame, text="Alchimie", font=('Arial', 16))
    label3.grid(row = 35, column = 0, padx = 10, sticky= "EW")

    Alchimie = customtkinter.CTkEntry(input_frame, font = ('Arial', 16), placeholder_text='0')
    Alchimie.grid(row = 35, column = 1, sticky = 'EW')



    header_frame.pack(fill = 'both', expand= True, pady = 20)
    name_frame.pack(anchor = 'w', expand = True, pady = 15)
    main_stats_frame.pack(fill = 'both', expand = True)
    input_frame.pack(fill = 'both', expand = True)



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


    global_dict = locals()
    skill_entry_dict = {}
    def retrieveData():
        for skill in skills_list:
            skill_entry_dict[skill] = global_dict[skill].get()
            if skill_entry_dict[skill] == "":
                skill_entry_dict[skill] = "0"
            skill_entry_dict[skill] = int(skill_entry_dict[skill])
        
        name_entry = global_dict["name_entry"].get()
        password_entry = global_dict["password_entry"].get()
        window.withdraw()
        Database.databaseLogic("character", skill_entry_dict, name_entry, password_entry)
        


    submit_skills = customtkinter.CTkButton(header_frame, command=retrieveData, text= "Charakter Erstellen")
    submit_skills.grid(row= 0, column = 3, sticky = customtkinter.E + customtkinter.S + customtkinter.N)

    window.mainloop()




        