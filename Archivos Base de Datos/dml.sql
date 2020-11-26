insert into Proyectos(nombre,descripcion) values
('Proyecto Scrum','Requisitos para la entrega del tercer corte');

insert into UserStories(codigo,nombre,card,conversation,confirmation,idproyecto) values
(1,'Consultar la lista de proyectos ','Prueba card ','Prueba conversation ','Prueba confirmation',1),
(2,'Consultar un proyecto ','Prueba card ','Prueba conversation ','Prueba confirmation',1),
(3,'Crear User Stories','Prueba card ','Prueba conversation ','Prueba confirmation',1),
(4,'Consultar un User Storie ','Prueba card ','Prueba conversation ','Prueba confirmation',1);

select * from UserStories