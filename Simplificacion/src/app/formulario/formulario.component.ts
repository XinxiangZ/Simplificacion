import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-formulario',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './formulario.component.html',
  styleUrl: './formulario.component.css'
})
export class FormularioComponent {

  textInput: string = '';
  selectedOption: string = '';

  constructor(private http: HttpClient) {}

  submitForm() {
    this.http.post<any>('http://tu-servidor-flask.com/procesar_datos', { 
      textInput: this.textInput,
      selectedOption: this.selectedOption
    }).subscribe(response => {
      // Manejar la respuesta del servidor si es necesario
    });
  }

}
