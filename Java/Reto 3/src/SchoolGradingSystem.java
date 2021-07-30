//WILLY CORZO

// Reto 2 Curso Programacion Basica MINTIC - Universidad del Norte

// Se utiliza el metodo de camello para declarar todas las variables ejemplo unaVariable
// Se debe implementar todo el procesamiento de información y cálculos en una clase llamada SchoolGradingSystem.
public class SchoolGradingSystem extends GradingSystem {

    // Se genera el constructor Vacio
    public SchoolGradingSystem() {
    }

    // Se genera el contructor de las variables
    public SchoolGradingSystem(float nombre, float genero, float materia, float calificacion) {
        super(nombre, genero, materia, calificacion);
    }

    // Metodo get de la variable nombre
    public float getNombre() {
        return nombre;
    }

    // Metodo set de la variable nombre
    public void setNombre(float nombre) {
        this.nombre = nombre;
    }

    // Metodo get de la variable genero
    public float getGenero() {
        return genero;
    }

    // Metodo set de la variable genero
    public void setGenero(float genero) {
        this.genero = genero;
    }

    // Metodo get de la variable materia
    public float getMateria() {
        return materia;
    }

    // Metodo set de la variable materia
    public void setMateria(float materia) {
        this.materia = materia;
    }

    // Metodo get de la variable calificacion
    public float getCalificacion() {
        return calificacion;
    }

    // Metodo set de la variable calificacion
    public void setCalificacion(float calificacion) {
        this.calificacion = calificacion;
    }

    // La clase SchoolGradingSystem debe contener un método llamado readData,
    // el cual no debe recibir ni retornar ningún parámetro.
    // El objetivo de este método es leer los valores de entrada del programa.

    

}