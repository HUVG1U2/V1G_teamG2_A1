#School: Hogeschool Utrecht
#Docent: Patrick Ubags
#Klas: ICT-V1G
#Team: G2
#Opdracht: A1
#Laatste versie gemaakt op: 30 oktober 2015
#Door: Bas Vermeij, Christiaan Ileana, Enes Cetintas, Kevin van Gils en Victor Duits
#Speciale dank aan Victor Duits voor zijn grote bijdrage aan dit project.


import os, sys, xmltodict, requests, xml, time
from tkinter import *
from PIL import Image, ImageTk
from xml.etree import ElementTree
from time import *


#Font eigenschappen titels
title_font =("Helvetica", 50)
title_font2 =("Helvetica", 20)

#grootte scherm
width = 1024
height = 768
#grootte taalimages
size_taal_image = 75
size_image_padding = 20
taalbalk_padding = 0
size_button_stop = 170


#aanmaak kleuren:
achtergrond_kleur="#FFCC18"
orangekleur=achtergrond_kleur
gelekleur=achtergrond_kleur
talenbalk_kleur="#01015C" #echte: #01015C
bovenbalk_kleur=achtergrond_kleur #echte: pink
buttonbalk_kleur=achtergrond_kleur #echte: rood
boven_buttonbalk_kleur=achtergrond_kleur #echte: rood
boven_taalbalk_kleur=achtergrond_kleur #echte: cyan
apibalk_kleur=achtergrond_kleur #echte: green
apibalk_kleur_2=achtergrond_kleur #wit ofzo
ns_letter_kleur="#01015C"
vertraging_letter_kleur="#CE0F0C"

#gerelateerd aan buttons
tekstcolor=("white")
achtergrondcolor=("#01015C")
button_hoogte=(3)
button_breedte=(14)
button_font = ("Helvetica", 15)


#================================
#Stations
#================================

#stations.xml inladen
dom = ElementTree.parse('stations.xml')
#Locatie Kaartautomaat
station_huidig = 'Utrecht Centraal'
#Aanmaken van lege lijst
station = None
stations = []

#api
stationtext = station_huidig
station_limiet = 10
station_font = ("Helvetica", 15)
station_font_kopjes = ("Helvetica", 15,"bold")


#Inladen van alleen nederlandse stations
for station in dom.findall('Station'):
    land = station.find('Land').text
    if land == 'NL' :
        stations.append(station.find('Namen/Lang').text)
#Check stations
#print(stations)

locatie = 0 #int(input("Geef 0 voor huidig, 1 voor een andere locatie: "))

#================================
#Tkinter
#================================

