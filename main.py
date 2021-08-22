from request import search_movies_by_title, get_movie_by_id

r1 = search_movies_by_title('lion')
r2 = get_movie_by_id('1')
r3 = get_movie_by_id('tt0363771')

print(r1)
print(r2)
print(r3)