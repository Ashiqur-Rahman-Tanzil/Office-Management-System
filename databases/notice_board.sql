--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-04 23:10:19

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
-- TOC entry 3031 (class 0 OID 16403)
-- Dependencies: 202
-- Data for Name: notice_board; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notice_board (notice_id, notice_body, pinned, priority_level, post_date, dept_id) FROM stdin;
111005	R&D members are requested to show their project progress on this sunday.	0	1	2021-05-02	111
222004	New product launch on this tuesday. Get ready for the big day!!	1	3	2021-05-02	222
333003	All members from admin panel are requested to update the system on this friday.	0	5	2021-05-02	333
666002	Front end for our client MR. Zafar should be finished by this monday.	0	4	2021-05-02	666
777001	We have a general body meeting on the upcoming sunday sharp at 10:00 AM. Location: Meeting room. Do not be late. \nDGM sir will be there on time.	1	5	2021-05-02	777
333006	be ready for the project demonstration	0	5	2021-05-03	333
333007	Admin panel. Good job!!!	0	1	2021-05-03	333
\.


-- Completed on 2021-05-04 23:10:19

--
-- PostgreSQL database dump complete
--

