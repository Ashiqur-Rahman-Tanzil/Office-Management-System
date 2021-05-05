--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-04 23:10:43

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

--
-- TOC entry 3031 (class 0 OID 24603)
-- Dependencies: 219
-- Data for Name: meetings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.meetings (meeting_id, meeting_body) FROM stdin;
1	meeting on sunday
2	meeting on monday
3	meeting on friday
\.


-- Completed on 2021-05-04 23:10:43

--
-- PostgreSQL database dump complete
--

