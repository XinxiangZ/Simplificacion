import { Component } from '@angular/core';
import { HttpClientModule, HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { FormsModule } from '@angular/forms';



@Component({
  selector: 'app-formulario',
  standalone: true,
  imports: [FormsModule,HttpClientModule],
  templateUrl: './formulario.component.html',
  styleUrl: './formulario.component.css'
})

@Injectable({
  providedIn: 'root'
})

export class FormularioComponent {

  constructor(private http: HttpClient) { }

  textInput: string = '';
  selectedOption: string = 'Sintáctica';
  respuesta: any="z";

 

  submitForm() {

    this.http.post<any>('https://laoxin.pythonanywhere.com/', { 
      textInput: this.textInput,
      selectedOption: this.selectedOption
    }).subscribe(response => {

      this.respuesta = response.generated_text;
  
    });

    
  }

}
