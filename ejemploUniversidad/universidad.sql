create database Universidad;
#crea la base de datos universidad

use Universidad;
#usa la base de datos universidad para las siguientes consultas

#sintaxis para crear tablas
create table Personas(
DNI int,#numeros enteros
PrimerNombre varchar(20),#texto dinámico que no excede 20 caracteres
SegundoNombre varchar(20),#se hace mas pequeño quitando el espacio sobrante
PrimerApellido varchar(20),
SegundoApellido varchar(20),
FechaDeNacimiento date,#fecha sin hora
primary key (DNI)#se define la llave primaria
);

create table Estado(
ID int, Estado varchar(20),
primary key(ID)
);

create table Estudiantes(
DNIPersonas int,
CreditosDelCicloLectivo int,
CreditosAprobados int,
PromedioGeneral decimal(2,1),#numeros de 2 digitos y un decimal
Estado int,
primary key(DNIPersonas),#la llave primaria es DNI
foreign key(DNIPersonas) references Personas(DNI),#DNIPersonas es un campo existente en DNI y no uno nuevo
foreign key(Estado) references Estado(ID)
);

create table Profesores(
DNIPersonas int,
HorasLaboradas int, 
Estado int,
primary key(DNIPersonas), 
foreign key(DNIPersonas) references Personas(DNI),
foreign key(Estado) references Estado(ID)
);

create table Telefonos(
ID int,
Telefonos varchar(15),
primary key(ID)
);

create table PersonasConTelefonos(
DNIPersonas int,
IDTelefonos int,
primary key(DNIPersonas, IDTelefonos),
foreign key(DNIPersonas) references Personas(DNI),
foreign key(IDTelefonos) references Telefonos(ID)
);

create table CorreosElectronicos(
ID int,
CorreosElectronicos varchar(20),
primary key(ID)
);

create table PersonasConCorreos(
DNIPersonas int,
IDCorreos int,
primary key(DNIPersonas, IDCorreos),
foreign key(DNIPersonas) references Personas(DNI),
foreign key(IDCorreos) references CorreosElectronicos(ID)
);

create table EstadoDelCurso(
ID int,
Estado varchar(20)
);

create table Cursos(
ID int,
Sigla varchar(20),
Nombre varchar(20),
Creditos int,
primary key(ID)
);

create table GruposMatriculados(
ID int,
DNIProfesor int,
IDCurso int,
Agno int,
Dia varchar(8),
HoraDeInicio varchar(5),
DuracionDeLecciones int,
primary key(ID, DNIProfesor, IDCurso),
foreign key(DNIProfesor) references Profesores(DNIPersonas)
);

create table Matriculas(
GrupoMatriculado int,
DNIEstudiante int,
Calificacion decimal(2,1),
EstadoDelCurso int,
primary key(GrupoMatriculado, DNIEstudiante),
foreign key(GrupoMatriculado) references GruposMatriculados(ID),
foreign key (DNIEstudiante) references Estudiantes(DNIPersonas)
);







