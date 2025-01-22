--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2 (Debian 17.2-1.pgdg120+1)
-- Dumped by pg_dump version 17.2 (Debian 17.2-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: wallet_requests; Type: TABLE; Schema: public; Owner: postgres
--
CREATE DATABASE test;

CREATE TABLE public.wallet_requests (
    id integer NOT NULL,
    balance numeric NOT NULL,
    bandwidth integer NOT NULL,
    energy integer NOT NULL,
    address character varying NOT NULL
);


ALTER TABLE public.wallet_requests OWNER TO postgres;

--
-- Name: wallet_requests_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.wallet_requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.wallet_requests_id_seq OWNER TO postgres;

--
-- Name: wallet_requests_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.wallet_requests_id_seq OWNED BY public.wallet_requests.id;


--
-- Name: wallet_requests id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wallet_requests ALTER COLUMN id SET DEFAULT nextval('public.wallet_requests_id_seq'::regclass);


--
-- Data for Name: wallet_requests; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.wallet_requests (id, balance, bandwidth, energy, address) FROM stdin;
\.


--
-- Name: wallet_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.wallet_requests_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

