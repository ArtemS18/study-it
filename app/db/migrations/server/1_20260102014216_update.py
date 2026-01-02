from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP CONSTRAINT IF EXISTS "fk_user_progress_986e4643";
        CREATE TABLE IF NOT EXISTS "status" (
    "id" SMALLSERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(32) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "user_module_progress" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "module_code" VARCHAR(128) NOT NULL,
    "status_id" SMALLINT NOT NULL DEFAULT 1 REFERENCES "status" ("id") ON DELETE SET DEFAULT,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_user_module_user_id_584066" UNIQUE ("user_id", "module_code")
);
CREATE INDEX IF NOT EXISTS "idx_user_module_module__c6dbac" ON "user_module_progress" ("module_code");
        CREATE TABLE IF NOT EXISTS "userpath" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "path" JSONB NOT NULL,
    "status_id" SMALLINT NOT NULL DEFAULT 1 REFERENCES "status" ("id") ON DELETE SET DEFAULT,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_user_path_gin" ON "userpath" USING GIN ("path");
        ALTER TABLE "user" ADD "have_active_path" BOOL NOT NULL DEFAULT False;
        ALTER TABLE "user" DROP COLUMN IF EXISTS "progress_id";
        DROP TABLE IF EXISTS "progress";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "progress_id" INT NOT NULL UNIQUE;
        ALTER TABLE "user" DROP COLUMN "have_active_path";
        DROP TABLE IF EXISTS "user_module_progress";
        DROP TABLE IF EXISTS "userpath";
        DROP TABLE IF EXISTS "status";
        ALTER TABLE "user" ADD CONSTRAINT "fk_user_progress_986e4643" FOREIGN KEY ("progress_id") REFERENCES "progress" ("id") ON DELETE CASCADE;"""


MODELS_STATE = (
    "eJztWltT2zoQ/isZP3Fm2k4xFJi+OSGcpk0IQ0J7pgzjUWwl0SDLriVDMgz/vZJ8v6UxJy"
    "lJqyfIalfWfpJ291v7SaPQf4D+OwP6yJprH1tPGgEO5P8URt60NOB5qVwIGJhgqQpSnQll"
    "PrAYl04BppCLbEgtH3kMuYRLSYCxELoWV0RklooCgn4E0GTuDLI5f8DH1u0dFyNiwwWk8U"
    "/v3pwiiO3cUpEtni3lJlt6UtYj7EIqiqdNTMvFgUNSZW/J5i5JtBFhQjqDBPqAQTE98wOx"
    "fLG6yM/Yo3ClqUq4xIyNDacgwCzj7poYWC4R+PHVUOngTDzlrX54fHp8dnRyfMZV5EoSye"
    "lz6F7qe2goEbgca89yHDAQakgYU9z4PlKxpBJ4nTnwq9HLmBQg5AsvQhgDtgrDWJCCmB6c"
    "DaHogIWJIZkxccD1Dx9WYPbVuO58Mq4PuNY/whuXH+bwjF9GQ3o4JoBNgRRXowGIkfp+An"
    "j4/v0aAHKtWgDlWB5A/kQGwzuYB/HzaHhZDWLGpADkDeEO3trIYm9aGFF2t5uwrkBReC0W"
    "7VD6A2fBOxgY/xVx7fSHbYmCS9nMl7PICdocYxEyp/eZyy8EE2DdPwLfNksjru7W6ZaHHN"
    "0pSgABM4mV8Fj4FyWREQMsoFXpJRpZmV5oqrMz6WXkAIz/oBxzpJ+eJOlF/FiVWUYDo9//"
    "dXqRfxuExVh/P+Pikb5GWDzSa6OiGGp0YVOgA35pTMe1AwxNz3dFEKC0jHw7mubiyzXEgN"
    "Wk8fBe3vC/AznjVTThbu7Bc3yIYml0Q3LZReDjATbfACZXfJo9Q2KbgV1AUhXWpXxlUA9i"
    "jZ0J6X9QNN8aY7B8KJw1QUWpds5HGHJgTbmWsyyAaUem7+J/1rhiEXK/M95zF+whwcs0xt"
    "QhOe4NuqOxMbjKVXHnxrgrRnQpXRakByeF3JBM0vrWG39qiZ+t78PLbrHYS/TG3zWxJhAw"
    "1yTuownszBGLpTEw+Qjp2S/c17yl2tfX3NdS4uPFwAOyw0C7bhWWtXlRJfYKG5gnqPrZOg"
    "RVP6snqGIsT1ChAxBuAmNisJlqduuJY/sQTpFPWVNOkDPaT2KwFTAxaI5l1kZBmUA5B3TO"
    "E5gHKH10/YrCsB7RClMFbD5mmrzwR3zSClzbroshICviZ864gOyEW28L2qZMZP3OXns47O"
    "dqh3ZvXID0ZtDucqwl0lwJsZCdRLV59tw+QJMzJ8T/eBEtbQBwlbmC+IUdmLD5onoumdJT"
    "9Vu21G8pHJGa7kv5IK3uxRT7h5vvzdwmPZ/oUZZrQ+1OtWxUy0ZRe9Wy+Tv3tZQ3s7GxtK"
    "/1TKRgti0Wsn9dh/Dlsdn8HW7O8NeZZFNFyeH/ziQvf5VbeKPYKONmLH4fWK+feUtsIY9h"
    "GcAL14doRr7ApcSxx1cEiFV5afOv0nYPv7oKmIt98JiUcNmjwd2zIYYh3+oYo45x3tUq7u"
    "sGcEu/LNmxa7oubLkAlANu1B23zrsXxk2fH8HX+aIn4WY19CPmbatJR9x32OpL4Cct9UnS"
    "Uk0owIUnaA6fPnE2ZRoLU55ZoWzOkKSo8en6tye/zIILvmDxO9wAxVgUY1GVrWIsf8G+Vn"
    "b6yhta/+FuTbNZfbWbfLWr+IviL4q/KP6i+MuG+cvzTx7btpY="
)
