-- concatenar {NOME_DATABASE}_{NOME_TABELA}

SELECT 
    a.id,
    a.nome,
    a.idade,
    a.salario,
    b.nome as nome_do_b,
    b.idade as idade_b,
    c.nome as nome_do_c,
    c.idade as idade_c
FROM db_pedido_tb_cad_prod as a
INNER JOIN db_prod_b_tb_cad_prod_b as b
INNER JOIN db_prod_b_tb_cad_prod_c as c
ON a.id = b.id
AND a.id = c.id