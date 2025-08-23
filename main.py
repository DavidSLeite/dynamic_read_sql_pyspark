import s3
from utils import generate_tbl_tmp_view


# argumentos recebidos pelo glue job para fazer no minimo a leitura do script SQL
args = {
    "JOB_NAME": "glue_job_teste", 
    "SQL_PATH": "db_pedido_venda.tb_cad_fornecedor.sql", 
    "list_tables_predicates": "[{'database': 'db_pedido', 'table': 'tb_cad_prod', 'predicate': 'ano=\"2025\" AND mes=\"08\" AND dia=\"20\"'},{'database': 'db_prod_b', 'table': 'tb_cad_prod_b', 'predicate': 'ano=\"2025\" AND mes=\"08\" AND dia=\"20\"'},{'database': 'db_prod_b', 'table': 'tb_cad_prod_c'}]"
}

# leitura do script SQL no S3
sql_query = s3.get_object(args["SQL_PATH"])

# gera as views temporarias com os predicados passados por argumento
generate_tbl_tmp_view(args)


print(f"""
spark.sql executando a query:
      
{sql_query}
""")