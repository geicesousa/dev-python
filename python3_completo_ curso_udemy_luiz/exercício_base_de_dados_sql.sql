-- insira 5 usuários 
INSERT INTO users (name, lastname, email, password, salary)
VALUES 
('Geice', 'Tokitako', 'geice@email.com', 'senha!@#', '1000')
('Sara', 'Vieira', 'sara@email.com', 'senha!@#', '1000')
('Akin', 'Tokitako Dandaro', 'akin@email.com', 'senha!@#', '1000')
('Luã', 'Dandaro', 'lua@email.com', 'senha!@#', '1000')
('Silva', 'Santos', 'silva@email.com', 'senha!@#', '1000');

-- insira 5 perfis para os novos usuários
INSERT INTO profiles 
(bio, description, user_id)
SELECT 
concat('Bio de ', name), 
concat('Descrição de ', name), 
id
FROM users
LIMIT 5;

INSERT INTO profiles
(bio, description, user_id)
VALUES
('Bio de Geice', 'Descrição de Geice', 01)
('Bio de Sara', 'Descrição de Sara', 02)
('Bio de Akin', 'Descrição de Akin', 03)
('Bio de Luã', 'Descrição de Luã', 04)
('Bio de Silva', 'Descrição de Silva', 05);


-- insira permissões para os usuários inseridos
-- primeiro a query para verificar os ids dos usuários inseridos
SELECT id FROM users
WHERE name IN ('Geice', 'Sara', 'Akin', 'Luã', 'Silva') 
AND lastname IN ('Tokitako', 'Vieira', 'Tokitako Dandaro', 'Dandaro', 'Santos');

INSERT INTO users_roles
(user_id, role_id)
VALUES
(01, 'GET')
(02, 'POST')
(03, 'PUT')
(04, 'DELETE')
(05, 'GET');

-- selecione os 5 últimos usuários por ordem decrescente
SELECT * FROM users
ORDER BY created_at DESC
LIMIT 5;

-- atualize o último usuário inserido
UPDATE users SET name = 'Silva', lastname = 'Sobrenome Atualizado'
WHERE id = 05;

-- remova uma permissão de algum usuário
DELETE FROM roles
WHERE id = 05;

-- remova um usuário que tem a permissão PUT
DELETE FROM users_roles
WHERE id = 03;

-- SELECT u.id as uid, u.name, r.name
DELETE u 
FROM users as u 
INNER JOIN users_roles as ur on u.id = ur.user_id
INNER JOIN roles r on ur.role_id = r.id
WHERE r.name = 'PUT' AND u.id = 03;

-- selecione usuários com perfis e permissões
SELECT u.id as u_id, u.name as u_name, r.name as r_name, p.bio as p_bio
FROM users
INNER JOIN users_roles as ur on u_id = r_name.user_id
INNER JOIN roles as r on ur.role_id = r.id
INNER JOIN profiles as p on p.user_id = u.id; -- usar LEFT JOIN deixaria como opcional ter perfil e permissao


-- selecione usuários com perfis e permissões ordenando por salário
SELECT u.id as u_id, u.name as u_name, r.name as r_name, p.bio as p_bio
FROM users
LEFT JOIN users_roles as ur on u_id = r_name.user_id
LEFT JOIN roles as r on ur.role_id = r.id
LEFT JOIN profiles as p on p.user_id = u.id; 
ORDER BY salary ASC