class Window(Frame):
    def __init__(self, master =None):
        """Initialiseer de master tkinter window in de klasse Window"""
        Frame.__init__(self, master)
        self.master =master

    def ini_GUI_calctaal(self):
        if taalbalk_padding == 0:
            grootte = (width-(size_image_padding*3+size_taal_image*2))
        elif taalbalk_padding == 1:
            grootte = 570
        return grootte


    def init_GUI_Start(self):
        """Het beginscherm wordt in deze functie gedefinieerd."""
        self.master.title("NS Kaartautomaat")
        self.configure(background ="#FFCC18")

        #frame dat alles omvat
        global content
        content = Frame(self, width=width, height=height,background =orangekleur)
        content.grid(column=0, row=0)

        #Decoratiebalken - Vormen de tabel, Door het geven van een andere kleur is bugtesten/plaatsen van objecten simpel
        global boven_balk
        boven_balk = Frame(self, width =width, height =100, background=bovenbalk_kleur, highlightthickness =0)
        boven_balk.grid(row=0,column=0,in_=content,columnspan=8,sticky=W)

        global talen_balk
        talen_balk = Frame(self, width =width, height =80, background=talenbalk_kleur, highlightthickness =0)
        talen_balk.grid(row=22,column=0,in_=content,columnspan=8)


        #NL afbeelding in blauwe balk
        load2 = Image.open("NL.png")
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self, image =render2, background =talenbalk_kleur,highlightthickness =0,borderwidth=0)
        img2.image = render2
        img2.grid(row=0,column=0, in_=talen_balk,pady=size_image_padding,padx=size_image_padding)

        #UK afbeelding in blauwe balk
        load3 = Image.open("UK.png")
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image =render3, background =talenbalk_kleur,highlightthickness =0,borderwidth=0)
        img3.image = render3
        img3.grid(row=0,column=1, in_=talen_balk,pady=size_image_padding,padx=(size_image_padding,self.ini_GUI_calctaal()))

        #Laad file menu in
        self.init_GUI_File_menu()

    def init_GUI_File_menu(self):
        """Maakt de File en Help menu aan in het tkinter window."""

        #File menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label ="Exit", command =self.client_exit)
        menu.add_cascade(label ="File", menu =file)

        #Help menu
        help = Menu(menu)
        help.add_command(label = "ReadMe", command =self.client_help)
        menu.add_cascade(label ="Help", menu =help)

    def init_GUI_Beginscherm(self):
        """Beginscherm interface wordt met deze functie verder uitgebreid met knoppen, ns logo en titel"""

        #Welkom bij NS - titel in Tkinter window
        text = Label(self, text="Welkom bij NS", font =title_font, background =achtergrond_kleur, foreground =ns_letter_kleur)
        text.grid(row=1,column=2, in_=content, columnspan=6)
        #NS afbeelding
        load1 = Image.open("NS.jpg")
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image =render1, background =achtergrond_kleur)
        img1.image = render1
        img1.grid(row=2,column=2, in_=content, columnspan=6)

        button_balk = Frame(self, width =width, height =100, background=buttonbalk_kleur, highlightthickness =0)
        button_balk.grid(row=20,column=0,in_=content,columnspan=8)
        vlak_boven_knoppen = Canvas(self, width =width, height =58, background=boven_buttonbalk_kleur, highlightthickness =0)
        vlak_boven_knoppen.grid(row=6,column=3,in_=content,columnspan=8)
        vlak_boven_taal = Canvas(self, width =width, height =90, background=boven_taalbalk_kleur, highlightthickness =0)
        vlak_boven_taal.grid(row=21,column=0,in_=content,columnspan=8)

        mbutton1 = Button(self,text ='Ik wil naar \nAmsterdam', font=button_font, fg=tekstcolor, bg=achtergrondcolor, height=button_hoogte, width=button_breedte,borderwidth=0).grid(row=0,column=1, in_=button_balk,padx=(92,5))
        mbutton2 = Button(self,text ='Kopen \nlost kaartje', font=button_font, fg=tekstcolor, bg=achtergrondcolor, height=button_hoogte, width=button_breedte,borderwidth=0).grid(row=0,column=2, in_=button_balk,padx=5)
        mbutton3 = Button(self,text ='Kopen \nOV-chipkaart', font=button_font, fg=tekstcolor, bg=achtergrondcolor, height=button_hoogte, width=button_breedte,borderwidth=0).grid(row=0,column=3, in_=button_balk,padx=5)
        mbutton4 = Button(self,text ='Ik wil naar het \n buitenland', font=button_font, fg=tekstcolor, bg=achtergrondcolor, height=button_hoogte, width=button_breedte,borderwidth=0).grid(row=0,column=4, in_=button_balk,padx=5)
        mbutton5 = Button(self,text ='Vertrektijden', font=button_font, fg=tekstcolor, bg=achtergrondcolor, height=button_hoogte, width=button_breedte, command = execute,borderwidth=0).grid(row=0,column=5, in_=button_balk,padx=(5,92))

    def init_GUI_actueel(self):
        """Maakt de tkinter GUI voor vertrektijden"""
        self.master.title("NS vertrektijden")
        self.configure(background =achtergrond_kleur)

        global api_balk
        api_balk = Frame(self, width =width, height =100, background=apibalk_kleur, highlightthickness =0)
        api_balk.grid(row=2,column=0,in_=content,columnspan=8)

        text_storingenbalk = Label(self, text="%s"%self.init_GUI_detijd(),relief=GROOVE , font =title_font2, background =bovenbalk_kleur, foreground =ns_letter_kleur)
        text_storingenbalk.grid(row=0,column=0,in_=boven_balk,padx=(8,150),pady=31,sticky=W)
        back = Button(self, text ="Ververs", font=("Helvetica", 20), justify=LEFT, fg ="white", bg ="#DD0A06",borderwidth=0, highlightthickness =0, command =lambda: executerefresh()).grid(row=0,column=2, in_=boven_balk,padx=(0,5))


        vlak_vertrektijden = Canvas(self, width =width, height =70, background=boven_taalbalk_kleur, highlightthickness =0)
        vlak_vertrektijden.grid(row=1,column=0,in_=content,columnspan=8,sticky=W)
        text_vertrektijden = Label(self, text="Vertrektijden:", font =title_font2, background =boven_taalbalk_kleur, foreground =ns_letter_kleur)
        text_vertrektijden.grid(row=0,column=0,in_=vlak_vertrektijden,padx=(5,0),pady=16, sticky=W)

        vlak_in_vertrektijden = Canvas(self, width =width, height =70, background=boven_taalbalk_kleur, highlightthickness =0)
        vlak_in_vertrektijden.grid(row=0,column=1,in_=vlak_vertrektijden,columnspan=8)
        text_vertrekstation = Label(self, text="%s"%(stationtext), font =title_font2, background =boven_taalbalk_kleur, foreground =ns_letter_kleur)
        text_vertrekstation.grid(row=0,column=0,in_=vlak_in_vertrektijden,padx=(8,80),pady=16)

        back = Button(self, text ="Stoppen \nNaar beginscherm", font=("Helvetica", 20), justify=LEFT, fg ="white", bg ="#DD0A06",borderwidth=0, highlightthickness =0, command =lambda: go_back()).grid(row=0,column=2, in_=talen_balk,padx=(0,5))
        station_input_knop = Button(self, text ="Kies ander station", font=("Helvetica", 20), justify=LEFT, fg =tekstcolor, bg =achtergrondcolor,borderwidth=0, highlightthickness =0, command =lambda: input_station_window()).grid(row=0,column=1, in_=boven_balk,sticky=E)

    def init_GUI_detijd(self):
        """Geeft de huidige tijd wanneer functie wordt uitgevoerd"""
        lokaal = localtime(time())
        hu= (lokaal[3])
        mu= (lokaal[4])
        if hu < 10:
            hf = ("0"+str(hu))
        else:
            hf = hu
        if mu < 10:
            mf = ("0"+str(mu))
        else:
            mf = mu
        return(str(hf)+":"+str(mf))

    def init_GUI_station_veranderen(self):
        self.master.title("NS station invoeren")
        self.configure(background =achtergrond_kleur)
        vlak_in_vertrektijden = Canvas(self, width =width, height =70, background=boven_taalbalk_kleur, highlightthickness =0)
        veld_vul_balk = Frame(self, width =width, height =566, background=apibalk_kleur, highlightthickness =0)
        veld_vul_balk.grid(row=2,column=0,in_=content,columnspan=8)
        Label(self, text="Voer een station in:", font=("Helvetica", 20), fg =ns_letter_kleur, bg =achtergrond_kleur,borderwidth=0, highlightthickness =0,).grid(row=1, column=0, in_=boven_balk, pady=4)
        global e1
        e1 = Entry(self)
        e1.grid(row=1, column=1, in_=boven_balk)
        Button(self, text='Verwerk', font=("Helvetica", 20), fg =tekstcolor, bg =achtergrondcolor,borderwidth=0, highlightthickness =0, command=self.init_show_entry_fields).grid(row=2, column=2, sticky=W, pady=4, in_=boven_balk)

        back = Button(self, text ="Stoppen \nNaar beginscherm", font=("Helvetica", 20), justify=LEFT, fg ="white", bg ="#DD0A06",borderwidth=0, highlightthickness =0, command =lambda: go_back2()).grid(row=0,column=2, in_=talen_balk,padx=(0,5))

    def init_show_entry_fields(self):
        station_in= e1.get()
        # Check for station in stations
        global stationtext
        if station_in in stations:
            stationtext = station_in
            execute2()
        # Check of met een hoofdletter het wel in de lijst staat en zet om naar hoofdletter
        elif station_in.title() in stations:
            station_in = station_in.title()
            stationtext = station_in
            execute2()
        else:
            # Als het station niet gevonden is - geef melding (end laat station met hoofdletter beginnen)
            Label(self, text="Station niet gevonden, probeer het nogmaals", font=("Helvetica", 20), fg =ns_letter_kleur, bg =achtergrond_kleur,borderwidth=0, highlightthickness =0).grid(row=2, column=3, in_=boven_balk,columnspan=4)
            #print("Station niet gevonden, probeer het nogmaals.")
        e1.delete(0,END)

    def init_GUI_resultaten(self, row,eindbestemming,treinsoort,via,vertrektijd,spoor,vertraging):
        """maakt de tabel aan voor vertrektijden"""
        columnlijst = [vertrektijd,vertraging,eindbestemming,spoor,via,treinsoort]
        for column in range(6):

            if row == 0:
                Label(self, text='%s'%(columnlijst[column]),font=station_font_kopjes,foreground =ns_letter_kleur, borderwidth=10,background =apibalk_kleur ).grid(row=row,column=column, in_=api_balk)
            else:
                if column == 1:
                    Label(self, text='%s'%(columnlijst[column]),font=station_font,foreground =vertraging_letter_kleur ,borderwidth=10,background =apibalk_kleur ).grid(row=row,column=column, in_=api_balk)
                else:
                    Label(self, text='%s'%(columnlijst[column]),font=station_font,foreground =ns_letter_kleur ,borderwidth=10,background =apibalk_kleur_2 ).grid(row=row,column=column, in_=api_balk)

    def init_GUI_NSAPI(self):
        """authenticatie met NS servers om xml file voor vertrektijden op te vragen"""
        auth_details = ('bas.vermeij@student.hu.nl', 'BM0zjuAZtA2xiaEEYU0A-YAhRgcAjIcpLheW6ExDTqsaBpom64Fhyg')
        #vraagstation = input('Station: ')
        vraagstation = stationtext
        response = requests.get('http://webservices.ns.nl/ns-api-avt?station='+vraagstation, auth=auth_details)
        parseXML = xmltodict.parse(response.text)
        row = 0
        #initeer
        limiet = station_limiet
        for station in parseXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            if limiet > 0:
                if row == 0:
                    self.init_GUI_resultaten(row,"Naar","Reisdetails","Via","Tijd","Spoor","    ")
                    row += 1
                limiet -= 1
                tijd = station['VertrekTijd']
                #Zet tijd om in leesbaar formaat
                tijddif = tijd[11:-8]
                try:
                    via = (' via '+station['RouteTekst'])
                except:
                    via = ''

                try:
                    vertraging = (station['VertrekVertragingTekst'])
                except:
                    vertraging = ''

                row += 1
                r_row = row
                r_eindbestemming = station['EindBestemming']
                r_treinsoort = station['TreinSoort']
                r_via = via
                r_vertrektijd = tijddif
                r_spoor = station['VertrekSpoor']['#text']
                r_vertraging = vertraging
                self.init_GUI_resultaten(r_row,r_eindbestemming,r_treinsoort,r_via,r_vertrektijd,r_spoor,r_vertraging)
            else:
                break

    def client_exit(self):
        """Sluit het programma af in het File menu"""
        exit()

    def client_help(self):
        """Opent de Readme.txt met notepad (Windows vereist) via de Help menu in het tkinter window"""
        os.system("notepad.exe ReadMe.txt")

