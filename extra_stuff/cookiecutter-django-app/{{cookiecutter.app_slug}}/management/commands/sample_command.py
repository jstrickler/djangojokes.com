from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "A sample manage.py command"

    # uses argparse
    def add_arguments(self, parser):
        parser.add_argument("-spam", action="store_true", help="sample option")
        parser.add_argument("ham", help="argument to command")

    def handle(self, *args, **options):
        print(f"{args = }")
        print(f"{options = }")
        
        print("sample management command")