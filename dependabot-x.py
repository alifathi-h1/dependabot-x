import time, argparse, sys, os, pyfiglet
from colorama import Fore, Style
from github import Github


class DependabotX:

	def __init__(self,org, personal_account):

		self.org = org
		self.personal_account = personal_account
		self.ACCESS_TOKEN = os.environ.get('GITHUB_API_KEY')	
		if self.ACCESS_TOKEN is None:
			print(Fore.RED)
			print('\n [--] Please Configure GITHUB_API_KEY as Env Variable first. \n')
			sys.exit()

	def login(self):

            try:
                self.g = Github(self.ACCESS_TOKEN)
                self.user = self.g.get_user()
                print("\n[++] Logged in successfully as " + str(self.user.name) + "....\n")
                return self.g, self.user
            except Exception as E:
                return False


	def enable_alerts(self, repos):

		try:
			print("\n[**] Enabling Dependabot alerts for "+ str(repos.totalCount) +" repo/s: \n")
			for repo in repos:
			        
				repo_name = repo.name
				try: 
					enable_alerts = repo.enable_vulnerability_alert()
					print("[++] "+ repo_name + ": Done\n")
					time.sleep(.5)
				except Exception as E:
					print("[--] There was an error when updating "+ repo_name + ": "+ str(E))
					pass
		except Exception as E:
			print(E)



	def main(self):


		if self.login() != False:

			if self.org is not None:

				try:
					org_name = self.g.get_organization(self.org)
					repos = org_name.get_repos()
					enable_alerts = self.enable_alerts(repos)
				except Exception as E:
					print("[**] We clould not find the GitHub Org...\n\n")
					pass

			elif self.personal_account:

				try:
					repos=self.user.get_repos(visibility='all')
					enable_alerts=self.enable_alerts(repos)
				except Exception as E:
					print("[**] There was an error: "+ str(E)+" \n\n")
			else:
				print("[**] --org/-o or --personal-account/-o should be present.\n\n")



print(Fore.GREEN)
banner = pyfiglet.figlet_format("Dependabot - X T o o l", width=130,  justify='center')

print('\n \n'+banner)
print('Developed By @Alifathi-h1 \n\n '.center(90))


parser = argparse.ArgumentParser(description='Dependabot-X is a tool written in Python3 that allows GitHub Organization/User to automate enabling Dependabot alerts feature for all repositories. \n\n')
parser.add_argument('-o', '--org', help='Key in your organization name')
parser.add_argument('-a', '--personal-account', help='Enable it for Your personal account', action=argparse.BooleanOptionalAction)

args = parser.parse_args()

org= args.org
personal_account = args.personal_account


dx = DependabotX(org, personal_account)
dx.main()
