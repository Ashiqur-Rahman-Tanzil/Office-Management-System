--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-04 23:09:14

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
-- TOC entry 3033 (class 0 OID 16397)
-- Dependencies: 201
-- Data for Name: user_list; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.user_list (id, user_password, user_name, dept_id, dept_name) FROM stdin;
1	3330	Ashiqur Rahman	333	Admin
3	1110	Zahid	111	R&D
2	0001	Farhan	666	Web Development
4	2220	Naimur	222	Marketing
\.


--
-- TOC entry 3040 (class 0 OID 0)
-- Dependencies: 200
-- Name: user_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_list_id_seq', 4, true);


-- Completed on 2021-05-04 23:09:14

--
-- PostgreSQL database dump complete
--

