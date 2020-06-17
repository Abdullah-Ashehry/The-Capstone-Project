--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Actor; Type: TABLE; Schema: public; Owner: 3bady
--

CREATE TABLE public."Actor" (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying(120) NOT NULL
);


ALTER TABLE public."Actor" OWNER TO "3bady";

--
-- Name: Actor_id_seq; Type: SEQUENCE; Schema: public; Owner: 3bady
--

CREATE SEQUENCE public."Actor_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actor_id_seq" OWNER TO "3bady";

--
-- Name: Actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: 3bady
--

ALTER SEQUENCE public."Actor_id_seq" OWNED BY public."Actor".id;


--
-- Name: Movie; Type: TABLE; Schema: public; Owner: 3bady
--

CREATE TABLE public."Movie" (
    id integer NOT NULL,
    title character varying NOT NULL,
    city character varying(120) NOT NULL,
    release_date character varying(120) NOT NULL
);


ALTER TABLE public."Movie" OWNER TO "3bady";

--
-- Name: Movie_id_seq; Type: SEQUENCE; Schema: public; Owner: 3bady
--

CREATE SEQUENCE public."Movie_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_id_seq" OWNER TO "3bady";

--
-- Name: Movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: 3bady
--

ALTER SEQUENCE public."Movie_id_seq" OWNED BY public."Movie".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: 3bady
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO "3bady";

--
-- Name: Actor id; Type: DEFAULT; Schema: public; Owner: 3bady
--

ALTER TABLE ONLY public."Actor" ALTER COLUMN id SET DEFAULT nextval('public."Actor_id_seq"'::regclass);


--
-- Name: Movie id; Type: DEFAULT; Schema: public; Owner: 3bady
--

ALTER TABLE ONLY public."Movie" ALTER COLUMN id SET DEFAULT nextval('public."Movie_id_seq"'::regclass);


--
-- Data for Name: Actor; Type: TABLE DATA; Schema: public; Owner: 3bady
--

COPY public."Actor" (id, name, age, gender) FROM stdin;
1	will smith	51	male
4	wille smithing	51	male
6	not will smith	21	female
7	heroku smithing	51	male
\.


--
-- Data for Name: Movie; Type: TABLE DATA; Schema: public; Owner: 3bady
--

COPY public."Movie" (id, title, city, release_date) FROM stdin;
1	pursuif of happiness	LA	12-12-1212
4	pursuiting of happiness	LA	12-12-1212
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: 3bady
--

COPY public.alembic_version (version_num) FROM stdin;
f097e7448cdf
\.


--
-- Name: Actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: 3bady
--

SELECT pg_catalog.setval('public."Actor_id_seq"', 7, true);


--
-- Name: Movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: 3bady
--

SELECT pg_catalog.setval('public."Movie_id_seq"', 4, true);


--
-- Name: Actor Actor_name_key; Type: CONSTRAINT; Schema: public; Owner: 3bady
--

ALTER TABLE ONLY public."Actor"
    ADD CONSTRAINT "Actor_name_key" UNIQUE (name);


--
-- Name: Actor Actor_pkey; Type: CONSTRAINT; Schema: public; Owner: 3bady
--

ALTER TABLE ONLY public."Actor"
    ADD CONSTRAINT "Actor_pkey" PRIMARY KEY (id);


--
-- Name: Movie Movie_pkey; Type: CONSTRAINT; Schema: public; Owner: 3bady
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_pkey" PRIMARY KEY (id);


--
-- Name: Movie Movie_title_key; Type: CONSTRAINT; Schema: public; Owner: 3bady
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_title_key" UNIQUE (title);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: 3bady
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- PostgreSQL database dump complete
--

