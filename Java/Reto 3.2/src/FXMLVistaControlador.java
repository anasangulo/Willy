
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class FXMLVistaControlador implements Initializable {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button btnCalcular;

    @FXML
    private Label lblSistema;

    @FXML
    private TextField txtFNumero;

    @FXML
    private TextArea txtADatos;

    @FXML
    private TextArea txtACalculos;

    @FXML
    void accionCalcular(ActionEvent event) {

    }
    
    @Override
    public void initialize(URL url, ResourceBundle resources) {
        // TODO Auto-generated method stub
        
    }

}
