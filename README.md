# Arbol de Sintaxis

## Introducción 
En esta actividad se desarrolló un analizador sintáctico en Python que permite leer una gramática libre de contexto desde un archivo (gra.txt) y posteriormente analizar una cadena de entrada para determinar si pertenece o no al lenguaje definido por la gramática. Además, el programa genera e imprime en pantalla el árbol de sintaxis, el cual representa de manera jerárquica cómo se construye la cadena a partir de las reglas gramaticales.

El propósito principal es afianzar los conocimientos sobre el proceso de análisis sintáctico en la construcción de compiladores, abordando conceptos como gramáticas, recursión por la izquierda, conjuntos First y Follow, tablas predictivas LL(1) y la construcción de árboles de derivación.

## Desarrollo 

En esta actividad se implementó en Python un analizador sintáctico que lee una gramática libre de contexto desde el archivo gra.txt y analiza cadenas de prueba para determinar si pertenecen al lenguaje definido. Además, genera un árbol de sintaxis que muestra cómo la cadena se deriva a partir de la gramática.

El programa primero lee y almacena las reglas, luego elimina la recursión por la izquierda, calcula los conjuntos First y Follow y construye la tabla que guía el análisis. También incorpora un clasificador que reconoce números como num, lo que permite procesar expresiones como 2 + 3 * 4. Durante el análisis, se usa una pila de símbolos y se van creando nodos que conforman el árbol de derivación.

- Ejemplo
  
   - Gramatica usada

<img width="160" height="52" alt="image" src="https://github.com/user-attachments/assets/1e686145-6e9e-455e-8c11-84776aeeda27" />

   - Salida

<img width="193" height="232" alt="image" src="https://github.com/user-attachments/assets/6e288b49-e162-4fa1-8a3b-eaa1bfee0f3d" />



Los resultados muestran que el sistema acepta cadenas válidas y genera su árbol sintáctico, o rechaza aquellas que no cumplen la gramática. En conclusión, se desarrolló una herramienta práctica que aplica los conceptos de gramáticas y parsing, reforzando la relación entre teoría de lenguajes formales y la construcción de compiladores.

- Ejemplo

  - Gramatica usada

<img width="187" height="53" alt="image" src="https://github.com/user-attachments/assets/19d0a086-e62c-405c-bc2e-665df386fae9" />

  - Salida
    
<img width="234" height="514" alt="image" src="https://github.com/user-attachments/assets/fee0700c-81fa-4c85-a812-4efb290792bf" />


## Conclusiones

- Se logró implementar un parser LL(1) genérico en Python que acepta como entrada cualquier gramática de la presentación 05 y cadenas de prueba, siempre que la gramática pueda adaptarse a la forma LL(1).

- El programa automatiza la eliminación de recursión por la izquierda, lo cual es fundamental para manejar gramáticas como las de expresiones aritméticas.

- El árbol de sintaxis generado ofrece una representación clara de la estructura de las cadenas, lo que facilita la comprensión del proceso de derivación.

