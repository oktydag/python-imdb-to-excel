import requests
from bs4 import BeautifulSoup
from Handlers.worksheet import *


try:

    def get_valid_text_in_source(source):
        return source.text.strip().replace("\n" , "")

    def get_valid_image_in_source(source):
        return source.a.img['src']

    imdb_url = "https://www.imdb.com/chart/top/"

    try:
        rating_input = float(input("Please Enter Min the Rating : "))
    except Exception as error:
         print("Please give a valid rating number such as 8.6")
         exit()

    response_as_html = requests.get(imdb_url).content
    soup_res = BeautifulSoup(response_as_html, "html.parser")

    titles = soup_res.findAll("td",{"class" : "titleColumn"})
    ratings = soup_res.findAll("td",{"class" : "ratingColumn imdbRating"})
    images = soup_res.find_all("td",{"class" : "posterColumn"})

    worksheet_helper = WorksheetHandler()
    workbook = worksheet_helper.create_worksheet("Movie Name", "Movie Rating", "Movie Image")

    for title,rating,image in zip(titles,ratings,images):
        title  = get_valid_text_in_source(title)
        rating = get_valid_text_in_source(rating)
        image = get_valid_image_in_source(image)

        if float(rating) >= rating_input:
            worksheet_helper.append_in_worksheet(workbook, title,rating,image)

    print("Done ! You can find movies whose rating is bigger than ", str(rating_input))

except Exception as error:
    print("Error: ", str(error))
    exit()
