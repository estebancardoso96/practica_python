# Creo un DF para ver repetidos por distintas variables

censo = pd.DataFrame({'id' : [1,2,3,4,1,4,4,3],
                     'barrio' : ['Buceo', 'Malvin','Cerrito','Malvin','Buceo','Malvin','Cordon','Cerrito']})

print(censo)

## repetidos por id

censo[censo['id'].duplicated()] ## muestra solamente el duplicado
censo.groupby('id').filter(lambda x: len(x)>1) ## muestra el "original" y el repetido

## ver repetidos por dos columnas o mas

censo[censo.duplicated(subset=['id','barrio'])] ## muestra solamente el duplicado
censo[censo.duplicated(subset=['id','barrio'], keep = False)] ## con el false muestra el original y el repetido

## elimnar duplicados pero de una columna

censo.drop_duplicates('barrio') ## se queda con el primer registro unico (se queda con la primer fila del registro)

## quiero quedarme con el primer registro agrupando por las dos variables

prueba = censo.drop_duplicates( subset = ['id', 'barrio'], keep = 'first').reset_index(drop = True) 
print(prueba)

## NA

## Ver las filas NA de una columna determinada

censo.query('id.isna()') ## no hay ningun na en id
