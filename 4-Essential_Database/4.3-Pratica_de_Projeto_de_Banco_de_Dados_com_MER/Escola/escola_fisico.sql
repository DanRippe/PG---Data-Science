/* escola_logico: */

CREATE TABLE ALUNO (
    ra number(5) PRIMARY KEY,
    nome_aluno varchar2(50),
    data_nasc date,
    genero varchar2(10)
);

CREATE TABLE MATRICULA (
    cod_matr number(5) PRIMARY KEY,
    data_matr date,
    ra number(5),
    cod_curso number(5)
);

CREATE TABLE CURSO (
    cod_curso number(5) PRIMARY KEY,
    carga_horaria_curso number(4),
    nome_curso varchar2(50)
);

CREATE TABLE DISCIPLINA (
    cod_disciplina number(5) PRIMARY KEY,
    carga_horaria_disciplina number(3),
    nome_disciplina varchar2(50),
    cod_curso number(5)
);

CREATE TABLE AULA (
    rp number(5),
    cod_disciplina number(5),
    data_aula date,
    PRIMARY KEY (rp, cod_disciplina)
);

CREATE TABLE PROFESSOR (
    rp number(5) PRIMARY KEY,
    nome_professor varchar2(50),
    data_nasc date,
    genero varchar2(10),
    titulacao varchar2(50)
);
 
ALTER TABLE MATRICULA ADD CONSTRAINT FK_MATRICULA_2
    FOREIGN KEY (ra)
    REFERENCES ALUNO (ra);
 
ALTER TABLE MATRICULA ADD CONSTRAINT FK_MATRICULA_3
    FOREIGN KEY (cod_curso)
    REFERENCES CURSO (cod_curso);
 
ALTER TABLE DISCIPLINA ADD CONSTRAINT FK_DISCIPLINA_2
    FOREIGN KEY (cod_curso)
    REFERENCES CURSO (cod_curso);
 
ALTER TABLE AULA ADD CONSTRAINT FK_AULA_1
    FOREIGN KEY (data_aula)
    REFERENCES PROFESSOR (rp);
 
ALTER TABLE AULA ADD CONSTRAINT FK_AULA_2
    FOREIGN KEY (rp)
    REFERENCES PROFESSOR (rp);
 
ALTER TABLE AULA ADD CONSTRAINT FK_AULA_4
    FOREIGN KEY (cod_disciplina)
    REFERENCES DISCIPLINA (cod_disciplina);