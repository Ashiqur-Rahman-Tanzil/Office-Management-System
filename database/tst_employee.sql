--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-07 11:48:05

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
-- TOC entry 221 (class 1259 OID 16768)
-- Name: tst_employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tst_employee (
    employee_id integer NOT NULL,
    user_password character varying(40) NOT NULL,
    user_name character varying(100) NOT NULL,
    dept_name character varying(200) NOT NULL
);


ALTER TABLE public.tst_employee OWNER TO postgres;

--
-- TOC entry 2911 (class 2606 OID 16772)
-- Name: tst_employee tst_employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tst_employee
    ADD CONSTRAINT tst_employee_pkey PRIMARY KEY (employee_id);


-- Completed on 2021-05-07 11:48:05

--
-- PostgreSQL database dump complete
--

