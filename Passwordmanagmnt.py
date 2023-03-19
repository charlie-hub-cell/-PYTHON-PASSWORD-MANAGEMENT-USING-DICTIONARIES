MyPasswords={
    "GB Whatssap":"908690",
    "TryHackMe":"charliewangara@gmail.com",
    "CorseHero":"Brenda",
    "Linkedin":"challotheboy",
    "Facebook":"0748985762895478215",
    "Email":"cha#2@45879",
    "Instagram":"Wuodawuor2233",
    "Tiktok":"C.Brenda",
}
x=input("Enter account:")
if x == "GB Whatssap":
 print("Your GB Whatssap password is",MyPasswords.get("GB Whatssap"))
elif x == "Facebook":
    print("Your Facebook password is", MyPasswords.get("Facebook"))
elif x == "CorseHero":
    print("Your CorseHero password is", MyPasswords.get("CorseHero"))
elif x == "Tiktok":
    print("Your Tiktok password is", MyPasswords.get("Tiktok"))
elif x == "Instagram":
    print("Your Instagram password is", MyPasswords.get("Instagram"))
elif x == "TryHackMe":
    print("Your TryHackMe password is", MyPasswords.get("TryhackMe"))
elif x == "Email":
    print("Your Email password is", MyPasswords.get("Email"))
elif x == "Linkedin":
    print("Your Linkedin password is", MyPasswords.get("Linkedin"))
else:
    print(" User account doesn't Exist!")