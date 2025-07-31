class Album: 
    def __init__(self, album_name, number_of_songs, artist):
        self.name = album_name 
        self.number_of_songs = number_of_songs
        self.artist = artist
    
    # Use __str__ method to format 'Album'
    def __str__(self): 
        return(f"{self.name}, {self.artist}, {self.number_of_songs}")

album1 = Album('Talkie Walkie', 10, 'Air')
album2 = Album('Syro', 12, 'Aphex Twin')
album3 = Album('Post', 13, 'Bjork')
album4 = Album('Untrue', 13, 'Burial')
album5 = Album('Roulette', 11, 'Violet Indiana')

# Store albums in a list 
albums1 = [album1, album2, album3, album4, album5]

print("Original albums1 list: ")
for album in albums1:
    print(album)

# Sort albums1 by number of songs using merge sort
def merge_sort_by_songs(album_list):
    # Base case
    if len(album_list) <= 1:
        return album_list

    mid = len(album_list) // 2 # Find the middle point of the list 
    left = album_list[:mid] # Left half of the list
    right = album_list[mid:] # Right half of the list
    
    # Sort both halves 
    left = merge_sort_by_songs(left) 
    right = merge_sort_by_songs(right) 

    # Merge the two sorted halves
    return merge_by_songs(left, right)

def merge_by_songs(left, right):
    result = [] # Empty list to store the merged result

    i = j = 0 # Indicies to track left and right part of list

    # Compare elements from both lists and append the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i].number_of_songs <= right[j].number_of_songs:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
   
    # Any remaining elements added to the list
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Sort albums1 by number of songs
albums1 = merge_sort_by_songs(albums1)
print("\nSorted albums1 by number of songs:")
for album in albums1:
    print(album)

# Swap index 0 and 1
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\n After swapping index 0 and 1 in albums1:")
for album in albums1: 
    print(album)


# Create albums2 and add 5 albums
album6 = Album('Arular', 14, 'M.I.A')
album7 = Album('Among My Swan', 12, 'Mazzy Star')
album8 = Album('Love Deluxe', 9, 'Sade')
album9 = Album('Stardust', 12, 'Yung Lean')
album10 = Album('A Love Supreme', 4, 'John Coltrane')

albums2 = [album6, album7, album8, album9, album10]
print("\nOriginal albums2 list: ")
for album in albums2:
    print(album)

# Add albums1 to albums2
albums2.extend(albums1)

# Add two albums to the albums2
albums2.append(Album('Dark Side of the Moon', 9, 'Pink Floyd'))
albums2.append(Album('Oops!... I Did It Again', 16, 'Britney Spears'))

# Sort albums2 alphabetically by album name 
def merge_sort_by_name(album_list):
    # Base case
    if len(album_list) <= 1:
        return album_list

    # Split the list
    mid = len(album_list) // 2
    left = album_list[:mid] 
    right = album_list[mid:]  

    left = merge_sort_by_name(left)
    right = merge_sort_by_name(right)

    # Merge the two sorted halves
    return merge_by_name(left, right)

# Helper function to merge two sorted halves based on the album name
def merge_by_name(left, right):
    result = []  # List to store the merged result
    i = j = 0  # Indices to track the left and right lists

    # Compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i].name.lower() <= right[j].name.lower():  # Case-insensitive comparison
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Now sort albums2 by album name
albums2 = merge_sort_by_name(albums2)
print("\nSorted albums2 by album name:")
for album in albums2:
    print(album)

# Search for 'Dark Side of the Moon' in list
search_name = 'dark side of the moon' # case-insensitive typing
index_found = -1 # default if index not found
for i, album in enumerate(albums2):
    if album.name.lower() == search_name: 
        index_found = i
        break 

if index_found != -1:
    print(f"\n'Dark Side of the Moon' found at index {index_found}")
else:
    print("\n 'Dark Side of the Moon' not found in albums2")