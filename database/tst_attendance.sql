--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-07 11:46:30

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
-- TOC entry 220 (class 1259 OID 16759)
-- Name: tst_attendance; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tst_attendance (
    id bigint NOT NULL,
    employee_id integer NOT NULL,
    leave_application text NOT NULL,
    open_date date NOT NULL,
    present integer NOT NULL
);


ALTER TABLE public.tst_attendance OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16757)
-- Name: tst_attendance_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tst_attendance_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tst_attendance_id_seq OWNER TO postgres;

--
-- TOC entry 3048 (class 0 OID 0)
-- Dependencies: 219
-- Name: tst_attendance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tst_attendance_id_seq OWNED BY public.tst_attendance.id;


--
-- TOC entry 2910 (class 2604 OID 16762)
-- Name: tst_attendance id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tst_attendance ALTER COLUMN id SET DEFAULT nextval('public.tst_attendance_id_seq'::regclass);


--
-- TOC entry 2912 (class 2606 OID 16767)
-- Name: tst_attendance tst_attendance_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tst_attendance
    ADD CONSTRAINT tst_attendance_pkey PRIMARY KEY (id);


-- Completed on 2021-05-07 11:46:31

--
-- PostgreSQL database dump complete
--

