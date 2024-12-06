CREATE SEQUENCE IF NOT EXISTS lastactions_id_seq;

CREATE TABLE "public"."lastactions" (
    "id" int4 NOT NULL DEFAULT nextval('lastactions_id_seq'::regclass),
    "actionName" varchar NOT NULL,
    "userId" int4 NOT NULL,
    "date" varchar NOT NULL,
    PRIMARY KEY ("id")
);
