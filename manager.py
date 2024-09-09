from cryptography.fernet import Fernet #cytpography lib for generating a key

class PasswordManager:

	def __init__(self):
		self.key = None
		self.password_file = None
		self.password_dict = {}

	def create_key(self, path):
		self.key = Fernet.generate_key()
		with open(path,'wb') as f:
			f.write(self.key)
	def load_key(self, path):
		with open(path, 'rb') as f:
			self.key = f.read()
	
	def create_password_file(self, path, initial_values = None):
		self.password_file = path
		
		if initial_values is not None:
			for key, value in initial_values.items():
				self.add_password(key, value)

	def load_password_file(self, path):
		self.password_file = path

		with open(path, 'r') as f:
			for line in f:
				site, encrypted = line.split(" : ")
				self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

	def add_password(self, site, password):
		self.password_dict[site] = password
		if self.password_file is not None:
			with open(self.password_file, 'a+') as f:
				encrypted = Fernet(self.key).encrypt(password.encode())
				f.write(site + " : " + encrypted.decode() + "\n")

	def get_password(self, site):
		return self.password_dict[site]

def main():
	InitialPW = {
		"FaceBook" : "12345678",
		"YouTube" : "YouCreater",
		"instagram" : "InstaCreater",
		"Whatsapp" : "FingerPrint",
	}

	pm = PasswordManager()
	
	print("""What do you want to do?"
	(1) Create a New Key
	(2) Load an existing Key
	(3) Create new password file
	(4) Load existing password file
	(5) Add a new password
	(6) Get a password
	(7) Quit
	""")
	
	flag = False
	
	while not flag:
		choice = input("Enter your choice:  ")
 
		match choice:
			case "1":
				path = input("Enter path: ")
				pm.create_key(path)
			case "2":
				path = input("Enter path: ")
				pm.load_key(path)
			case "3":
				path = input("Enter path: ")
				pm.create_password_file(path, InitialPW)
			case "4":
				path = input("Enter path: ")
				pm.load_password_file(path)
			case "5":
				site = input("Enter the site: " ) 
				NewPW = input("Enter THe paswsword: " ) 
				pm.add_password(site, NewPW)
			case "6":
				site = input("What site do you want? : ")
				print(f"Password for {site} is {pm.get_password(site)}")
			case "7":
				flag = True
				print("Thanks for using our service :)")
			case default:
				print("Please Enter Valide Choices!!!")

if __name__ == "__main__":
	main()
 				
				


