import factory

from ninjify.models import Buzzword


class BuzzwordFactory(factory.Factory):
    class meta:
        model = Buzzword

    label = factory.Faker('')