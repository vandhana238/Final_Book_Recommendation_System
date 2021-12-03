from flask import Flask, render_template,request
import books
import tqdm
import movies
import missing
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

#This allows flask to receive information from the form and display appropriate info on the results page
@app.route('/result',methods = ['POST', 'GET'])
#This is the main function to call the books module or the movies module
def result():
    titleMain=request.form['title']
    valueOption=request.form['options']
    selectOption=request.form['bmselect']
    #If the user selects books. get the lists using the title
    if(valueOption=="book"):
        #If user selects genre, make listgenre the mainlist
        if selectOption=="genre":
            listsecondary,listmain=books.findbook(titleMain)
        #Else make the other list the main list
        else:
            listmain,listsecondary=books.findbook(titleMain)
        author=books.findAuthor(titleMain)
        print(author)
        for i in author:
            author=i
        #If list does not exist, display error screen
        if not listmain:
            missing.writemissing(titleMain,'book')
            return render_template("error.html",error="list",option=valueOption)
        #Otherwise, display the result screen and find the poster of the book
        else:
            #posterlink=books.findPoster(titleMain,author)
            return render_template("result.html", titleMain=titleMain, listmain=listmain,listsecondary=listsecondary,valueOption=valueOption)
    #The same as above for movies
    else:
        if selectOption=="genre":
            listmain,listsecondary,listtertiary=movies.findMovies(titleMain)
        elif selectOption=="cast":
            listsecondary,listmain,listtertiary=movies.findMovies(titleMain)
        elif selectOption=="collection":
            listsecondary,listtertiary,listmain=movies.findMovies(titleMain)
            if listmain==None:
                return render_template("error.html",error="collection",option=valueOption, selectOption=selectOption)
        
        if not listmain:
            missing.writemissing(titleMain,'movie')
            return render_template("error.html",error="list",option=valueOption, selectOption=selectOption)
        else:
            #posterlink=movies.findPoster(titleMain)
            return render_template("result.html", titleMain=titleMain, listmain=listmain,listsecondary=listsecondary,valueOption=valueOption)
   

          
if __name__ == "__main__":
    app.run(debug=True)

