# allomalar = {
#     "Abu Abdulloh Muhammad ibn Ismoil" : {"yil": 810, "yosh": 60, "manzil": "Buxoro"},
#     "Abdulla Qodiriy": {"yil": 1894, "yosh": 44, "manzil": "Toshkent"},
#     "Erkin Vohidov ": {"yil": 1936, "yosh": 80, "manzil": "Farg\'ona"},
#     "Alisher Navoiy": {"yil": 1441, "yosh": 60, "manzil": "Xirot"},
#
# }
# for alloma, mal in allomalar.items():
#     print(f"{alloma} {mal['yil']}-yilda {mal['manzil']}da tavallud topgan. {mal['yosh']} da vafot etgan.")

# Lug'atlar
tolstoy ={
    "ismi": "Lev Tolstoy",
    "asarlar": ["Anna Karenina", "Savaş ve Barış", "İvan İlyiç'in Ölümü"]
}

dostoyevski ={
    "ismi": "Fyodor Dostoyevski",
    "asarlar": ["Suç ve Ceza", "Karamazov Kardeşler", "Budala"]}


gogol ={
    "ismi": "Nikolay Gogol",
    "asarlar": ["Ölü Canlar", "Palto", "Burun"]}


# For tsikli yordamida lug'atlardan muallifning ismi va asarlari chiqariladi
for muallif in [tolstoy, dostoyevski, gogol]:
    print(muallif["ismi"])
    for asar in muallif["asarlar"]:
        print("-" + asar)
