drop table if  exists UserStories;
drop table if  exists Proyectos;

create table Proyectos(
	id serial primary key,
	nombre varchar(200) not null,
	descripcion varchar(1000) not null
);

create table UserStories (
id serial primary key,
	codigo varchar(45) not null unique,
	nombre varchar(500) not null,
	card TEXT,
	conversation TEXT,
	confirmation TEXT,
	idproyecto int references Proyectos (id) not null
);



