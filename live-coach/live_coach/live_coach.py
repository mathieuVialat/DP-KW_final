import  argparse
from utils import entrainement
from utils import classification

#poetry run live_coach.py live -n 100
#poetry run live_coach.py load -i chemin -n 100 --output chemin


# Initialisation du Parser du script : 
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')
load= subparser.add_parser('load')
live = subparser.add_parser('live')

# Ajout des arguments : 
live.add_argument('-n', type=int, required=True)
load.add_argument('-i', type=str, required=True)
load.add_argument('-n', type=int, required=True)
load.add_argument('--output', type=str, required=False)
args = parser.parse_args()

# Création des varaibles : 
if args.command == 'live':
    input_path = 'webcam'
    input_number = args.n
    output = ''
elif args.command == 'load':
  input_path = args.i
  input_number = args.n
  output = args.output 

entrainement(input_number)

classification(input_path, output)

