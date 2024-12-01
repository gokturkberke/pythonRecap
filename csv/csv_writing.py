from csv import writer

# with open("cars.csv","w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Brand", "Model"])
#     csv_writer.writerow(["Honda", "Civic"])
#     csv_writer.writerow(["Honda", "Accord"])
    
with open("cars.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerows([["Brand", "Model"],["Honda", "Civic"],["Honda", "Accord"]])
    #ustteki yorum satirinin aynisini boyle yazabiliriz
    
with open("cars.csv","a") as file: #yeni arabalar ekleme
    csv_writer = writer(file)
    csv_writer.writerows([["Honda","City"],["Audi","A4"]])
    