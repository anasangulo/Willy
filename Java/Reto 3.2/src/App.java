import javafx.application.Application;
import javafx.stage.Stage;

//WILLY CORZO

// Reto 2 Curso Programacion Basica MINTIC - Universidad del Norte

// Iniciamos la clase App
public class App extends Application{
    // Clase principal MAIN
    

    @Override
    public void start(Stage arg0) throws Exception {
        // TODO Auto-generated method stub
        
    }

    public static void main(String[] args) throws Exception {
        // Se llama el metodo readData
        SchoolGradingSystem.loadData();
        // Se llama el metodo question1
        System.out.println(SchoolGradingSystem.stat1());
        // Se llama el metodo question2
        System.out.println(SchoolGradingSystem.stat2());
        // Se llama el metodo question3
        System.out.println(SchoolGradingSystem.stat3());
        // Se llama el metodo question4
        System.out.println(SchoolGradingSystem.stat4());
    }
}
