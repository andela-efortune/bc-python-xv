"""
	basically what i am about to do is create
	an app used for taking notes using oop
	and this version NotesApplication is currently
	running on the terminal, there are no UIs or DBs
	the notes are simply stored on a list.
	And this note taking application has all the basic
	functionality of an actual note taking application
	with pretty UIs and databases.
	~fortune iyke
	~enjoy
"""

class NotesApplication (object):

	def __init__(self,author=None):
		'''
			the initialisation of the 
			NoteApplication object for which the author 
			parameter is  first initialized to None
			This is an empty list which holds the created 
			note in a list 
		'''  
		self.author = author
		self.note_name = [] 

	def create(self,note_content):
		'''
			The create method basically allows notes 
			to be created within the note_content parameter
			The created note is now appended into that empty list
		'''
		self.note_content = note_content
		self.note_name.append(self.note_content) 

	def list(self):
		'''
			Here this list method allows the created 
			notes to be listed based on the index number 
			of that list
			loops througn the list of the created notes
			and returns the index number of the particular 
			note 
			the variable self.ls holds the note in our 
			required format
			and then self.ls is printed
		''' 
		self.ls = ''
		for i in self.note_name:
			self.i_idex = self.note_name.index(i) 
			self.ls = "Note ID: %s \n %r \n By Author: %s" % \
			(self.i_idex, self.note_name, self.author) 
			print self.ls 

	def get(self,note_id): 
		'''
			this get method takes in the index number 
			of a particular note and returns the note 
			in a string 
			prints in a string format
		'''
		self.note_id = note_id
		print str(self.note_name[int(self.note_id)]) 
		

	def search(self, search_text):
	    if search_text != "": 
	    	add = "Showing results for search \"[<"+search_text+">]\"" 
	    	for i in self.note_name: 
	    		if search_text in i: 
	    			note_id = self.note_name.index(i) 
	    			add += "\n Note ID: %d \n %s \n By Author %s"%(note_id, i, self.author) 
	    		else: 
	    			print 'sorry! its not found' 
	      	print str(add) 

	def delete(self,note_id):
		self.note_name.pop(int(note_id))

	def edit (self,note_id,new_content): 
		self.note_name[int(note_id)]=new_content
'''
	the code below allows the NotesApplication
	to be used on a command line terminal
	as we make the first instance of an object
	using the raw_input to request it from the user
'''

author = raw_input('Enter the name of the Author: ') 
fortune = NotesApplication(author) 
def action():
	what_to_do = raw_input(
	"Press 1 to create a note \n"
	"Press 2 list to notes \n"
	"Press 3 to get a note \n"
	"Press 4 to search for a note \n"
	"press 5 to delete a note \n "
	"Press 6 to edit a note: \n"
	">>>"
)
	if what_to_do == '1':
		notecreated = raw_input("Please create a note: ")
		fortune.create(notecreated)
		print "Your note has been created"
		action()

	if what_to_do == '2':
		print "Here is your note:"
		fortune.list()
		action()

	if what_to_do == '3':
		get_with_note_id = raw_input('what is your note id: ')
		int(get_with_note_id)
		fortune.get(get_with_note_id)
		action()
		
	if what_to_do == '4':
		what_to_search = raw_input('what are you looking for: ')
		fortune.search(what_to_search)
		action()

	if what_to_do == '5':
		what_to_delete = raw_input(
			'what is the note ID of what you wish to delete: '
			)
		int(what_to_delete)
		fortune.delete(what_to_delete)
		action()

	if what_to_do == '6':
		note_id_to_edit = raw_input('what is the Note ID: ')
		new_stuff_added = raw_input(
			'what changes would you like to make on that note: '
			)
		fortune.edit(note_id_to_edit, new_stuff_added)
		action()



action() 