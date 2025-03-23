import { Component } from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-add-product',
    imports: [
        FormsModule,
    ],
  templateUrl: './add-product.component.html',
  styleUrl: './add-product.component.css'
})

export class AddProductComponent {
    name: string = "";
    description: string = "";
    link: string = "";

    constructor(private http: HttpClient) {}

    apiUrl: string = "http://localhost:8000/products";

    PostData() {
        let obj = {
            name: this.name,
            description: this.description,
            link: this.link,
        };

        let httpOptions = {
            headers: new HttpHeaders({ 'Content-Type': 'application/json' })
        };

        this.http.put(this.apiUrl, obj, httpOptions).subscribe(
            response => console.log("Success:", response),
            error => console.error("Error:", error)
        );
    }
}
