from django.core.management import BaseCommand

from ninjify.models import Buzzword, NinjaName, Grammar


class Command(BaseCommand):
    help = 'Populate data for Nijify application'

    def handle(self, *args, **options):

        n1 = NinjaName.objects.create(label="Blue", type=Grammar.ADJECTIVE)
        n2 = NinjaName.objects.create(label="Eyed", type=Grammar.ADJECTIVE)
        n3 = NinjaName.objects.create(label="Executioner", type=Grammar.NOUN)
        n4 = NinjaName.objects.create(label="Shadow", type=Grammar.NOUN)
        n5 = NinjaName.objects.create(label="Drop", type=Grammar.ADJECTIVE)

        Buzzword.objects.bulk_create([
            Buzzword(label="sass", ninja_name=n1),
            Buzzword(label="css", ninja_name=n1),
            Buzzword(label="html", ninja_name=n1),
            Buzzword(label="xml", ninja_name=n1),
            Buzzword(label='c', ninja_name=n2),
            Buzzword(label='Fortran', ninja_name=n2),
            Buzzword(label='Cobol', ninja_name=n2),
            Buzzword(label='c++', ninja_name=n2),
            Buzzword(label='Frontend', ninja_name=n3),
            Buzzword(label='Backend', ninja_name=n3),
            Buzzword(label='Fullstack', ninja_name=n3),
            Buzzword(label='React', ninja_name=n4),
            Buzzword(label='Vuejs', ninja_name=n4),
            Buzzword(label='Angular', ninja_name=n4),
            Buzzword(label='font', ninja_name=n5)
        ])

        for ninja_name in NinjaName.objects.all():
            self.stdout.write(f"Ninja name : {ninja_name.label} has been " + self.style.SUCCESS("GENERATED"))

        for buzzword in Buzzword.objects.all():
            self.stdout.write(f"Buzzword : {buzzword.label} related to {buzzword.ninja_name.label} has been " + self.style.SUCCESS("GENERATED"))

        self.stdout.write(self.style.SUCCESS('Successfully generated all data!'))
