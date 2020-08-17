import pandas as pd
from .models import Voca

levels = ["N3", "N4", "N5"]


def create_default_voca(sender, **kwargs):
    for level in levels:

        file_name = "quiz/csv/" + level + "_Voca.csv"

        df = pd.read_csv(file_name, encoding="shift-jis")

        for i in range(len(df)):
            example = df.iat[i, 4]
            example = example.split("\n") if example else [None, None]

            Voca.objects.get_or_create(
                kanji=df.iat[i, 0],
                kana=df.iat[i, 1],
                pos=df.iat[i, 2],
                meaning=df.iat[i, 3],
                en_example=example[0],
                ja_example=example[1],
                level=level,
            )
