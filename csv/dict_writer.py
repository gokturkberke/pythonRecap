from csv import DictWriter

with open("films.csv","w") as file:
    headers = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"]
    #sutun basliklarini tanimladik
    csv_writer =DictWriter(file,headers)
    #dictwriter sinifinin bir ornegini olustururken dosya ve basliklari parametre olarak veriyoruz
    csv_writer.writeheader() #tanimlanan basliklari csv dosyasina yazar
    
    csv_writer.writerows([   
        {
        "Title" : "The Shawshank Redemptions",
        "Genre" : "Drama",
        "Premiere" : "1994",
        "Runtime" : "142",
        "IMDB Score" : "9.3",
        "Language" : "English"
    },
    {
        "Title" : "Matrix",
        "Genre" : "Fantastic",
        "Premiere" : "1999",
        "Runtime" : "136",
        "IMDB Score" : "8.1",
        "Language" : "English"
    }
    ])