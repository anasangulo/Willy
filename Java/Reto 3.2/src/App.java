
import java.net.URL;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

//WILLY CORZO

// Reto 3 Curso Programacion Basica MINTIC - Universidad del Norte

// Iniciamos la clase App
public class App extends Application {
    // Clase principal MAIN

    @Override
    public void start(Stage stage) throws Exception {
        // TODO Auto-generated method stub
        URL url = getClass().getClassLoader().getResource("GUI.fxml");
        FXMLLoader fxmlloader = new FXMLLoader(url);

        Parent root = fxmlloader.load();
        Scene scene = new Scene(root);

        stage.setTitle("SISTEMA ESTADISTICO");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) throws Exception {
        launch(args);
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
