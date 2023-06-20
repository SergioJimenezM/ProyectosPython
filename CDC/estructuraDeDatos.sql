create table persona(
    nombre text primary key not null,
    telefono text not null
);

create table dispositivo(
    telefono text not null,
    descripcion text not null,
    fechaDeEntrega date not null,
    vencimientoDeGarantia date not null, 
    foreign key (telefono) references persona(telefono)
);