--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-07 11:47:40

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
-- TOC entry 223 (class 1259 OID 16775)
-- Name: tst_employeeofthemonth; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tst_employeeofthemonth (
    id bigint NOT NULL,
    employee_id integer NOT NULL,
    attendance_point integer NOT NULL,
    project_point integer NOT NULL,
    attitude_point integer NOT NULL,
    work_quality_point integer NOT NULL,
    leadership_point integer NOT NULL,
    cooperation_point integer NOT NULL,
    total_point integer NOT NULL,
    date date NOT NULL
);


ALTER TABLE public.tst_employeeofthemonth OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16773)
-- Name: tst_employeeofthemonth_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tst_employeeofthemonth_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tst_employeeofthemonth_id_seq OWNER TO postgres;

--
-- TOC entry 3048 (class 0 OID 0)
-- Dependencies: 222
-- Name: tst_employeeofthemonth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tst_employeeofthemonth_id_seq OWNED BY public.tst_employeeofthemonth.id;


--
-- TOC entry 2910 (class 2604 OID 16778)
-- Name: tst_employeeofthemonth id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tst_employeeofthemonth ALTER COLUMN id SET DEFAULT nextval('public.tst_employeeofthemonth_id_seq'::regclass);


--
-- TOC entry 2912 (class 2606 OID 16780)
-- Name: tst_employeeofthemonth tst_employeeofthemonth_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tst_employeeofthemonth
    ADD CONSTRAINT tst_employeeofthemonth_pkey PRIMARY KEY (id);


-- Completed on 2021-05-07 11:47:40

--
-- PostgreSQL database dump complete
--

