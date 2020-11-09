create table Proyectos(
id serial primary key,
	nombre varchar(200) not null,
	descripcion varchar(1000) not null
);

create table UserStories (
id INT primary key,
	codigo varchar(45) not null,
	nombre varchar(500) not null,
	card TEXT,
	conversation TEXT,
	confirmation TEXT,
	foreign key(idProyecto) references Proyectos (id) 
);