#Einde Class
#=====================


def SchermFuncties(onderdeel):
    """Beschrijft wanneer een andere functie moet worden uitgevoerd."""
    currentap = Window(root)
    currentap.init_GUI_Start()
    currentap.init_GUI_File_menu()
    if onderdeel == "beginscherm":
        currentap.init_GUI_Beginscherm()
    elif onderdeel == "vertrektijden":
        currentap.init_GUI_actueel()
        currentap.init_GUI_NSAPI()
    elif onderdeel == "stationinput":
        currentap.init_GUI_station_veranderen()
    currentap.pack(fill =BOTH, expand =1)
    return currentap

def Scherm1():
    global taalbalk_padding
    taalbalk_padding = 0
    global app
    app = SchermFuncties('beginscherm')

#Button vertrektijden gebruikt en voert nu dit uit

def execute():
    global taalbalk_padding
    taalbalk_padding = 1
    app.destroy()
    global app2
    app2 = SchermFuncties('vertrektijden')

def execute2():
    global taalbalk_padding
    taalbalk_padding = 1
    app3.destroy()
    global app2
    app2 = SchermFuncties('vertrektijden')

def executerefresh():
    global taalbalk_padding
    taalbalk_padding = 1
    app2.destroy()
    start2()

def start2():
    global app2
    app2 = SchermFuncties('vertrektijden')

def go_back():
    global stationtext
    stationtext = station_huidig
    app2.destroy()
    Scherm1()

def go_back2():
    global stationtext
    stationtext = station_huidig
    app3.destroy()
    Scherm1()

def input_station_window():
    global taalbalk_padding
    taalbalk_padding = 1
    app2.destroy()
    global app3
    app3 = SchermFuncties('stationinput')



#=============================
#Uitvoerend gedeelte
#=============================

root = Tk()

#root.geometry(str(width) + "x" + str(height))
root.maxsize(width, height)
root.minsize(width, height)
root.iconbitmap("favicon.ico")

Scherm1()
root.mainloop()