import { Component , Input, Output, EventEmitter } from '@angular/core';
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

  textInput: string = "";
  selectedOptionSintactica: boolean = false;
  selectedOptionLexica: boolean = false;
  selectedOptionResumen: boolean = false;
  
  respuesta: any="";

  letterCount: number = 0;
  isLimitReached: boolean = false;

  submitForm() {

    console.log(this.textInput)
    console.log(this.selectedOptionSintactica)
    console.log(this.selectedOptionLexica)
    console.log(this.selectedOptionResumen)
    this.http.post<any>('http://127.0.0.1:5000', { 
      textInput: this.textInput,
      selectedOptionSintactica: this.selectedOptionSintactica,
      selectedOptionLexica: this.selectedOptionLexica,
      selectedOptionResumen: this.selectedOptionResumen
    }).subscribe(response => {

      this.respuesta = response.generated_text;
  
    });
  }

  countWords() {
    // Split the text by spaces to count letters
    this.letterCount = this.textInput.length;

    // Check if letter count exceeds the limit
    this.isLimitReached = this.letterCount > 5000;
  }
}