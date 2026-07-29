import mysql.connector

# Connect mySQL and python :- 
conn = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'Test@1234',
	database = 'movie_tracker'
)

if conn.is_connected():
	print("Database is connected successfully ! ")

# Add cursor :-
cursor = conn.cursor()

# EXample To check cursor :- 
# cursor.execute("SHOW TABLES")
# for table in cursor:
# 	print(table)

# TO VIEW ALL THE MOVIES IN OUR DATABASE :-
def view_movies():
	cursor.execute('SELECT * FROM movies')
	movies = cursor.fetchall()
	for movie in movies:
		print(movie)

# TO SEARCH PARTICULAR MOVIE IN OUR DATABASE :-
def search_movie():
	movie_name = input("Enter movie you want : ")
	query_search = 'SELECT * FROM movies WHERE movie_name = %s'
	cursor.execute(query_search , (movie_name,))
	result = cursor.fetchone()
	if result:
		print(result)
	else:
		print("Not found")

# TO ADD NEW MOVIE IN OUR DATABASE :-
def Add_movies():
    try:
        movie_name = input("Enter new movie name : ")
        genre = input("Enter genre : ")
        language = input("Enter the language : ")
        rating = float(input("Enter rating : "))
        status = input("Enter status : ")
        release_year = int(input("Enter release year of your movie : "))
        insert_query = """
        INSERT INTO movies
        (movie_name, genre, language, rating, status, release_year)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (movie_name, genre, language, rating, status, release_year)

        cursor.execute(insert_query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("Your movie is successfully added!")
        else:
            print("Movie not added!")

    except ValueError:
        print("Invalid input! Enter valid rating and release year.")

    except Exception as e:
        print("Database Error:", e)

# TO UPDATE MOVIE IN OUR DATABASE :-
def upd_movies():
	try:
		movie_name = input("Enter movie name : ")
		New_language = input("Enter new language : ")
		New_rating = float(input("Enter new rating : "))
		New_status = input("Enter new status : ")
		query_upd = """UPDATE movies SET status = %s,rating = %s ,language = %s WHERE movie_name = %s"""
		values = (New_status , New_rating , New_language , movie_name)
		cursor.execute(query_upd , values )
		conn.commit()
		if cursor.rowcount > 0:
			print("Your movie is updated successfully ! ")
		else:
			print("NOT FOUND !")
	except ValueError:
		print("Please enter valid info ! ")
	except Exception as e:
		print("DATABASE ERROR : " , e)

# TO DELETE MOVIE IN OUR DATABASE :- 
def dlt_movies():
	movie_name = input("Enter movie name : ")
	query_dlt = """DELETE FROM movies WHERE movie_name = %s"""
	cursor.execute(query_dlt , (movie_name,))
	conn.commit()
	if cursor.rowcount > 0:
		print("Your movie is successfully deleted ! ")
	else:
		print("Not found")


menu = """MOVIE TRACKER
1.View_movie
2.Search_movie
3.Add_movie
4.Update_movie
5.Delete_movie
6.Exit"""
while True:
	print(menu)
	try:
		choice = int(input("Enter your choices : "))
	except ValueError:
		print("Please Enter a number between 1 and 6 only! ")
		continue
	if choice == 1:
		view_movies()
	elif choice == 2:
		search_movie()
	elif choice == 3:
		Add_movies()
	elif choice == 4:
		upd_movies()
	elif choice == 5:
		dlt_movies()
	elif choice == 6:
		break
	else:
		print("Invalid choice! please enter a number between 1 and 6.")
cursor.close()
conn.close()
print('Database connection closed successfully ! ')


	



