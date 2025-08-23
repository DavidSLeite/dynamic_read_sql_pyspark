import ast


def generate_tbl_tmp_view(args):
    list_tables_predicates = ast.literal_eval(args["list_tables_predicates"])

    for i in list_tables_predicates:
        db = i.get('database', None)
        tbl = i.get('table', None)
        predicate = i.get('predicate', None)

        if predicate:
            print(f"Lendo {db}.{tbl} com filtro de partição: {predicate}")
            # dyf = glueContext.create_dynamic_frame.from_catalog(
            #     database=db,
            #     table_name=tbl,
            #     push_down_predicate=predicate
            # )
        else:
            print(f"Lendo {db}.{tbl} sem filtro de partição")
            # dyf = glueContext.create_dynamic_frame.from_catalog(
            #     database=db,
            #     table_name=tbl
            # )

        # df = dyf.toDF()
        # df.createOrReplaceTempView(f"{db}_{tbl}")