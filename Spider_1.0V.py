import requests as url
import webbrowser as wb
from bs4 import BeautifulSoup as bs
#
#Spider 1.0V
#
#Spider 1.0V is a programme that use to find and download movies from YTS.ag.
#Spider 1.0V can use to find,
#       ==> Whether the movie has been released or not.
#       ==> Download movies in 1080p or 720p BluRay quality.
#Spider 1.0V is consist with 159 code lines.
#
print('*******************************')
print('*         Spider 1.0V         *')
print('*******************************')
print('')
#
print('Welcome to Spider 1.0V')
print('')
#
#downloadMovie is the finction used to download movies.
#
def downloadMovie(movieType720,movieType1080,urlMovieType1080,urlMovieType720):
    TempmovieType720 = movieType720
    TempmovieType1080 = movieType1080
    TempurlMovieType1080 = urlMovieType1080
    TempurlMovieType720 = urlMovieType720
    if movieType720 == 'no' and movieType1080 == 'no':
        findMovie()
    if movieType720 == 'yes' and movieType1080 == 'yes':
        print('Select download ==>')
        print('')
        print('01. 1080p BluRay')
        print('02. 720p BluRay')
        print('')
        option = int(input('Enter option : '))
        print('')
        if option == 1:
            wb.open(urlMovieType1080)
            print('Your download is completed.')
            print('')
            findMovie()
        if option == 2:
            wb.open(urlMovieType720)
            print('Your download is completed.')
            print('')
            findMovie()
        else:
            print('You have entered a wrong option')
            print('')
            downloadMovie(TempmovieType720,TempmovieType1080,TempurlMovieType1080,TempurlMovieType720)
    if movieType720 == 'no' and movieType1080 == 'yes':
        print('Select download ==>')
        print('')
        print('01. 1080p BluRay')
        print('')
        option = int(input('Enter option : '))
        print('')
        if option == 1:
            wb.open(urlMovieType1080)
            print('Your download is completed.')
            print('')
            findMovie()
        else:
            print('')
            print('You have entered a wrong option')
            print('')
            downloadMovie(TempmovieType720,TempmovieType1080,TempurlMovieType1080,TempurlMovieType720)
    if movieType720 == 'yes' and movieType1080 == 'no':
        print('Select download ==>')
        print('')
        print('01. 720p BluRay')
        print('')
        option = int(input('Enter option : '))
        print('')
        if option == 1:
            wb.open(urlMovieType720)
            print('Your download is completed.')
            print('')
            findMovie()
        else:
            print('You have entered a wrong option')
            print('')
            downloadMovie(TempmovieType720,TempmovieType1080,TempurlMovieType1080,TempurlMovieType720)
#
#download is the finction that you can use to download the torrent file.
#
def download(movieURL,title):
    urlMovieType720 = ''
    urlMovieType1080 = ''
    movieType720 = 'no'
    movieType1080 = 'no'
    sourceCode = url.get(movieURL)
    text = sourceCode.text
    soup = bs(text)
    download720 = 'Download '+title+' 720p Torrent'
    download1080 = 'Download '+title+' 1080p Torrent'
    for movieName in soup.findAll('a',{'title':download720}):
        type = movieName.string
        if type == "720p.BluRay":
            print('')
            print('720p Torrent is available for ',title)
            print('')
            movieType720 = 'yes'
            urlMovieType720 = movieName.get('href')
            break
    for movieName in soup.findAll('a',{'title':download1080}):
        type = movieName.string
        if type == "1080p.BluRay":
            print('1080p Torrent is available for ',title)
            print('')
            movieType1080 = 'yes'
            urlMovieType1080 = movieName.get('href')
            break
    if movieType720 == 'no':
        print('')
        print('720p BluRay Torrent is not available for ',title)
        print('')
    if movieType1080 == 'no':
        print('1080p BluRay Torrent is not available for ',title)
        print('')
    if movieType720 == 'yes' or movieType1080 == 'yes' or movieType720 == 'no' or movieType1080 == 'no':
        downloadMovie(movieType720,movieType1080,urlMovieType1080,urlMovieType720)
#
#spider function is the web crowler
#
def spider(max_pages,movieTitle):
    page = 1
    found = 'no'
    while page <= max_pages:
        wURL = 'https://yts.am/browse-movies?page='+str(page)
        sourceCode = url.get(wURL)
        text = sourceCode.text
        soup = bs(text)
        for link in soup.findAll('a',{'class':'browse-movie-title'}):
            href = link.get('href')
            title = link.string
            titlelower = title.lower()
            if titlelower == movieTitle:
                found = 'yes'
                print('')
                print(title,'is available in YTS.ag.')
                download(href,title)
        page += 1
    if found == 'no':
        print('')
        print(movieTitle,'is not available in YTS.ag.')
        print('')
        findMovie()
#
#findMovie is the function use to find a movie.
#
def findMovie():
    print('Find your movies ==>')
    print('')
    movieTitle = input('Search : ')
    movieTitle = movieTitle.lower()
    spider(561,movieTitle)
findMovie()
