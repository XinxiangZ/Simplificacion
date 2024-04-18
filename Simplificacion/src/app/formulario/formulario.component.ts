import { Component } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-formulario',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './formulario.component.html',
  styleUrl: './formulario.component.css'
})

@Injectable({
  providedIn: 'root'
})

export class FormularioComponent {

  textInput: string = '';
  selectedOption: string = '';

  //constructor(private _http: HttpClient) { }

 

  submitForm() {
    /*this.http.post<any>('http://localhost:4200/', { 
      textInput: this.textInput,
      selectedOption: this.selectedOption
    }).subscribe(response => {
      // Manejar la respuesta del servidor si es necesario
    });**/
  }

}
