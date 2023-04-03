while True:
  print("Sankari on tullut metsään.")
  print("Hän kulkee polkua pitkin.")
  print("Polku jakautuu kolmeen: ")
  print("Oikealle, vasemmalle, suoraan.")
  print("Minkä polun valitset? Vaihtoehdot: V/S/O")

  valinta1 = input()
  if valinta1 == "V":
    print("Menit vasemmalle.")
    print("Näet lohikäärmeen, Taisteletko sitä vastaan?")
    print("Vaihtoehdot: kyllä/ei")
    valinta2 = input()
    if valinta2 == "kyllä":
      print("Taistelit lohikäärmettä vastaan. Kuolit välittömästi. Tarinasi päätyi tähän.")
    elif valinta2 == "ei":
      print("Juoksit karkuun välittömästi lohikäärmeen nähtyäsi. Se oli hyvä päätös, sillä lohikäärme olisi 99% mahdollisuudella tappanut sinut noin yhden sekunnin sisällä.")
    else:
      print("Sankari ei valinnut mitään ja häippäs.")
  elif valinta1 == "S":
    print("Menit suoraan.")
    print("Näet puisen arkun tien poskessa.")
    print("Avaatko hieman epäilyttävän näköisen arkun?")
    print("Vaihtoehdot: kyllä/ei")
    valinta2 = input()
    if valinta2 == "kyllä":
      print("Avasit arkun. Se olikin vain helvetillinen hirviö, joka oli naamioutunut arkuksi. Kuolit mysterisistä syistä. Jos et siis vielä tajunnut, tarinasi päätyi tähän.")
    elif valinta2() == "ei":
      print("Et halunnut ottaa riskiä. Hyvä, sillä et tiennyt mitä sen sisällä oli.")
    else:
      print("Sankari jähmettyi hetkeksi paikalleen, mutta jatkoi matkaa.")
  elif valinta1 == "O":
    print("Löysit pimeän polun pois metsästä.")
    print("Menetkö takaisin metsään?")
    print("kyllä/ei")
    valinta2 = input()
    if valinta2 == "kyllä":
      print("Menit takaisin metsään...")
    elif valinta2 == "ei":
     print("Juoksit pois metsästä. Peli loppuu tähän.")
    else:
     print("Sankari ei valinnut mitään ja jäi seisomaan paikalleen.")