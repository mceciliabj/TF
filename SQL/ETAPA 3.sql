/*
INTEGRANTES
Ariel Fernandes 1700760
Thiago Roldão 1520133
Gabriel Chaves 1700727
Vitor Freitas 1700741
Maria Cecilia 1700785
*/

USE ImpactaTOP
GO

/*EX 1*/
SELECT
	NOME, EMAIL, RA
FROM
	dbo.Aluno
WHERE
	SIGLA_CURSO = 'SI';

/*EX 2*/
SELECT
	NOME_DISCIPLINA
FROM
	dbo.DisciplinaOfertada
WHERE
	ANO = '2018' and SEMESTRE = '1';

/*EX 4*/
SELECT Disciplina.NOME AS 'Nome da Disciplina' ,count(Aluno.SIGLA_CURSO) AS 'Total de Alunos'

FROM Aluno INNER JOIN Disciplina ON Aluno.SIGLA_CURSO = Disciplina.NOME INNER JOIN GradeCurricular ON Aluno.SIGLA_CURSO = GradeCurricular.SIGLA_CURSO

WHERE GradeCurricular.ANO = 2017 AND GradeCurricular.SEMESTRE = 2

GROUP BY Disciplina.NOME

ORDER BY Disciplina.NOME DESC

/*EX 6*/
SELECT	Questao.NUMERO, Questao.DESCRICAO, ALUNO.NOME AS 'NOME DO ALUNO', ALUNO.RA, Resposta.DATA_DE_ENVIO

FROM
		Questao INNER JOIN Resposta ON Questao.NUMERO = Resposta.NUMERO_QUESTAO INNER JOIN Aluno ON Resposta.RA_ALUNO = Aluno.RA

/*EX 8*/
SELECT 
	Curso.NOME AS 'Curso', count(Curso.SIGLA) AS 'Total de Alunos'
FROM
	Aluno
INNER JOIN Curso ON Aluno.SIGLA_CURSO = Curso.SIGLA

GROUP BY Curso.NOME

ORDER BY 'Total de Alunos' DESC