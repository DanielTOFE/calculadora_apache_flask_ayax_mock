FORMAT: 1A
HOST: https://polls.apiblueprint.org/

# calculadoraBasica

Realitzará les *operacions* amb els dos operands que el usuari posi i amb el *operador* que aquest seleccioni, entre els quals estàn disponibles : 
`suma`
`resta`
`multiplicació`
`divisió`;

I mostrarà el resultat de la *operació* per pantalla.


## Operacions disponibles [/CalculadoraBasica]

# Group Operacions
## Sumar [/CalculadoraBasica/suma/{op1}/{op2}]
### Sumar [GET]

+ Response 201 (application/json)

    + Body
   
            {
                "op1": 88,
                "op2": 22,
                "resultat": 110
            }
            

## Restar [/CalculadoraBasica/resta/{op1}/{op2}]
### Restar [GET]

+ Response 201 (application/json)

    + Body
   
            {
                "op1": 88,
                "op2": 22,
                "resultat": 66
            }
           

## Divisió [/CalculadoraBasica/div/{op1}/{op2}]
### Divisió [GET]

+ Response 201 (application/json)

    + Body

            {
                "op1": 88,
                "op2": 22,
                "resultat": 4
            }
           
## Multiplicació [/CalculadoraBasica/mult/{op1}/{op2}]
### Multiplicació [GET]

+ Response 201 (application/json)

    + Body

            {
                "op1": 88,
                "op2": 22,
                "resultat": 50
            }