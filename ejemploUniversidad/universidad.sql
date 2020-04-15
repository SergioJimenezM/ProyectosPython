create database Universidad;
#crea la base de datos universidad

use Universidad;
#usa la base de datos universidad para las siguientes consultas

#sintaxis para crear tablas
CREATE TABLE Personas (
 DNI int(11) NOT NULL,
 PrimerNombre varchar(20) NOT NULL,
 SegundoNombre varchar(20),
 PrimerApellido varchar(20) NOT NULL,
 SegundoApellido varchar(20),
 FechaDeNacimiento date NOT NULL,
 PRIMARY KEY (DNI)
);

CREATE TABLE Estado (
 ID int(11) NOT NULL,
 Estado varchar(20) NOT NULL,
 PRIMARY KEY (ID)
) ;

CREATE TABLE Estudiantes (
 DNIPersona int(11) NOT NULL,
 CreditosDelCicloLectivo int(11) NOT NULL,
 CreditosAprobados int(11) NOT NULL,
 PromedioGeneral decimal(2,1) NOT NULL,
 Estado int(11) NOT NULL,
 PRIMARY KEY (DNIPersona),
 KEY Estado (Estado),
 CONSTRAINT EstudiantesConPersonas FOREIGN KEY (DNIPersona) REFERENCES Personas (DNI) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT EstudiantesConEstado FOREIGN KEY (Estado) REFERENCES Estado (ID)
);

CREATE TABLE Profesores (
 DNIPersonas int(11) NOT NULL,
 HorasLaboradas int(11) NOT NULL,
 Estado int(11) NOT NULL,
 PRIMARY KEY (DNIPersonas),
 KEY Estado (Estado),
 CONSTRAINT ProfesoresConPersonas FOREIGN KEY (DNIPersonas) REFERENCES Personas (DNI) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT ProfesoresConEstado FOREIGN KEY (Estado) REFERENCES Estado (ID)
);

CREATE TABLE Telefonos (
 ID int(11) NOT NULL,
 Telefonos varchar(15) NOT NULL,
 PRIMARY KEY (ID)
);

CREATE TABLE PersonasConTelefonos (
 DNIPersonas int(11) NOT NULL,
 IDTelefonos int(11) NOT NULL,
 PRIMARY KEY (DNIPersonas,IDTelefonos),
 KEY IDTelefonos (IDTelefonos),
 CONSTRAINT TablaConDNI FOREIGN KEY (DNIPersonas) REFERENCES Personas (DNI) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT TablaConTelefonos FOREIGN KEY (IDTelefonos) REFERENCES Telefonos (ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE CorreosElectronicos (
 ID int(11) NOT NULL,
 CorreosElectronicos varchar(20) NOT NULL,
 PRIMARY KEY (ID)
);

CREATE TABLE PersonasConCorreos (
 DNIPersonas int(11) NOT NULL,
 IDCorreos int(11) NOT NULL,
 PRIMARY KEY (DNIPersonas,IDCorreos),
 KEY IDCorreos (IDCorreos),
 CONSTRAINT TablaConDNI FOREIGN KEY (DNIPersonas) REFERENCES Personas (DNI) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT TablaConCorreos FOREIGN KEY (IDCorreos) REFERENCES CorreosElectronicos (ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE EstadoDelCurso (
 ID int(11) NOT NULL,
 Estado varchar(20) NOT NULL,
 PRIMARY KEY (ID)
);

CREATE TABLE Cursos (
 ID int(11) NOT NULL,
 Sigla varchar(20) NOT NULL,
 Nombre varchar(20) NOT NULL,
 Creditos int(11) NOT NULL,
 PRIMARY KEY (ID),
 UNIQUE KEY Sigla (Sigla)
);

CREATE TABLE GruposMatriculados (
 ID int(11) NOT NULL,
 DNIProfesor int(11) NOT NULL,
 IDCurso int(11) NOT NULL,
 Agno year(4) NOT NULL,
 Dia varchar(8) NOT NULL,
 HoraDeInicio varchar(5) NOT NULL,
 DuracionDeLecciones int(11) NOT NULL,
 PRIMARY KEY (ID,DNIProfesor,IDCurso),
 KEY DNIProfesor (DNIProfesor),
 KEY IDCurso (IDCurso),
 CONSTRAINT GruposMatriculadosConMatriculas FOREIGN KEY (ID) REFERENCES Matriculas (GrupoMatriculado) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT GruposMatriculadosConProfesores FOREIGN KEY (DNIProfesor) REFERENCES Profesores (DNIPersonas) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT GruposMatriculadosConCursos FOREIGN KEY (IDCurso) REFERENCES Cursos (ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Matriculas (
 GrupoMatriculado int(11) NOT NULL,
 DNIEstudiante int(11) NOT NULL,
 Calificacion decimal(2,1) NOT NULL,
 EstadoDelCurso int(11) NOT NULL,
 PRIMARY KEY (GrupoMatriculado,DNIEstudiante),
 KEY DNIEstudiante (DNIEstudiante),
 KEY EstadoDelCurso (EstadoDelCurso),
 CONSTRAINT MatriculasConEstudiantes FOREIGN KEY (DNIEstudiante) REFERENCES Estudiantes (DNIPersona) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT MatriculasConEstadoDelCurso FOREIGN KEY (EstadoDelCurso) REFERENCES EstadoDelCurso (ID)
);







