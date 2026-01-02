from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" ADD "current_module_code" VARCHAR(128) NOT NULL;
        CREATE INDEX IF NOT EXISTS "idx_userpath_current_3d9326" ON "userpath" ("current_module_code");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "idx_userpath_current_3d9326";
        ALTER TABLE "userpath" DROP COLUMN "current_module_code";"""


MODELS_STATE = (
    "eJztWm1P4zgQ/itVPnHS3moJLKD9lpZy21tKES13p0UochO3tXCcbOJAK8R/X9t5dV66Ta"
    "+FdvGnNuMZx35sz8wz8bMWQP8R+h8N6CNrpn1pPWsEOJD9KbR8aGnA8zI5F1AwxkIVZDrj"
    "gPrAokw6ATiATGTDwPKRR5FLmJSEGHOhazFFRKaZKCToRwhN6k4hnbEXfGnd3TMxIjacwy"
    "B59B7MCYLYloaKbP5uITfpwhOyHqEXQpG/bWxaLg4dkil7CzpzSaqNCOXSKSTQBxTy7qkf"
    "8uHz0cXzTGYUjTRTiYaYs7HhBISY5qa7IgaWSzh+bDSBmOCUv+VP/fD49Pjs6OT4jKmIka"
    "SS05doetncI0OBwNVIexHtgIJIQ8CY4cbWMeBDKoHXmQG/Gr2cSQFCNvAihAlgyzBMBBmI"
    "2cbZEIoOmJsYkinlG1z//HkJZv8YN52vxs0B0/qDz8Zlmzna41dxkx61cWAzIPnRaABirL"
    "6fAB5++rQCgEyrFkDRJgPI3khhdAZlEP8eDq6qQcyZFIC8JWyCdzay6IcWRgG9301Yl6DI"
    "Z80H7QTBD5wH76Bv/FfEtXM5aAsU3IBOfdGL6KDNMOYuc/KQO/xcMAbWwxPwbbPU4upunW"
    "65ydGdogQQMBVY8Rnz+cVBZEgBDYOq8BK3LA0vQaazM+Fl6ACMf6MYc6SfnqThhT8siyzD"
    "vnF5+evwIn4buMVEfz/94pG+gls80mu9Im9qdGAzoEN2aEzHtUMMTc93uRMIgjLy7bibi2"
    "83EANaE8ajc3nLfvuix+u4w91cg5dkEyXS+IRI0YXj4wE62wAm16ybPUNim46dQ1Ll1oV8"
    "qVMPE42dcem/kTffGmOwfMgna4KKVO2ctVDkwJp0TbIsgGnHph+TPyscsRi51/T3bAr2gO"
    "BF5mPqkBz1+t3hyOhfS1ncuTHq8hZdSBcF6cFJITaknbT+7Y2+tvhj6/vgqltM9lK90XeN"
    "jwmE1DWJ+2QCO7fFEmkCjOwhPXvNdZUt1bq+5bqWAh9LBh6RHTnaVbOwvM1amdgbLKBMUP"
    "WzVQiqflZPUHmbTFChAxBuAmNqsJlsduuBY/sQTpAf0KacQDLaT2KwFTAxaI5l3kZBmUI5"
    "A8GMBTAPBMGT61ckhvWIVpgqYGWfabLEH7FOK3Btuy6GgCzxn5JxAdkxs94WtE2ZyOqVvf"
    "ZgcCnlDu3eqADpbb/dZVgLpJkSohE7iXPz/L59hCZjToj9eDEtbQBwlbmCeM0KTFR8UTWX"
    "XOqp6i1bqrcUtkhN9aW8kZbXYor1w83XZu7Smk/8Ksu1oXavSjaqZKOovSrZvM91LcXNvG"
    "8srWs9EymYbYuF7F/VIfp4bDb/hisZ/jqSbCopOfzfkWT9T7mFL4qNIm7O4vXAevvIW2IL"
    "MoZlAC9cH6Ip+QYXAsceGxEgVuWhlT+l7R5+dRkwE/vgKU3h8luDTc+GGEZ8q2MMO8Z5V6"
    "s4rxvALbtZsmPHdFXYJAckATfsjlrn3Qvj9pJtwbe50ZNysxr6kfC25aQjqTts9SPws5bN"
    "SdBSjSvAucdpDus+nWzGNOam2LNc2ZwiQVGT3fVXT9zMgnM2YP4cLYBiLIqxqMxWMZZ3sK"
    "6Vlb7ygtZf3K0pNqtbu+mtXelmdOj7kFBzTV5YY674oeKHih8qfvgarlLxw3fDD19+Aqhz"
    "KNk="
)
