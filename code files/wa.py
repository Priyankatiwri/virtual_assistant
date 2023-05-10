import pywhatkit
def Wa(text):
    contacts = {"Karuna": "+919171212076","Mansi": "+917000716828","Fabin": "+919109044555","Mitushi Mam": "+918770907122"}
    pywhatkit.sendwhatmsg_instantly(phone_no=contacts["Karuna"], message=text,)